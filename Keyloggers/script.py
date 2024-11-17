import keyboard  # Importing the keyboard module for capturing and replaying keystrokes
from colorama import Fore, Style, init  # Importing colorama for colorful terminal output
import time  # Importing time module for delay effects

# Initialize colorama for color support across platforms
init(autoreset=True)

# Display banner with tool name and author
print(f"{Fore.CYAN}{Style.BRIGHT}")
print("==============================================")
print("        KEYPRESS RECORDER by NAITRO 07")
print("==============================================")
print(Style.RESET_ALL)

# Prompt the user to start recording
print(f"{Fore.YELLOW}Press any keys to record. Press ENTER to stop recording.{Style.RESET_ALL}")
time.sleep(1)

# Record all keystrokes until "ENTER" is pressed
keys = keyboard.record(until='ENTER')  # Capturing keystrokes until the ENTER key is pressed

# Notify user that recording has stopped
print(f"\n{Fore.GREEN}[+] Recording complete. Replaying recorded keystrokes...{Style.RESET_ALL}")
time.sleep(1)

# Replay the recorded keystrokes
keyboard.play(keys)  # Replaying the captured keystrokes as they were entered

# Final message to indicate the script has finished executing
print(f"{Fore.CYAN}[+] Keystroke playback complete! Thank you for using KEYPRESS RECORDER by NAITRO 07.")
