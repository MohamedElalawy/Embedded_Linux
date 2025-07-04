from gtts import gTTS
import os

arabic_text = "أجدع علوي على الكوكب."

tts = gTTS(text=arabic_text, lang='ar')
tts.save("arabic_speech.mp3")

print("Done! Saved as arabic_speech.mp3")

# Play the audio (Linux example using 'mpg123')
os.system("mpg123 arabic_speech.mp3")

