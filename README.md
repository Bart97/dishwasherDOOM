# Dishwasher DOOM

This is a fork of fbDOOM patched to run on a Whirlpool dishwasher.

Whirlpool used to have a line of high-end dishwashers with a graphical TFT display and WiFi connectivity. The UI board used in those dishwashers is of course running Linux.

## Necessary patches

In order to get fbDOOM running properly on the board I had to overcome two issues.

First, the display orientation was incorrect. DOOM was being rendered vertically on the screen, which made it very hard to play. I was not able to figure out a way to rotate the display at the OS level, so I modified the framebuffer copying algoritm in fbDOOM to rotate the output by 90 degrees. The output should also be scaled up, so the game has to be run with -scaling 2.

The second issue was input. I don't see any reasonable way to attach a keyboard to the board. The CPU does not support USB OTG and reverse engineering the board to find some available input pins to hook up some buttons seems like too much effort. As a workaround I've modified the input implementation in fbDOOM to receive raw scancodes via the UART port available on the board. I've also prepared a Python script that will capture keyboard input from another PC and output the scancodes using a USB to UART converter.

