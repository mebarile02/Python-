"""
checkerboard.py


Draw a checkerboard on a tkinter Canvas widget.
"""

import tkinter

boxHeight = 40

root = tkinter.Tk()
root.title("Checkerboard")

board_height = 8*boxHeight
board_width = board_height
root.geometry(f"{board_width}x{board_height}")

canvas = tkinter.Canvas(root, highlightthickness = 0, background = "white")

for i in range(8):
    if i%2 == 0:
        for j in range(8):
            if j%2 != 0:
                canvas.create_rectangle(boxHeight*j,boxHeight*i,
                    boxHeight*(j+1),boxHeight*(i+1), width = 0, fill = "black")
    else:
        for j in range(8):
            if j%2 == 0:
                canvas.create_rectangle(boxHeight*j,boxHeight*i,
                boxHeight*(j+1),boxHeight*(i+1), width = 0, fill = "black")

canvas.pack(expand = tkinter.YES, fill = "both")

root.mainloop()
                
    
