import os
import re
import configparser
from openai import OpenAI

# from dotenv import load_dotenv
# load_dotenv()

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# client = OpenAI(api_key=api_key)


# use singleton pattern to crete client
class OpenAIClientSingleton:
    _instance = None

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            config = configparser.ConfigParser()
            config.read("settings.ini")
            api_key = config.get(
                "Settings", "openai_key", fallback=os.getenv("OPENAI_API_KEY")
            )
            if api_key:
                cls._instance = OpenAI(api_key=api_key)
            else:
                raise ValueError("API key has not been set.")
        return cls._instance


def transcribe_audio_to_srt(audio_path):
    with open(audio_path, "rb") as audio:
        # audio_data = audio.read()

        # response = client.audio.transcriptions.create("whisper-1", audio_data)
        client = OpenAIClientSingleton.getInstance()
        response = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio,
            response_format="verbose_json",
            # timestamp_granularities=["word"]
        )
        print(response)
        # print(response.words)
        print(response.segments)

    def format_time(seconds):
        millis = int(seconds * 1000)
        hours = millis // 3600000
        minutes = (millis % 3600000) // 60000
        seconds = (millis % 60000) // 1000
        milliseconds = millis % 1000
        return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

    srt_content = ""
    for i, segment in enumerate(response.segments):
        start_time = segment["start"]
        end_time = segment["end"]
        text = segment["text"]
        srt_content += f"{i + 1}\n"
        srt_content += f"{format_time(start_time)} --> {format_time(end_time)}\n"
        srt_content += f"{text}\n\n"

    output_srt = os.path.splitext(audio_path)[0] + ".srt"
    with open(output_srt, "w", encoding="utf-8") as srt_file:
        srt_file.write(srt_content)

    return output_srt


def get_tts(text, output_folder):
    client = OpenAIClientSingleton.getInstance()
    response = client.audio.speech.create(
        model="tts-1",
        voice="onyx",
        input=text,
    )

    audio_data = response.content
    base_filename = re.sub(r"[^\w\s\u4e00-\u9fff]", "", text[:20]).replace(" ", "_")
    output_path = os.path.join(output_folder, base_filename + ".mp3")

    counter = 1
    while os.path.exists(output_path):
        output_path = os.path.join(output_folder, f"{base_filename}_{counter}.mp3")
        counter += 1

    with open(output_path, "wb") as audio_file:
        audio_file.write(audio_data)

    # write txt file
    txt_path = os.path.join(output_folder, base_filename + ".txt")
    with open(txt_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(text)

    return output_path
