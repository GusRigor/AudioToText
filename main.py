import speech_recognition as sr

print('Início')
r = sr.Recognizer()
print('Coloque o nome do arquivo (.wav)')
arquivo = input('')
path = 'audio/' + arquivo + '.wav'
print(path)
print('pegou o arquivo')

with sr.AudioFile(path) as source:
    audio = r.record(source)
print('leu o arquivo')


try:
    fala = r.recognize_google(audio,language='pt-BR')
    print("Fala:")
    print(fala)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

print('Gravando o arquivo em texto')    

text_file = open("texto/" + arquivo + ".txt", "w")
n = text_file.write(fala)
text_file.close()

print('Arquivo gravado')
print('Fim!')