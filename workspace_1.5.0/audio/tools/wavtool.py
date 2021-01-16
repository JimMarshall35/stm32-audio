import re

inputurl = "sample-data-easy_champ.txt" 
outfile = open("output.h", 'w')

once = True
with open(inputurl, 'r', encoding='utf-8') as infile:
    for line in infile:
        try:
            f = float(line)
            integer = 2048 + round(2048 * f)
            if once:
                outfile.write("const uint16_t samples[] = {\n")
                once = False
            outfile.write("\t\t\t"+str(integer)+",\n")
        except:
            srate = re.findall("Sample Rate",line)
            samplesprocessed  = re.findall("Length processed",line)
            matches = re.findall('[0-9,.]+',line)
            matches = list(filter(lambda a: a != '.', matches))
            #print(matches)
            if len(srate) > 0:
                outfile.write("#define SAMPLE_RATE "+ matches[0]+"\n")
            if len(samplesprocessed) > 0:
                outfile.write("#define LENGTH_SAMPLES "+matches[0]+"\n")
                outfile.write("#define DURATION "+matches[1]+"\n")               
            print(line)
        
outfile.write("};")
outfile.close()
input()
