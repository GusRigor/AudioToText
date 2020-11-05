import speech_recognition as sr

def ler_arquivo():
    r = sr.Recognizer()
    print('Coloque o nome do arquivo (.wav)')
    arquivo = input('')
    path = 'audio/' + arquivo + '.wav'
    print(path)
    return {'r':r, 'arquivo':arquivo, 'path':path}

def gravar_audio(path, r):
    with sr.AudioFile(path) as source:
        audio = r.record(source)
    return audio

def converter_audio(r, audio):
    try:
        fala = r.recognize_google(audio,language='pt-BR')
        print("Fala:")
        print(fala)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return fala

def salvar_texto(arquivo, fala):
    text_file = open("texto/" + arquivo + ".txt", "w")
    n = text_file.write(fala)
    text_file.close()

def main():
    Arquivo = ler_arquivo()
    print('pegou o arquivo')
    Audio = gravar_audio(Arquivo['path'], Arquivo['r'])
    print('leu o arquivo')
    print('Convertendo o Arquivo...')
    Fala = converter_audio(Arquivo['r'], Audio)
    print('Gravando o arquivo em texto')    
    salvar_texto(Arquivo['arquivo'], Fala)
    print('Arquivo gravado')

print('Início')
rodar_novamente = 'S'
while rodar_novamente == 'S':
    main()
    print('Digite S para rodar novamente')
    rodar_novamente = input('')

print('Fim!')