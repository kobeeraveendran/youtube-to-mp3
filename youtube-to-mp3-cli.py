from subprocess import call
import os
import argparse

parser = argparse.ArgumentParser(description = 'Convert and download individual YouTube songs, an entire playlist, or a portion of a playlist.')


# for downloading an entire playlist or part of a playlist
#parser.add_argument("url",  help = "URL of the target video to be converted, or URL of the target playlist")
parser.add_argument("--song_range", nargs = 2, help = "download part of a playlist by specifying a start number and end number")
parser.add_argument("--full-playlist", action = 'store_true', help = "download entire playlist")

args = parser.parse_args()

pwd = input("Enter folder to save converted video(s) in: ")
os.chdir(pwd)

if not args.song_range and not full_playlist:
    cmd = "youtube-dl --extract-audio --audio-format mp3 " + str(args.url)
    cmd = cmd.split()

if args.song_range:
    print('Downloading index {0} to {1} of playlist...'.format(args.song_range[0], args.song_range[1]))

    # might need --yes-playlist
    cmd = "youtube-dl --extract-audio --audio-format mp3 -i --playlist-start " + str(args.song_range[0]) + " --playlist-end " + str(args.song_range[1]) + " " + args.url
    cmd = cmd.split()

if args.full_playlist:
    print('Downloading all songs in target playlist...')
    cmd = "youtube-dl --extract-audio --audio-format mp3 -i --yes-playlist " + args.url
    cmd = ["youtube-dl", "--extract-audio", "--audio-format", "mp3", "-i", "--yes-playlist", args.url]


# execute terminal command
#call(cmd)