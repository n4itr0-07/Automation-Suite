# Keypress Recorder

**Keypress Recorder by NAITRO 07** is a simple Python tool that records keystrokes until the `ENTER` key is pressed, then replays them in the same sequence. This can be useful for automating repetitive typing tasks, testing, or educational purposes.

---

## Features

- **Record and Replay Keystrokes**: Records all keystrokes until `ENTER` is pressed and then replays them exactly as they were typed.
- **Interactive and Colorful Terminal Output**: User-friendly prompts and notifications with colorful output, enhancing the interaction.
- **Simple to Use**: Minimal setup required; just start typing to record and press `ENTER` to stop.

---

## Setup

### Prerequisites

1. **Python 3.x**: Ensure Python is installed on your system.
2. **Required Modules**:
   - **keyboard**: Used to record and replay keystrokes. Install via:
     ```bash
     pip install keyboard
     ```
   - **colorama**: Adds color support for cross-platform terminals. Install via:
     ```bash
     pip install colorama
     ```

### Files

- **`script.py`**: This is the main script that handles the recording and replaying of keystrokes.

---

## Usage

1. **Run the Script**:
   - Open a terminal in the directory where `script.py` is located.
   - Run the script with:
     ```bash
     python script.py
     ```

2. **Record Keystrokes**:
   - Once the script starts, type any keys you want to record. The script will keep recording until you press the `ENTER` key.
   
3. **Playback**:
   - After pressing `ENTER`, the script will replay all recorded keystrokes in the same order they were typed.

---

## Example Output

Here’s an example of what the output might look like when you run the script:

```plaintext
==============================================
        KEYPRESS RECORDER by NAITRO 07
==============================================

Press any keys to record. Press ENTER to stop recording.

[+] Recording complete. Replaying recorded keystrokes...

[+] Keystroke playback complete! Thank you for using KEYPRESS RECORDER by NAITRO 07.
```

### Notes

- **Keyboard Capture Permissions**: The script may require admin privileges or specific permissions to capture keyboard inputs, depending on your system.
- **Ethical Usage**: Please use this tool responsibly. **Do not use it for unauthorized keystroke logging**, as this is illegal and unethical. The tool is intended for automation and testing purposes only.

---

## Troubleshooting

- **Keyboard Module Issues**: If you get an error regarding the `keyboard` module, make sure you’re running the script with appropriate permissions, as some systems restrict key logging features.
- **Playback Delay**: If playback is too fast, consider adding a slight delay in the script between keystrokes (using `time.sleep()`).

---

## Legal Disclaimer

This tool is for **educational and ethical purposes only**. Unauthorized keystroke logging is illegal. Use this tool only in environments where you have permission.

---

Enjoy using **Keypress Recorder by NAITRO 07** for your automation and testing needs! 😊