# Auto-Shutdown-Bot
This is a simple Python-based tool that automates the shutdown process of your computer, providing vocal notifications throughout the countdown. The tool utilizes text-to-speech (TTS) to announce the start of the shutdown sequence, progress updates, and the final countdown before shutting down your system.

Features:
Text-to-Speech Notifications: Provides vocal feedback for every step of the shutdown process.

Customizable Shutdown Timer: Allows you to set the time (in minutes) before your system shuts down.

Progress Updates: Announces random progress updates depending on the total time.

Final Countdown: Announces the last 60 seconds, 30 seconds, and individual seconds as it nears shutdown.

Requirements:
Python 3.x

pyttsx3 library for text-to-speech functionality.

How to Use:
Clone or download this repository.

Install the required dependencies using:

pip install pyttsx3

Run the script:

python shutdown_tool.py
Enter the desired time in minutes before the automatic shutdown starts.

Example Output:
"Welcome to Auto Shutdown Tool. Enter time in minutes before shutdown."

"Automatic shutdown sequence has been started."

"Automatic shutdown sequence is in progress."

"60 seconds remaining."

"Shutdown sequence has been completed, shutting down your PC."

License:
This project is open-source and available under the MIT License.
