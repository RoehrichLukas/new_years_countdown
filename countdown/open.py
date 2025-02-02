import os
import signal
import time

# Function to handle script termination
def cleanup(signum, frame):
    print("\nTerminating script. Closing browser...")
    os.system("pkill chromium-browser")
    os.system("pkill unclutter")
    exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, cleanup)

# File path for the HTML file
fp = './index.html'

# Open the file using the Raspberry Pi's browser in 50% zoom and fullscreen mode
print("Opening Browser...")
os.system(f"DISPLAY=:0 chromium-browser --app=file://{os.path.abspath(fp)} "
          f"--force-device-scale-factor=1.0 --start-fullscreen &")
time.sleep(2)
print("Browser opened!\nLoading Page...")
time.sleep(5)
print("Page should be loaded.\nHidding Cursor.")

# Hide the Mouse Cursor
os.system("DISPLAY=:0 unclutter -idle 0 &")

# Keep the script running until interrupted
print("\nScript running. Press Ctrl+C to exit.")
try:
    while True:
        time.sleep(1)  # Keep the script alive
except KeyboardInterrupt:
    cleanup(None, None)
