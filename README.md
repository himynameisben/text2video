# text2video

text2video is a tool that enables you to generate text-to-speech (TTS) audio, convert audio files into SRT subtitles, and create videos with embedded subtitles. It leverages the power of OpenAI's API for transcription and TTS functionalities.

## Features

- **Text-to-Speech (TTS) Generation**: Converts text into speech and saves it as an MP3 file.
- **Audio to SRT Conversion**: Converts audio files (MP3) into SRT subtitle files.
- **Create Video with Subtitles**: Combines an MP3 file and an SRT file to create a video with embedded subtitles.

## Installation

1. Clone the repository:

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Ensure you have [ImageMagick](https://imagemagick.org/) installed on your system, as it is required by `moviepy` for subtitle rendering.

## Usage

### Running the GUI

To start the GUI, run:

```bash
python tkgui.py
```



## Configuration

Before using the transcription and TTS features, you need to set your OpenAI API key. This can be done through the Settings page in the GUI.

## Troubleshooting

Here's a step-by-step guide to troubleshoot the ImageMagick error and modify the policy settings:

### Step-by-Step Guide to Modify ImageMagick Policy Settings

1. **Identify the Error**:
   If you encounter the error message indicating issues with ImageMagick not being installed or the path not being specified correctly, you need to adjust the policy settings.
   > This error can be due to the fact that ImageMagick is not installed on your computer, or (for Windows users) that you didn't specify the path to the ImageMagick binary in the file conf.py, or that the path you specified is incorrect.

2. **Open the Policy File**:
   Use a text editor with superuser permissions to open the ImageMagick policy file. You can use `vim` or any other text editor you prefer.

   ```bash
   sudo vim /etc/ImageMagick-6/policy.xml
   ```

3. **Modify the Policy File**:
   Locate the lines in the policy file that restrict read and write permissions. You will need to comment out the restrictive line and add permissions that suit your needs.

   ```xml
   <!-- in order to avoid to get image with password text -->
   <!-- comment this line -->
   <!-- <policy domain="path" rights="none" pattern="@*"/> -->

   <!-- let ImageMagick read/write all files -->
   <policy domain="path" rights="read|write" pattern="@*"/>
   <!-- or specify your project absolute path -->
   <policy domain="path" rights="read|write" pattern="/your_project_path*"/>
   ```

   - **Comment Out Restrictive Line**: This line is originally set to deny any read/write access. By commenting it out, you prevent this restriction from applying.
   - **Grant Read/Write Permissions**: Add a line that grants read and write permissions to all files or specify the exact path of your project.

4. **Save and Exit**:
   Save the changes and exit the text editor. In `vim`, you can do this by pressing `Esc`, typing `:wq`, and pressing `Enter`.

5. **Verify Changes**:
   Ensure that the changes are correctly saved and the file permissions are updated. You can reopen the file to verify.

6. **Test ImageMagick**:
   Run your project or the specific command that was failing to see if the issue is resolved.

### Summary
- Open `/etc/ImageMagick-6/policy.xml` with superuser permissions.
- Comment out the restrictive policy line.
- Add a policy line that grants read/write permissions to all files or to your specific project path.
- Save the changes and verify.
- Test to ensure the issue is resolved.

By following these steps, you should be able to resolve the ImageMagick error related to read and write permissions.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

- [OpenAI](https://openai.com/) for the transcription and TTS APIs.
- [moviepy](https://zulko.github.io/moviepy/) for video editing capabilities.
- [pysrt](https://github.com/byroot/pysrt) for SRT file handling.

