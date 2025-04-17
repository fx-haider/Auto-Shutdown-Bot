import os
import time
import pyttsx3
import random

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set voice to female
voices = engine.getProperty('voices')
for voice in voices:
    if "female" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break  # Use the first available female voice

def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

# Welcome message
speak("Welcome to Auto Shutdown Tool. Enter time in minutes before shutdown.")
print("Welcome to Auto Shutdown Tool.")

# Ask for shutdown time in minutes
minutes = int(input("Enter time in minutes before shutdown: "))
seconds = minutes * 60

# Announce start
speak("Automatic shutdown sequence has been started.")
print("Automatic shutdown sequence has been started.")

# Decide when to say "in progress" based on time
progress_announcements = []
if seconds > 600:  # More than 10 minutes
    count = 2 if seconds <= 1800 else 4  # 2-3 times for 10-30 min, 4-5 times for >30 min
    progress_announcements = sorted(random.sample(range(600, seconds - 60, 600), count))

# Countdown loop
for remaining in range(seconds, 0, -1):
    print(f"Shutting down in {remaining // 60}m {remaining % 60}s...", end="\r")
    
    if remaining in progress_announcements:
        speak("Automatic shutdown sequence is in progress.")
        print("\nAutomatic shutdown sequence is in progress.")

    if remaining == 60:
        speak("60 seconds remaining.")
        print("\n60 seconds remaining.")

    if remaining == 30:
        speak("30 seconds remaining.")
        print("\n30 seconds remaining.")

    if remaining <= 10:
        speak(str(remaining))

    time.sleep(1)

# Final shutdown announcement
speak("Shutdown sequence has been completed, shutting down your PC.")
print("\nShutdown sequence has been completed, shutting down your PC.")

# Force shutdown (closes all apps)
os.system("shutdown /s /f /t 0")
