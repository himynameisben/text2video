import tkinter as tk
from tkinter import filedialog, messagebox
from utils import batch_generate_tts


def create_batch_tts_frame(root, main_frame):
    batch_tts_frame = tk.Frame(root)

    label_description = tk.Label(
        batch_tts_frame,
        text=(
            "Enter multiple lines of text below. To use a specific voice, prefix the text with the voice name followed by a colon.\n"
            "Allowed voices are: Alloy, Echo, Fable, Onyx, Nova, Shimmer. For example:"
        ),
        justify="left",
        wraplength=400,
    )
    label_description.pack(pady=10)

    example_text = (
        "Alloy: Hey, Nova! Did you hear about Goldman Sachs’ latest move into the digital asset space?\n"
        "Nova: Yeah, I did. It’s pretty exciting. They’re launching three new tokenization projects by the end of this year, right?"
    )

    label_text_input = tk.Label(batch_tts_frame, text="Enter multiple lines of text:")
    label_text_input.pack(pady=5)

    text_input = tk.Text(batch_tts_frame, height=20, width=50)
    text_input.insert(tk.END, example_text)  # Insert example text as default input
    text_input.pack(pady=5)

    label_folder_path = tk.Label(batch_tts_frame, text="No folder selected")
    label_folder_path.pack(pady=5)

    def select_folder():
        global tts_output_folder
        tts_output_folder = filedialog.askdirectory()
        if tts_output_folder:
            label_folder_path.config(text=f"Selected folder: {tts_output_folder}")

    button_select_folder = tk.Button(
        batch_tts_frame, text="Select Output Folder", command=select_folder
    )
    button_select_folder.pack(pady=10)

    # Response format options
    label_format = tk.Label(batch_tts_frame, text="Select response format:")
    label_format.pack(pady=5)

    format_options = ["aac", "mp3", "opus", "flac", "pcm"]
    selected_format = tk.StringVar(batch_tts_frame)
    selected_format.set(format_options[0])  # set default option

    format_menu = tk.OptionMenu(batch_tts_frame, selected_format, *format_options)
    format_menu.pack(pady=5)

    button_generate = tk.Button(
        batch_tts_frame,
        text="Generate Audio Files",
        command=lambda: batch_generate_tts(
            text_input.get("1.0", tk.END), tts_output_folder, selected_format.get()
        ),
    )
    button_generate.pack(pady=10)

    button_back_to_main = tk.Button(
        batch_tts_frame,
        text="Back to Main",
        command=lambda: (
            batch_tts_frame.pack_forget(),
            main_frame.pack(padx=10, pady=10, fill="both", expand="yes"),
        ),
    )
    button_back_to_main.pack(pady=10)

    return batch_tts_frame
