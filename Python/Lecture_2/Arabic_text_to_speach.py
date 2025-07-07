from gtts import gTTS
import os

arabic_text = "هو فيه جييييييييييييه."

tts = gTTS(text=arabic_text, lang='ar')
tts.save("arabic_speech.mp3")

print("Done! Saved as arabic_speech.mp3")
os.system("mpg123 arabic_speech.mp3")

