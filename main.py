from speech import speech_recog
from text_summary import generate_summary

print("starting")

text = speech_recog()
print(text)

with open('testing_text.txt','w') as f:
    f.write(text)
summary = generate_summary("testing_text.txt", 2)
print(summary)