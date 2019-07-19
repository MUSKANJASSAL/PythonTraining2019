from gtts import gTTS
tts = gTTS('This is an awesome day', lang='en')
tts.save('hello.mp3')
print(">> File Created")
