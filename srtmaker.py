# CSV to SRT Subtitle Converter
# Licensed under the Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
# For non-commercial use only

import csv
import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import re
import sys

FRAME_RATE = 25  # Adjust this if your frame rate is different
MIN_DURATION = 1.0  # Minimum subtitle duration in seconds
MAX_DURATION = 7.0  # Maximum subtitle duration in seconds
CHARS_PER_LINE = 42  # Maximum characters per line
READING_SPEED = 20  # Characters per second for an average reader

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def time_to_seconds(time_str):
    hours, minutes, seconds, frames = map(int, time_str.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds + frames / FRAME_RATE
    return total_seconds

def seconds_to_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    whole_seconds = int(seconds)
    milliseconds = int((seconds - whole_seconds) * 1000)
    return f"{int(hours):02d}:{int(minutes):02d}:{whole_seconds:02d},{milliseconds:03d}"

def count_words(text):
    return len(re.findall(r'\w+', text))

def estimate_subtitle_duration(text):
    char_count = len(text)
    word_count = count_words(text)
    line_count = max(1, (char_count - 1) // CHARS_PER_LINE + 1)
    
    # Base duration on character count
    base_duration = char_count / READING_SPEED
    
    # Add time for processing line breaks
    line_break_time = 0.3 * (line_count - 1)
    
    # Add time for processing word count
    word_processing_time = 0.05 * word_count
    
    # Calculate total duration
    total_duration = base_duration + line_break_time + word_processing_time
    
    # Ensure duration is within limits
    return max(MIN_DURATION, min(total_duration, MAX_DURATION))

def split_long_lines(text):
    words = text.split()
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) + (1 if current_line else 0) <= CHARS_PER_LINE:
            current_line.append(word)
            current_length += len(word) + (1 if current_line else 0)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_length = len(word)

    if current_line:
        lines.append(' '.join(current_line))

    return '\n'.join(lines)

def convert_to_srt(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as csv_file, open(output_file, 'w', encoding='utf-8') as srt_file:
        csv_reader = csv.reader(csv_file)
        subtitle_number = 1
        subtitles = list(csv_reader)
        
        for i, row in enumerate(subtitles):
            if len(row) >= 2:
                start_time = row[0].strip()
                text = row[1].strip()

                if start_time and text:
                    start_seconds = time_to_seconds(start_time)
                    estimated_duration = estimate_subtitle_duration(text)
                    
                    if i < len(subtitles) - 1:
                        next_start_time = subtitles[i + 1][0].strip()
                        next_start_seconds = time_to_seconds(next_start_time)
                        end_seconds = min(start_seconds + estimated_duration, next_start_seconds - 0.1)
                    else:
                        end_seconds = start_seconds + estimated_duration
                    
                    start_time_srt = seconds_to_time(start_seconds)
                    end_time_srt = seconds_to_time(end_seconds)
                    
                    formatted_text = split_long_lines(text)
                    
                    srt_file.write(f"{subtitle_number}\n")
                    srt_file.write(f"{start_time_srt} --> {end_time_srt}\n")
                    srt_file.write(f"{formatted_text}\n\n")
                    subtitle_number += 1

def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    return file_path

def get_parameters():
    root = tk.Tk()
    root.withdraw()

    params = {}
    params['FRAME_RATE'] = simpledialog.askfloat("Input", "Enter frame rate (default 25):", initialvalue=FRAME_RATE)
    params['MIN_DURATION'] = simpledialog.askfloat("Input", "Enter minimum subtitle duration in seconds (default 1.0):", initialvalue=MIN_DURATION)
    params['MAX_DURATION'] = simpledialog.askfloat("Input", "Enter maximum subtitle duration in seconds (default 7.0):", initialvalue=MAX_DURATION)
    params['CHARS_PER_LINE'] = simpledialog.askinteger("Input", "Enter maximum characters per line (default 42):", initialvalue=CHARS_PER_LINE)
    params['READING_SPEED'] = simpledialog.askinteger("Input", "Enter reading speed in characters per second (default 20):", initialvalue=READING_SPEED)

    return params

def main():
    input_file = select_file()
    if not input_file:
        messagebox.showinfo("Information", "No file selected. Exiting.")
        return

    params = get_parameters()
    
    global FRAME_RATE, MIN_DURATION, MAX_DURATION, CHARS_PER_LINE, READING_SPEED
    FRAME_RATE = params['FRAME_RATE'] or FRAME_RATE
    MIN_DURATION = params['MIN_DURATION'] or MIN_DURATION
    MAX_DURATION = params['MAX_DURATION'] or MAX_DURATION
    CHARS_PER_LINE = params['CHARS_PER_LINE'] or CHARS_PER_LINE
    READING_SPEED = params['READING_SPEED'] or READING_SPEED

    output_folder = os.path.join(os.path.dirname(input_file), "converted")
    os.makedirs(output_folder, exist_ok=True)

    output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(input_file))[0] + ".srt")

    convert_to_srt(input_file, output_file)
    messagebox.showinfo("Success", f"Conversion complete. SRT file saved as:\n{output_file}")

if __name__ == "__main__":
    main()
