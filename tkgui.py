import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import configparser

from openai_func import transcribe_audio_to_srt, get_tts
from subclip import create_video_with_subtitles  # Import create_video_with_subtitles function from subclip

CONFIG_FILE = 'settings.ini'

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

def select_folder():
    global tts_output_folder
    tts_output_folder = filedialog.askdirectory()
    if tts_output_folder:
        label_folder_path.config(text=f"Selected folder: {tts_output_folder}")

def convert_audio():
    audio_path = entry_file_path.get()
    if not audio_path:
        messagebox.showwarning("Warning", "Please select an audio file.")
        return

    try:
        srt_path = transcribe_audio_to_srt(audio_path)
        messagebox.showinfo("Success", f"Transcription complete! SRT file saved at: {srt_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def generate_tts():
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
        messagebox.showinfo("Success", f"TTS generation complete! MP3 file saved at: {audio_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def create_subtitled_video():
    srt_path = entry_srt_path.get()
    mp3_path = entry_mp3_path.get()
    if not srt_path or not mp3_path:
        messagebox.showwarning("Warning", "Please select both SRT and MP3 files.")
        return
    
    output_path = os.path.splitext(mp3_path)[0] + ".mp4"
    
    try:
        create_video_with_subtitles(srt_path, mp3_path, output_path)
        messagebox.showinfo("Success", f"Video creation complete! MP4 file saved at: {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def save_settings():
    api_key = entry_api_key.get()
    if not config.has_section('Settings'):
        config.add_section('Settings')
    config.set('Settings', 'openai_key', api_key)
    with open(CONFIG_FILE, 'w') as configfile:
        config.write(configfile)
    messagebox.showinfo("Success", "OpenAI key saved!")
    show_main_page()

def load_settings():
    if config.has_option('Settings', 'openai_key'):
        entry_api_key.insert(0, config.get('Settings', 'openai_key'))

def show_settings_page():
    main_frame.pack_forget()
    subclip_frame.pack_forget()
    settings_frame.pack(padx=10, pady=10, fill="both", expand="yes")
    load_settings()

def show_main_page():
    settings_frame.pack_forget()
    subclip_frame.pack_forget()
    main_frame.pack(padx=10, pady=10, fill="both", expand="yes")

def show_subclip_page():
    main_frame.pack_forget()
    subclip_frame.pack(padx=10, pady=10, fill="both", expand="yes")

def cancel_settings():
    show_main_page()

# Create Tkinter window
root = tk.Tk()
root.title("Audio to SRT Converter, TTS Generator, and Subtitle Video Creator")

# Settings page
settings_frame = tk.Frame(root)
label_api_key = tk.Label(settings_frame, text="Enter OpenAI key:")
label_api_key.pack(pady=5)

entry_api_key = tk.Entry(settings_frame, width=50)
entry_api_key.pack(pady=5)

label_api_key_info = tk.Label(settings_frame, text="The key will only be stored on your computer.", font=("Arial", 8))
label_api_key_info.pack(pady=5)

button_save_settings = tk.Button(settings_frame, text="Save", command=save_settings)
button_save_settings.pack(pady=10)

button_cancel_settings = tk.Button(settings_frame, text="Cancel", command=cancel_settings)
button_cancel_settings.pack(pady=5)

# Main page
main_frame = tk.Frame(root)

# TTS section
tts_frame = tk.LabelFrame(main_frame, text="Text to Speech (TTS)", padx=10, pady=10)
tts_frame.pack(padx=10, pady=10, fill="both", expand="yes")

# Select folder
button_select_folder = tk.Button(tts_frame, text="Select TTS Output Folder", command=select_folder)
button_select_folder.pack(pady=10)

label_folder_path = tk.Label(tts_frame, text="No folder selected")
label_folder_path.pack(pady=5)

# Text input
label_text_input = tk.Label(tts_frame, text="Enter text for TTS:")
label_text_input.pack(pady=5)

text_input = tk.Text(tts_frame, height=10, width=50)
text_input.pack(pady=5)

# Generate TTS button
button_tts = tk.Button(tts_frame, text="Generate TTS", command=generate_tts)
button_tts.pack(pady=10)

# Separator
separator = tk.Frame(main_frame, height=2, bd=1, relief=tk.SUNKEN)
separator.pack(fill=tk.X, padx=5, pady=10)

# SRT section
srt_frame = tk.LabelFrame(main_frame, text="Audio to SRT", padx=10, pady=10)
srt_frame.pack(padx=10, pady=10, fill="both", expand="yes")

# File selection
frame = tk.Frame(srt_frame)
frame.pack(pady=10)

label_file_path = tk.Label(frame, text="Select MP3 file:")
label_file_path.grid(row=0, column=0, padx=5, pady=5)

entry_file_path = tk.Entry(frame, width=50)
entry_file_path.grid(row=0, column=1, padx=5, pady=5)

button_browse = tk.Button(frame, text="Browse", command=lambda: select_file(entry_file_path))
button_browse.grid(row=0, column=2, padx=5, pady=5)

# Convert button
button_convert = tk.Button(srt_frame, text="Convert to SRT", command=convert_audio)
button_convert.pack(pady=10)

# Subclip page
subclip_frame = tk.Frame(root)

label_srt_file_path = tk.Label(subclip_frame, text="Select SRT file:")
label_srt_file_path.pack(pady=5)

entry_srt_path = tk.Entry(subclip_frame, width=50)
entry_srt_path.pack(pady=5)

button_browse_srt = tk.Button(subclip_frame, text="Browse", command=lambda: select_srt_file(entry_srt_path))
button_browse_srt.pack(pady=5)

label_mp3_file_path = tk.Label(subclip_frame, text="Select MP3 file:")
label_mp3_file_path.pack(pady=5)

entry_mp3_path = tk.Entry(subclip_frame, width=50)
entry_mp3_path.pack(pady=5)

button_browse_mp3 = tk.Button(subclip_frame, text="Browse", command=lambda: select_file(entry_mp3_path))
button_browse_mp3.pack(pady=5)

button_create_video = tk.Button(subclip_frame, text="Create Video with Subtitles", command=create_subtitled_video)
button_create_video.pack(pady=10)

button_back_to_main = tk.Button(subclip_frame, text="Back to Main", command=show_main_page)
button_back_to_main.pack(pady=10)

# Menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
menu_bar.add_command(label="Home", command=show_main_page)
menu_bar.add_command(label="Create Video", command=show_subclip_page)
settings_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Setting", menu=settings_menu)
settings_menu.add_command(label="Set OpenAI key", command=show_settings_page)

# Check config file
if config.has_option('Settings', 'openai_key'):
    show_main_page()
else:
    show_settings_page()

# Start Tkinter main loop
root.mainloop()
