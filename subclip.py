# import os
# os.environ["IMAGEMAGICK_BINARY"] = "/usr/bin/convert"  # or "/usr/bin/magick" based on your ImageMagick version

from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
from pysrt import open as open_srt


# Read the SRT file and parse subtitles
def parse_subtitles(srt_file):
    subs = open_srt(srt_file)
    return [
        ((sub.start.ordinal / 1000, sub.end.ordinal / 1000), sub.text) for sub in subs
    ]


# Generate subtitle clip
def make_subtitle_clip(subs, font_size, video_width):
    def generator(txt):
        # return TextClip(txt, font='Arial', fontsize=24, color='white')
        return TextClip(
            txt,
            font="Arial",
            fontsize=font_size,
            color="white",
            size=(video_width, None),
            method="caption",
            align="center",
        )

    return SubtitlesClip(subs, generator)


# Main function
def create_video_with_subtitles(
    srt_file, mp3_file, output_file, width, height, font_size
):
    # Parse subtitles
    subs = parse_subtitles(srt_file)
    print(subs)

    # Generate subtitle clip
    subtitle_clip = make_subtitle_clip(subs, font_size, width)

    # Read the MP3 file
    audio_clip = AudioFileClip(mp3_file)

    # Generate a video clip with black background, same length as the audio file
    video_clip = ColorClip(
        size=(width, height), color=(0, 0, 0), duration=audio_clip.duration
    )

    # Set the audio file as the background audio of the video
    video_clip = video_clip.set_audio(audio_clip)

    # Overlay subtitles on the video
    # final_clip = CompositeVideoClip([video_clip, subtitle_clip.set_pos(('center', 'bottom'))])
    final_clip = CompositeVideoClip(
        [video_clip, subtitle_clip.set_pos(("center", "center"))]
    )

    # Output the video
    final_clip.write_videofile(output_file, fps=24)


if __name__ == "__main__":
    # Example usage
    create_video_with_subtitles(
        "sample/ok_google.srt", "sample/ok_google.mp3", "sample/ok_google.mp4"
    )
