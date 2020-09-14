# declarative to import all tkinter constructs
# you can install it on your conda env by running the command conda install -c anaconda tk
from tkinter import *

# static call to Tk() constructor to create a model of the window
root = Tk()

# specify container layouts that works as Frames and operates over the Tk() constructor
top = Frame(root)
top.pack()     # this ensures that the container is visible when it is attributed

bottom = Frame(root)   # another frame for the bottom layout
bottom.pack(side = BOTTOM)     # overloading pack() to explicitly shift container to the bottom of the window
# You don't need to do that for the top frame, but you can like topframe.pack(side = TOP) explicitly if you feel like
# it. by default, containers will take up everything and auto-adjust when they reach the end of screen or when they
# encounter an interruption like another container window in their layout

# we call the Button object which can be overloaded with other parameters like fg, bg if you feel the need to - not necessary)
# we specify the frame buffer to load the button object into, and then the button text (something like we do with input type)
b1 = Button(top, text="Button 1", fg="red")

# button to be placed in second frame buffer
b2 = Button(bottom, text="Button 2", fb="blue")

# in python, the frame would close the moment it is rendered which is very fast. so in order to keep it visible and close
# explicitly only when facilitated by the user, we call mainloop to keep it running as an activity or a process tree
root.mainloop()
