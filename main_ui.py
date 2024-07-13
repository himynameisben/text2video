import tkinter as tk
from utils import select_folder, generate_tts, convert_audio, select_file


def create_main_frame(root):
    main_frame = tk.Frame(root)

    # TTS section
    tts_frame = tk.LabelFrame(main_frame, text="Text to Speech (TTS)", padx=10, pady=10)
    tts_frame.pack(padx=10, pady=10, fill="both", expand="yes")

    # Select folder
    button_select_folder = tk.Button(
        tts_frame,
        text="Select TTS Output Folder",
        command=lambda: select_folder(label_folder_path),
    )
    button_select_folder.pack(pady=10)

    label_folder_path = tk.Label(tts_frame, text="No folder selected")
    label_folder_path.pack(pady=5)

    # Text input
    label_text_input = tk.Label(tts_frame, text="Enter text for TTS:")
    label_text_input.pack(pady=5)

    text_input = tk.Text(tts_frame, height=10, width=50)
    text_input.pack(pady=5)

    # Generate TTS button
    button_tts = tk.Button(
        tts_frame,
        text="Generate TTS",
        command=lambda: generate_tts(text_input, label_folder_path),
    )
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

    button_browse = tk.Button(
        frame, text="Browse", command=lambda: select_file(entry_file_path)
    )
    button_browse.grid(row=0, column=2, padx=5, pady=5)

    # Convert button
    button_convert = tk.Button(
        srt_frame, text="Convert to SRT", command=lambda: convert_audio(entry_file_path)
    )
    button_convert.pack(pady=10)

    return main_frame
