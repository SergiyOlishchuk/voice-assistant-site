
from gtts import gTTS

def say(text: str, save_path: str):
    tts = gTTS(text, lang='uk', slow=False)
    tts.save(save_path)
    return True

