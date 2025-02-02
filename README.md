# New Years Countdown

Bundle of scripts and manuals on how to setup this new-years countdown using a raspberry pi 3+ B and an old TV with an AV input. Push button can be plugged in to raspi to switch between countdown and screen-saver video.


## What You Need to Know

I had this old, small TV with a AV-Input (Analog Video) and a Raspberry Pi 3+ B laying around and thought I tinker with that for a private new years party. The raspi has a AV-Output which you might have to setup as the standard out. [This video](https://www.youtube.com/watch?v=9m8ScViTZi0&t=386s) helped me with the setup.

### Main Script

The script `new_years.py` is the main script. When executed, it opens the file `countdown/index.html`, which displays a clock in a new-years theme, counting down to the upcomming end of the year. The css style templates and the java-script for the flip-countdown is borrowed from [here](https://pqina.nl/flip/).

### Push Button

The main script has an implementation for detecting a signal input at `BUTTON_PIN`, which I realized with a push button. Every time the button is pushed, the screen switches from one display to the other. For my setup, these displays were the countdown and a screen-saver video, which was localy stored as an `.mp4`-file.

### Sudo Files

The raspi root file `boot/config.txt` must be altered to enable a valid video-output to the AV-jack. Not gonna lie, this was a pain to figure out and might be different for your controlling device. The file found in this repo under `sudo_files/config.txt` did the trick for me.


Last Read-Me update: 2025-02-02