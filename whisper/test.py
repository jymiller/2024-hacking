from openai import OpenAI

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key='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',
)
from docx import Document

def transcribe_audio():
    with open('audio1720145364.m4a', 'rb') as audio_file:
        transcription = client.audio.transcriptions.create("whisper-1", audio_file)
    return transcription['text']