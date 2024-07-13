import tkinter as tk
from utils import save_settings


def create_settings_frame(root, main_frame):
    settings_frame = tk.Frame(root)

    label_api_key = tk.Label(settings_frame, text="Enter OpenAI key:")
    label_api_key.pack(pady=5)

    entry_api_key = tk.Entry(settings_frame, width=50)
    entry_api_key.pack(pady=5)

    label_api_key_info = tk.Label(
        settings_frame,
        text="The key will only be stored on your computer.",
        font=("Arial", 8),
    )
    label_api_key_info.pack(pady=5)

    button_save_settings = tk.Button(
        settings_frame, text="Save", command=lambda: save_settings(entry_api_key)
    )
    button_save_settings.pack(pady=10)

    button_cancel_settings = tk.Button(
        settings_frame,
        text="Cancel",
        command=lambda: (
            settings_frame.pack_forget(),
            main_frame.pack(padx=10, pady=10, fill="both", expand="yes"),
        ),
    )
    button_cancel_settings.pack(pady=5)

    return settings_frame, entry_api_key
