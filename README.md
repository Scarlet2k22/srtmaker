
# CSV to SRT Subtitle Converter

### 📜 Project Description
CSV to SRT Subtitle Converter is a Python script that converts subtitles stored in a CSV file into the popular SRT format for video players. The script automatically calculates subtitle duration based on character count, ensures appropriate line length, and provides a convenient file selection interface.

### 🎯 Features
- **CSV to SRT Conversion:** Supports CSV files containing subtitles and converts them to SRT format.
- **Convenient File Selection Interface:** Users can easily choose a CSV file to convert using Tkinter.
- **Success Notifications:** The script displays conversion status messages.
- **Subtitle Duration Control:** Considers reading speed and restricts subtitle display time.
- **Line Splitting:** Improves readability by automatically splitting overly long lines.

### 📋 Parameters
- **FRAME_RATE** - The video frame rate for time synchronization (default: 25 FPS).
- **MIN_DURATION** - Minimum subtitle display time in seconds (default: 1 second).
- **MAX_DURATION** - Maximum subtitle display time in seconds (default: 7 seconds).
- **CHARS_PER_LINE** - Maximum number of characters per line (default: 42 characters).
- **READING_SPEED** - Reading speed in characters per second (default: 20 characters/second).

### 🛠️ Requirements
- Python 3.x
- Python Libraries:
  - `csv`
  - `os`
  - `tkinter`
  - `re`
  - `sys`

### 🔧 Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Scarlet2k22/srtmaker.git
    cd srtmaker
    ```
2. Ensure you have Python 3.x and the required libraries installed.
3. Run the script.

### 🚀 How to Use
1. Run the script using:
   ```bash
   python srtmaker.py
   ```
2. Select the CSV file you wish to convert using the file selection dialog.
3. The script will automatically convert the CSV file to SRT format and save it in the `converted` folder located in the same directory as the CSV file.
4. A success message will be displayed upon completion.

### 📂 CSV Structure
The CSV file should have the following format:
- **Column 1**: Start time in `HH:MM:SS:FF` format (hours:minutes:seconds:frames).
- **Column 2**: Subtitle text.

Example:
```csv
00:00:01:10, Welcome to our video.
00:00:05:20, Today we discuss subtitles.
```

### 🎉 Example Usage
Here's an example of a CSV file and its SRT conversion:
- **CSV Input**:
  ```csv
  00:00:01:10, Sample subtitle one.
  00:00:05:20, Another sample subtitle for the video.
  ```
- **SRT Output**:
  ```
  1
  00:00:01,400 --> 00:00:03,500
  Sample subtitle one.

  2
  00:00:05,800 --> 00:00:08,000
  Another sample subtitle for the video.
  ```

### ✨ Parameter Customization

After selecting a CSV file for conversion, you can now customize key subtitle parameters such as frame rate, minimum and maximum subtitle durations, characters per line, and reading speed. These settings allow for precise control over the subtitle timing and display, ensuring optimal readability.

### 🛠️ Building the Project

To build the application for your operating system, run `build.py` with the desired target as an argument. This script will compile the code into a standalone executable for Windows, macOS, or Linux.

#### Usage:
- **Windows**:
  ```bash
  python build.py Windows
  ```
- **macOS**:
  ```bash
  python build.py Darwin
  ```
- **Linux**:
  ```bash
  python build.py Linux
  ```

By default, if no argument is provided, the script will detect and use the current operating system.

The output files will be located in the `dist` directory.

### 💡 Notes
- If your video file has a different frame rate, adjust the `FRAME_RATE` value to synchronize times accurately.
- Use the `MIN_DURATION` and `MAX_DURATION` parameters to control subtitle display duration.

### 📜 License
This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License. You may use, modify, and share the code for non-commercial purposes, provided that you give appropriate credit. For more details, refer to the [full license text](LICENSE).

---

Enjoy using the tool, and best of luck with your subtitles! If you have any questions, don't hesitate to reach out.
