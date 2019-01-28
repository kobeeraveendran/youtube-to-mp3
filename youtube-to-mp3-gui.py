from subprocess import call
import os
import argparse
from tkinter import *
from tkinter import filedialog

# single video vs. part of playlist vs. full plalylist selection

root = Tk()

root.title("Youtube to MP3")
root.geometry("560x150")
root.resizable(width = False, height = False)

var = StringVar()

def selection():
    sel = str(var.get())
    selection_label.config(text = sel)

radiogroup = Frame(root)

r1 = Radiobutton(radiogroup, text = "Single", variable = var, value = "Convert a single video", command = selection)
r1.grid(row = 0, column = 0, padx = 50)
#r1.deselect()

r2 = Radiobutton(radiogroup, text = "Part", variable = var, value = "Convert a portion of a playlist", command = selection)
r2.grid(row = 0, column = 1, padx = 50)
#r2.deselect()

r3 = Radiobutton(radiogroup, text = "Full", variable = var, value = "Convert an entire playlist", command = selection)
r3.grid(row = 0, column = 2, padx = 50)
#r3.deselect()

radiogroup.grid(row = 0, columnspan = 3)

def browse_button():
    global filepath
    filename = filedialog.askdirectory()
    filepath.set(filename)

filepath = StringVar()


Label(root, text = "Select download folder: ").grid(row = 4, sticky = W)

directory_entry = Entry(root, bd = 5, width = 40)
directory_entry.grid(row = 4, column = 1, sticky = E)

selection_label = Label(root)
selection_label.grid(row = 6, columnspan = 3)

Label(root, text = "Video or Playlist URL:").grid(row = 5, sticky = W)
url_entry = Entry(root, bd = 5, width = 40)
url_entry.grid(row = 5, column = 1, sticky = E)

root.mainloop()

'''
class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()


    def init_window(self):
        self.master.title("Youtube to MP3")
        self.pack(fill = BOTH, expand = 1)
        self.options()

    def options(self):
        
        var = StringVar()
        def selection():
            sel = str(var.get())
            selection_label.config(text = sel)

        r1 = Radiobutton(root, text = "Single", variable = var, value = "Convert a single video")
        r1.place(x = 80, y = 25)
        r1.deselect()

        r2 = Radiobutton(root, text = "Part", variable = var, value = "Convert a portion of a playlist")
        r2.place(x = 180, y = 25)
        r2.deselect()

        r3 = Radiobutton(root, text = "Full", variable = var, value = "Convert an entire playlist")
        r3.place(x = 280, y = 25)
        r3.deselect()

        selection_label = Label(root)

        
'''


