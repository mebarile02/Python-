"""
itflag_loop.py

Draw the Italian flag in color on a tkinter Canvas widget.

"""

import tkinter

root = tkinter.Tk()
root.title("Italian Flag")


#Hex colors corresponding to official colors on Wiki, left to right.

colors = [
    "#008C45", #green
    "#F4F5F0", #white
    "#CD212A"  #red
]

stripeWidth = 300
width = len(colors) * stripeWidth
height = int(width * 2/3)  # Aspect ratio 2:3 according to Wiki
root.geometry(f"{width}x{height}")

canvas = tkinter.Canvas(root, highlightthickness = 0)

for i, color in enumerate(colors):
    canvas.create_rectangle(i * stripeWidth, 0, (i + 1) * stripeWidth,
height, width = 0, fill = color)

canvas.pack(expand = tkinter.YES, fill = "both")
root.mainloop()
