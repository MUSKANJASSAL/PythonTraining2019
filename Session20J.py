import mpor win32com.client as wincl

def speech(text):
    service = wincl.Dispatch("SAPI.SpVoice")
    service.Speak(text)

speech("hello friends, today is my birthday, give me some gifts, like hug, a long hug, kiss, a long kiss")