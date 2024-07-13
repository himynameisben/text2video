import tkinter as tk
import configparser
from settings_ui import create_settings_frame
from subclip_ui import create_subclip_frame
from main_ui import create_main_frame
from utils import load_settings

CONFIG_FILE = "settings.ini"

# Check if the config file exists
config = configparser.ConfigParser()
config.read(CONFIG_FILE)

# Create Tkinter window
root = tk.Tk()
root.title("Audio to SRT Converter, TTS Generator, and Subtitle Video Creator")

# Frames
main_frame = create_main_frame(root)
settings_frame, entry_api_key = create_settings_frame(root, main_frame)
subclip_frame = create_subclip_frame(root, main_frame)


def show_settings_page():
    main_frame.pack_forget()
    subclip_frame.pack_forget()
    settings_frame.pack(padx=10, pady=10, fill="both", expand="yes")
    load_settings(entry_api_key)


def show_main_page():
    settings_frame.pack_forget()
    subclip_frame.pack_forget()
    main_frame.pack(padx=10, pady=10, fill="both", expand="yes")


def show_subclip_page():
    main_frame.pack_forget()
    settings_frame.pack_forget()
    subclip_frame.pack(padx=10, pady=10, fill="both", expand="yes")


# Menu bar
menu_bar = tk.Menu(root)

# Home menu
home_menu = tk.Menu(menu_bar, tearoff=0)
home_menu.add_command(label="Home", command=show_main_page)
menu_bar.add_cascade(label="Home", menu=home_menu)

# Create Video menu
create_video_menu = tk.Menu(menu_bar, tearoff=0)
create_video_menu.add_command(label="Create Video", command=show_subclip_page)
menu_bar.add_cascade(label="Create Video", menu=create_video_menu)

# Settings menu
settings_menu = tk.Menu(menu_bar, tearoff=0)
settings_menu.add_command(label="Set OpenAI key", command=show_settings_page)
menu_bar.add_cascade(label="Settings", menu=settings_menu)

root.config(menu=menu_bar)

# Check config file
if config.has_option("Settings", "openai_key"):
    show_main_page()
else:
    show_settings_page()

# Start Tkinter main loop
root.mainloop()
