import speech_recognition as sr
from deepmultilingualpunctuation import PunctuationModel
#from transformers import pipeline
#ner = pipeline("ner", aggregation_strategy="simple", model="dbmdz/bert-large-cased-finetuned-conll03-english")  # Named Entity Recognition (NER)


def punct(text):
    m= PunctuationModel()
    result = m.restore_punctuation(text)
    return result

def speech_recog():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak Anything : ")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return punct(text)
        except Exception as e:
            return e
