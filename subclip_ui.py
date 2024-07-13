import tkinter as tk
from utils import select_file, select_srt_file, set_resolution, create_subtitled_video


def create_subclip_frame(root, main_frame):
    subclip_frame = tk.Frame(root)

    label_srt_file_path = tk.Label(subclip_frame, text="Select SRT file:")
    label_srt_file_path.pack(pady=5)

    entry_srt_path = tk.Entry(subclip_frame, width=50)
    entry_srt_path.pack(pady=5)

    button_browse_srt = tk.Button(
        subclip_frame, text="Browse", command=lambda: select_srt_file(entry_srt_path)
    )
    button_browse_srt.pack(pady=5)

    label_mp3_file_path = tk.Label(subclip_frame, text="Select MP3 file:")
    label_mp3_file_path.pack(pady=5)

    entry_mp3_path = tk.Entry(subclip_frame, width=50)
    entry_mp3_path.pack(pady=5)

    button_browse_mp3 = tk.Button(
        subclip_frame, text="Browse", command=lambda: select_file(entry_mp3_path)
    )
    button_browse_mp3.pack(pady=5)

    # Frame for resolution inputs and presets
    resolution_frame = tk.LabelFrame(
        subclip_frame, text="Resolution Settings", padx=10, pady=10
    )
    resolution_frame.pack(padx=10, pady=10, fill="both", expand="yes")

    # Preset buttons
    preset_frame = tk.Frame(resolution_frame)
    preset_frame.pack(pady=10)

    button_preset_1080p = tk.Button(
        preset_frame,
        text="1080p",
        command=lambda: set_resolution(
            entry_width, entry_height, entry_font_size, 1920, 1080, 96
        ),
    )
    button_preset_1080p.grid(row=0, column=0, padx=5, pady=5)

    button_preset_720p = tk.Button(
        preset_frame,
        text="720p",
        command=lambda: set_resolution(
            entry_width, entry_height, entry_font_size, 1280, 720, 64
        ),
    )
    button_preset_720p.grid(row=0, column=1, padx=5, pady=5)

    button_preset_640p = tk.Button(
        preset_frame,
        text="640p",
        command=lambda: set_resolution(
            entry_width, entry_height, entry_font_size, 640, 360, 42
        ),
    )
    button_preset_640p.grid(row=0, column=2, padx=5, pady=5)

    # Width input
    label_width = tk.Label(resolution_frame, text="Enter video width:")
    label_width.pack(pady=5)

    entry_width = tk.Entry(resolution_frame, width=50)
    entry_width.insert(0, "1920")
    entry_width.pack(pady=5)

    # Height input
    label_height = tk.Label(resolution_frame, text="Enter video height:")
    label_height.pack(pady=5)

    entry_height = tk.Entry(resolution_frame, width=50)
    entry_height.insert(0, "1080")
    entry_height.pack(pady=5)

    # Font size input
    label_font_size = tk.Label(resolution_frame, text="Enter font size:")
    label_font_size.pack(pady=5)

    entry_font_size = tk.Entry(resolution_frame, width=50)
    entry_font_size.insert(0, "28")
    entry_font_size.pack(pady=5)

    button_create_video = tk.Button(
        subclip_frame,
        text="Create Video with Subtitles",
        command=lambda: create_subtitled_video(
            entry_srt_path, entry_mp3_path, entry_width, entry_height, entry_font_size
        ),
    )
    button_create_video.pack(pady=10)

    button_back_to_main = tk.Button(
        subclip_frame,
        text="Back to Main",
        command=lambda: (
            subclip_frame.pack_forget(),
            main_frame.pack(padx=10, pady=10, fill="both", expand="yes"),
        ),
    )
    button_back_to_main.pack(pady=10)

    return subclip_frame
