# Importando as bibliotecas.
import gtts
from playsound import playsound

with open('frase.txt', 'r') as arquivo:  # r = ler
    for linha in arquivo:  # ler a 1° linha do arquivo.
        frase = gtts.gTTS(linha, lang='pt-br')
        frase.save('frase.mp3')  # transformando um arquivo de texto em áudio
        playsound('frase.mp3')  # executando o áudio
