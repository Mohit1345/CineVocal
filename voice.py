from elevenlabs import set_api_key
import os 
from dotenv import load_dotenv
load_dotenv()
set_api_key(os.environ['elevenlabs_api'])

import requests

CHUNK_SIZE = 1024


headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": os.environ['elevenlabs_api']
}
def voiceover(script,title,Genre):
    if "Horror" or "Suspence" in Genre:
        url = "https://api.elevenlabs.io/v1/text-to-speech/piTKgcLEGmPE4e6mEKli"
    else:
        url = "https://api.elevenlabs.io/v1/text-to-speech/TxGEqnHWrfWFTfGW9XjX"

    data = {
    "text": script,
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.5
    }
    }

    response = requests.post(url, json=data, headers=headers)
    with open(f'audio_generated\{title}.mp3', 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)

