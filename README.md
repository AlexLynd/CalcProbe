# 6 function calculator hack
I couldn't think of a better name, but this is a mostly hardware hack that allows you to use a standard six function calculator to do anything you want given the limited interface of about 20 push buttons, and a monochrome LCD.  Everything else is scripted to run autonomously.  The Code is still in development stage, and is poorly maintained by me and a friend.
## Things to Add
* Startup script
* UART serial integration
* Code that actually works

## How it Works
The PCB on a standard calculator is composed of a key matrix, a microcontroller, and a small LCD.  We hooked up a Raspberry Pi Zero to the key matrix to spoof keypresses by shorting columns and rows, allowing it to send information very fast.  The Raspberry Pi can also detect keypresses from the user, and as a result, we can use the Raspberry Pi as a MITM (man in the middle), to intercept keystrokes sent back and forth.  If the user enters a specific preset set of keystrokes like 111000, the Pi will detect this and can run a custom script, something like solve a complex equation based on the next 3 inputs, or start logging wifi data with a wifi card.  Essentially all this project is is a Rasperry Pi with 20 keys, a screen with only digits, and whatever else you can fit in the case of a Pi Zero.
## How to Use
This is under development stage, but I will soon write a guide.  Clone this repository, and change calc_modules to include whatever programs *you* want.  In calc_source, include the programs you want to use at the time.  I am still improving modulation.  
