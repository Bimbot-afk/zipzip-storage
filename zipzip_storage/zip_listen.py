import pyttsx3
import random

class zip_listen():
    def __init__(self, zip_text, file_name):
        self.engine = pyttsx3.init()

        voices = self.engine.getProperty('voices')     
        self.engine.setProperty('voice', voices[1].id) 

        zip_listen_path = file_name + ".aiff"

        blocks = [b.replace("\n", " ") for b in zip_text.split("|") if b.strip()]

        sample = random.sample(blocks, min(5,len(blocks)))

        text_say =  " ".join(sample).replace("zip", "zip ").replace("zap", "zap ").strip()

        self.engine.save_to_file(text_say, zip_listen_path)
        self.engine.runAndWait()
