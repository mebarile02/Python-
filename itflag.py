"""
itflag.py

Draw the Italian flag in color on a tkinter Canvas widget.

"""

import tkinter

stripeWidth = 300

root = tkinter.Tk()
root.title("Italian Flag")

width = 3*stripeWidth
height = int(width*2/3)  # Aspect ratio 2:3 according to Wiki
root.geometry(f"{width}x{height}")

"""
Hex colors corresponding to official colors on Wiki
"""

canvas = tkinter.Canvas(root, highlightthickness = 0, background = "#F4F5F0")

canvas.create_rectangle(0,0,stripeWidth,height, width = 0, fill = "#008C45")

canvas.create_rectangle(2/3*width, 0 , width, height, width = 0, fill = "#CD212A")


canvas.pack(expand = tkinter.YES, fill = "both")

root.mainloop()
