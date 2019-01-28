from subprocess import call
import os
from tkinter import *
from tkinter import filedialog
import youtube_dl
import copy

# single video vs. part of playlist vs. full plalylist selection

root = Tk()

root.title("Youtube to MP3")
root.geometry("560x150")
root.resizable(width = False, height = False)

selection_var = StringVar()
selection_var.set("Single")

def selection():
    sel = str(selection_var.get())
    selection_label.config(text = sel)

radiogroup = Frame(root)

r1 = Radiobutton(radiogroup, text = "Single", variable = selection_var, value = "Convert a single video", command = selection)
r1.deselect()
r1.grid(row = 0, column = 0)

r2 = Radiobutton(radiogroup, text = "Part", variable = selection_var, value = "Convert a portion of a playlist", command = selection)
r2.grid(row = 0, column = 1)
r2.deselect()

r3 = Radiobutton(radiogroup, text = "Full", variable = selection_var, value = "Convert an entire playlist", command = selection)
r3.grid(row = 0, column = 2, padx = (0, 50))
r3.deselect()

start_index = StringVar()
end_index = StringVar()

Label(radiogroup, text = "First video index:").grid(row = 0, column = 3)
Label(radiogroup, text = "Last video index:").grid(row = 0, column = 5)

start_index_entry = Entry(radiogroup, bd = 5, textvariable = start_index, width = 3)
start_index_entry.grid(row = 0, column = 4)
end_index_entry = Entry(radiogroup, bd = 5, textvariable = end_index, width = 3)
end_index_entry.grid(row = 0, column = 6)

radiogroup.grid(row = 0, columnspan = 3)

currdir = os.getcwd()

def directory_browser():
    global filepath
    filename = filedialog.askdirectory(parent = root, initialdir = currdir, title = "Choose where to save converted videos")
    filepath.set(filename)

filepath = StringVar()

# filepath selection
Label(root, text = "Select download folder: ").grid(row = 4, sticky = W)

directory_entry = Entry(root, bd = 5, width = 34, textvariable = filepath)
directory_entry.grid(row = 4, column = 1, sticky = W)

browse_button = Button(root, text = "Browse", command = directory_browser)
browse_button.grid(row = 4, column = 2)

# video/playlist URL insertion
video_url = StringVar()
Label(root, text = "Video or Playlist URL:").grid(row = 5, sticky = W)
url_entry = Entry(root, bd = 5, textvariable = video_url, width = 34)
url_entry.grid(row = 5, column = 1, sticky = W)

selection_label = Label(root)
selection_label.grid(row = 6, columnspan = 3)

# youtube-dl options and download command

ydl_base_options = {
    "format": "bestaudio/best", 
    "postprocessors": [{
        "key": "FFmpegExtractAudio", 
        "preferredcodec": "mp3", 
        "preferredquality": "192"
    }], 
    "ignoreerrors": True
}

# convert video, cd if applicable, other background processes

def convert_video():
    os.chdir(filepath.get())

    # TODO: add branched functionality for whichever option the user selected
    ydl_options = copy.deepcopy(ydl_base_options)

    if selection_var.get() == "Single":
        ydl_options["noplaylist"] = True

    # TODO: add start range and end range entry boxes (may need try/catch)
    if selection_var.get() == "Part":
        ydl_options["playliststart"] = start_index.get()
        ydl_options["playlistend"] = end_index.get()

    with youtube_dl.YoutubeDL(ydl_options) as ydl:
        ydl.download(video_url)

convert_button = Button(root, text = "Convert", command = convert_video)
convert_button.grid(row = 5, column = 2)

root.mainloop()