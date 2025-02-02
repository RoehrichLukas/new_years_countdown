"""
Coded by Lukas Röhrich, Berlin, Germany
 - for New Years Party 2024/25

Happy Coding!
"""

import RPi.GPIO as GPIO
import os
import signal
import time

# Function to handle script termination
def cleanup(signum, frame):
    """
    Executed when this script is cancelled.
	- closes browser properly
	- reappearing mouse cursor
    """

    print("\nTerminating script. Closing browser...")
    os.system("pkill -TERM chromium-browser")
    os.system("pkill unclutter")
    exit(0)

def toggle_page():
    """
    Imitates a key-press Ctrl+Tab, which switches tabs in a standard browser.
    """

    os.system("DISPLAY=:0 xdotool key ctrl+Tab")
    time.sleep(0.5)

# setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
BUTTON_PIN = 10							                    # set raspberry pi pin number
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Register the signal handler
signal.signal(signal.SIGINT, cleanup)

# File path for the HTML file for the countdown
fp_countdown = './countdown/index.html'
# Local video file path
fp_video = '/path/to/video/'					            # either local or online
								                            # script is written for local file
                                                            # opened in chromium browser
# Open the first file (Countdown) in Chromium
print(">> Opening Countdown...")
os.system("rm -rf ~/.config/chromium/Default/Sessions/*")   # Clear previous Session data
os.system(f"DISPLAY=:0 chromium-browser "
          f"file://{os.path.abspath(fp_countdown)} "
          f"--disable-restore-session-state "			    # to not automatically restore old session
          f"--disable-session-crash-bubble "			    # to omitt browser asking to restore last session
          f"--no-first-run "					            # to omitt introduction
          f"--force-device-scale-factor=1.0 "			    # zoom of browser
	  f"&")
time.sleep(5)  							                    # Wait for the browser to load
print("Done!")

# Open the second file (Video) in a new tab
print(">> Opening Video...")
os.system("DISPLAY=:0 xdotool key ctrl+t")			        # Open a new tab
time.sleep(1)							                    # Small delay to ensure the new tab is active
os.system(f"DISPLAY=:0 xdotool type --delay 100 '{os.path.abspath(fp_video)}'")
os.system("DISPLAY=:0 xdotool key Return")			        # Open the video
time.sleep(7)							                    # Wait for the video page to load
print("Done!")

# Enable the Loop Option on the Video
print(">> Enabling Video Loop.")
os.system("DISPLAY=:0 xdotool click 3")				        # Right-click
os.system("DISPLAY=:0 xdotool key Down")			        # Select 'Loop'
os.system("DISPLAY=:0 xdotool key Return")			        # Confirm
# Disable Player Controlls
print(">> Disabling Player Controlls.")
os.system("DISPLAY=:0 xdotool click 3")				        # Right-click
os.system("DISPLAY=:0 xdotool key Down")
os.system("DISPLAY=:0 xdotool key Down")			        # Select Player Controlls
os.system("DISPLAY=:0 xdotool key Return")			        # Confirm

# change to fullscreen
os.system(f"DISPLAY=:0 xdotool key F11")
time.sleep(2)


# Hide the Mouse Cursor (Optional)
print(f"Hiding Mouse Cursor.")
os.system("DISPLAY=:0 unclutter -idle 0 &")


# toggle between the pages
print("\nScript running. Press Ctrl+C to exit.\nListening for button push...")
while True:
    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        print("Button push detected.")
        toggle_page()

# Keep the script running until interrupted
print("\nScript running. Press Ctrl+C to exit.")
try:
    while True:
        time.sleep(1)						# Keep the script alive
except KeyboardInterrupt:
    cleanup(None, None)
