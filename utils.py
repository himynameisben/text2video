import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import configparser

from openai_func import transcribe_audio_to_srt, get_tts
from subclip import create_video_with_subtitles

CONFIG_FILE = "settings.ini"

# Check if the config file exists
config = configparser.ConfigParser()
config.read(CONFIG_FILE)

tts_output_folder = ""


def select_file(entry):
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)


def select_srt_file(entry):
    file_path = filedialog.askopenfilename(filetypes=[("SRT Files", "*.srt")])
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)


def select_folder(label_folder_path):
    global tts_output_folder
    tts_output_folder = filedialog.askdirectory()
    if tts_output_folder:
        label_folder_path.config(text=f"Selected folder: {tts_output_folder}")


def convert_audio(entry_file_path):
    audio_path = entry_file_path.get()
    if not audio_path:
        messagebox.showwarning("Warning", "Please select an audio file.")
        return

    try:
        srt_path = transcribe_audio_to_srt(audio_path)
        messagebox.showinfo(
            "Success", f"Transcription complete! SRT file saved at: {srt_path}"
        )
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


def generate_tts(text_input, label_folder_path):
    global tts_output_folder
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Please enter some text.")
        return
    if not tts_output_folder:
        messagebox.showwarning("Warning", "Please select an output folder.")
        return

    try:
        audio_path = get_tts(text, tts_output_folder)
        messagebox.showinfo(
            "Success", f"TTS generation complete! MP3 file saved at: {audio_path}"
        )
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


def create_subtitled_video(
    entry_srt_path, entry_mp3_path, entry_width, entry_height, entry_font_size
):
    srt_path = entry_srt_path.get()
    mp3_path = entry_mp3_path.get()

    width = int(entry_width.get())
    height = int(entry_height.get())
    font_size = int(entry_font_size.get())

    if not srt_path or not mp3_path:
        messagebox.showwarning("Warning", "Please select both SRT and MP3 files.")
        return

    output_path = os.path.splitext(mp3_path)[0] + ".mp4"

    try:
        create_video_with_subtitles(
            srt_path, mp3_path, output_path, width, height, font_size
        )
        messagebox.showinfo(
            "Success", f"Video creation complete! MP4 file saved at: {output_path}"
        )
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


def save_settings(entry_api_key):
    api_key = entry_api_key.get()
    if not config.has_section("Settings"):
        config.add_section("Settings")
    config.set("Settings", "openai_key", api_key)
    with open(CONFIG_FILE, "w") as configfile:
        config.write(configfile)
    messagebox.showinfo("Success", "OpenAI key saved!")


def load_settings(entry_api_key):
    if config.has_option("Settings", "openai_key"):
        entry_api_key.insert(0, config.get("Settings", "openai_key"))


def set_resolution(
    entry_width, entry_height, entry_font_size, width, height, font_size
):
    entry_width.delete(0, tk.END)
    entry_width.insert(0, width)
    entry_height.delete(0, tk.END)
    entry_height.insert(0, height)
    entry_font_size.delete(0, tk.END)
    entry_font_size.insert(0, font_size)
