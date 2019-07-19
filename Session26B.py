# from gtts import gTTS
# tts_en = gTTS('hello', lang='en')
# tts_fr = gTTS('bonjour', lang='fr')
#
# with open('hello_bonjour.mp3', 'wb') as f:
#     tts_en.write_to_fp(f)
#     tts_fr.write_to_fp(f)
#  print(">> Done")


print("=====Playing sound directly=====")

from gtts import gTTS
from io import BytesIO
mp3_fp = BytesIO()
tts = gTTS('hello', 'en')
tts.write_to_fp(mp3_fp)
print(">> Done")
# Load `mp3_fp` as an mp3 file in
# the audio library of your choice
