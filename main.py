import speech_recognition as sr
r = sr.Recognizer()
print('Coloque o nome do arquivo (.wav)')
path = input('')
path = 'audio/' + path + '.wav'
print(path)

with sr.AudioFile(path) as source:
    audio = r.record(source)

try:
    fala = r.recognize_google(audio,language='pt-BR')
    print("Fala:")
    print(fala)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
