from subprocess import call
import os
import argparse
from tkinter import *

top = Tk()

# single video vs. part of playlist vs. full plalylist selection

def selection():
    sel = str(var.get())
    selection_label.config(text = sel)

var = StringVar()

r1 = Radiobutton(top, text = "Single", variable = var, value = "Convert a single video", command = selection)
r1.pack(anchor = NW)

r2 = Radiobutton(top, text = "Part", variable = var, value = "Convert a portion of a playlist", command = selection)
r2.pack(anchor = N)

r3 = Radiobutton(top, text = "Full", variable = var, value = "Convert an entire playlist", command = selection)
r3.pack(anchor = NE)

selection_label = Label(top)
selection_label.pack()

# URL entry
url_label = Label(top, text = "Video or Playlist URL")
url_label.pack(side = LEFT)
E1 = Entry(top, bd = 5)
E1.pack(side = RIGHT)

top.mainloop()