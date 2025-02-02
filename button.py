import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

# Set pin 10 to be an input pin and set initial value to be pulled low (off)
BUTTON_PIN = 10
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True: # Run forever
    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        print("Button was pushed!")
        time.sleep(0.5)
