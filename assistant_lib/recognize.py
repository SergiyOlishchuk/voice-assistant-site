import speech_recognition

def recognize(sample_path: str):
    
    sample = speech_recognition.WavFile(sample_path)
    
    recognizer = speech_recognition.Recognizer()
    
    with sample as audio:
        recognizer.adjust_for_ambient_noise(audio)
        content = recognizer.record(audio)
        
        return recognizer.recognize_google(content, language='uk-UK')
    
