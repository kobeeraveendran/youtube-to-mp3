# youtube-to-mp3 

## Installation instructions 

### (if installing on Windows, skip to step 2)

### 1. Download FFmpeg

<details>
<summary>Linux users</summary>

##### Run `sudo apt-get install ffmpeg` from the command line.
</details>

<details>
<summary>macOS users</summary>

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

</details>

<details>
<summary>Windows users</summary>

##### No setup required. Proceed to Step 2 (Download and Set Up Youtube to MP3)
</details>

### 2. __Download and Set Up Youtube to MP3__
<details>
<summary>macOS users</summary>

1. On this page, go to the `build_osx` folder, and click on `Youtube to MP3-1.0.dmg`.
2. Near the top right, click the __Download__ button.
3. For the pop-up in the download bar, click the arrow next to the Discard button and select "Keep".
4. After clicking the dmg file, drag the icon in the folder that pops up to your Dock.
5. Run `setup_mac.sh` by double-clicking it or running `./setup_mac.sh` at the command line. You're now good to go.


</details>

<details>
<summary>Windows users</summary>

Download `youtube-to-mp3-gui.exe` from [gui/dist](https://github.com/kobeeraveendran/youtube-to-mp3/blob/master/gui/dist/youtube-to-mp3-gui.exe) by clicking "Download" near the right of your screen (next to History), and save it somewhere you can find it easily later.

*(If you are prompted with a dialog box saying that the app is unrecognized, click "More Info" then "Run Anyway"). This only appears because I developed this myself and released it here, open source, and is such not registered with Microsoft.*

</details>

<details>
<summary>Linux users</summary>

      Work in progress
</details>

## Usage

1. Browse for a download location (where your converted mp3 file will be downloaded). The default is the same folder that `youtube-to-mp3-gui.py` is in.
2. Select the type of conversion you'd like to make; default is "Single Video" if the URL is that of a single video or video in a playlist. To download an entire playlist or part of a playlist, select one of the other two options.

      ***NOTE: At the moment, converting Single videos is functional and has been tested for Windows users. The other two options will likely not be functional on Windows and other platforms. A fix is coming.***

3. Enter a valid YouTube video or playlist URL corresponding to your choice above and click "Convert". After a few seconds your conversions should appear in the folder you chose above.

Note: depending on which platform you're using, you may see console/terminal windows pop up after pressing "Convert". This is normal: it is simply ffmpeg converting the video into an audio format.