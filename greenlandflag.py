"""
itflag.py

Draw the flag of Greenland in color on a tkinter Canvas widget.

"""

import tkinter

stripeHeight = 6*50

root = tkinter.Tk()
root.title("Flag of Greenland")

height = 2*stripeHeight
width = int(height*3/2)  # Aspect ratio 2:3 according to Wiki
root.geometry(f"{width}x{height}")

"""
Hex colors corresponding to official colors on Wiki
"""

canvas = tkinter.Canvas(root, highlightthickness = 0, background = "#c8102e")

canvas.create_rectangle(0, 0, width, height/2, width = 0, fill = "white")

canvas.pack(expand = tkinter.YES, fill = "both")

xCenter = (7/18)*width
yCenter = height/2
radius = 0.5*(8/18)*width

x0 = xCenter - radius
y0 = yCenter + radius
x1 = xCenter + radius
y1 = yCenter - radius

coord = x0, y0, x1, y1
canvas.create_arc(coord, start = 0, extent = -180, fill = "white",
    outline = "white")
canvas.create_arc(coord, start=0, extent = 180, fill = "#c8102e",
    outline = "#c8102e")

root.mainloop()
