# youtube-to-mp3 

## Installation instructions

### 1. Download FFmpeg
####  Linux users

##### Run `sudo apt-get install ffmpeg` from the command line.

####  macOS users

##### If you have homebrew installed (easiest):

Enter `brew install ffmpeg` in Terminal.
      
##### If you don't have homebrew installed, but would like to install it to make this easier:
Open the Terminal (search "Terminal" from the Launchpad), and paste the following command, hit enter to execute it, then enter again to accept.

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" && brew install ffmpeg
```

Follow the instructions here: http://macappstore.org/ffmpeg/

##### Alternatively, the hard way (if you have a 64-bit OS):

Download the static build here: https://ffmpeg.zeranoe.com/builds/

####  Windows users

##### No setup required. Proceed to Step 2 (Download and Set Up Youtube to MP3)

### 2. __Download and Set Up Youtube to MP3__
<details>
<summary>macOS users</summary>

1. On this page, go to the `build_osx` folder, and click on `Youtube to MP3-1.0.dmg`.
2. Near the top right, click the __Download__ button.
3. For the pop-up in the download bar, click the arrow next to the Discard button and select "Keep".
4. After clicking the dmg file, drag the icon in the folder that pops up to your Dock.
5. Run `setup_mac.sh` by double-clicking it or running `./setup_mac.sh` at the command line. You're now good to go.


</details>

#### Windows users

      Simply download (save it somewhere you can find easily later) and run `youtube-to-mp3-gui.exe` at [gui/dist](gui/dist)

#### Linux users

      Work in progress

## Usage

1. Open the GUI application by double-clicking `youtube-to-mp3-gui.py` wherever you installed it.
2. Browse for a download location (where your converted mp3 file will be downloaded). The default is the same folder that `youtube-to-mp3-gui.py` is in.
3. Select the type of conversion you'd like to make; default is "Single Video" if the URL is that of a single video or video in a playlist. To download a playlist or part of a playlist, select one of the other two options.
3. Enter a valid YouTube video or playlist URL corresponding to your choice above and click "Convert". After a few seconds your conversions should appear in the folder you chose above.