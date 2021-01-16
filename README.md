# stm32-audio

this contains some code for the stm32f303 microcontroller. unlike the 8 bit atmega32 this hss a 32 bit ARM processor with floating point and DSP instructions 
and has many and better peripherals useful for audio including more timers of higher resolution, a DMA controller and a built in digital to analog converter.
At the same time its also really cheap  - about £5 for a development board from china. or ten from the official company.

In this repository is some code that is intended to play back audio from data stored in the flash memory and a 
python script to turn the samples_data.txt file exported from audacity into a c header filer for use in the program. This is still a workl in progress...

There's also a some code i've written to control shift registers, allowing 16 LEDS to be controlled from only three pins using two shift registers. 
This will form the basis of a tr-606  style sequencer for a drum machine

Unlike atmel studio, STM's "cube" IDE will generate code for you to initialize any peripherals you might want to use using a GUI and comes with a hardware abstraction
library.

