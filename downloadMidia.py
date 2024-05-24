import subprocess
import os
from time import sleep

esc = ''
clear = lambda: os.system('cls')
try:
    from pytube import YouTube
except ImportError:
    print("Baixando Biblioteca...")
    subprocess.call("pip", "install", "pytube")
while True:    
    print('''
                        1 - Baixar video
                        2 - Baixar Musica
                        3 - sair 
                            ''')
    esc = int(input(">"))
    clear()

    match esc:

        case 1:
            while True:

                print('''
                        1 - Baixar video com o link do youtube
                        2 - Baixar do arquivo txt com os links 
                        3 - sair 
                            ''')
                esc = int(input("> "))
                try:
                    if esc == 1:
                        while True:
                            print("digite sair caso deseja voltar ao inicio!")
                            url = input("informe(cole) o URL do youtube: ")
                            if url == 'sair':
                                break
                            else:
                                yt = YouTube(url)
                                video = yt.streams.filter(only_audio=False).first()
                                downloaded_file = video.download()
                                base, ext = os.path.splitext(downloaded_file)
                                new_file = base + '.mp4'
                                os.rename(downloaded_file, new_file)
                                print(f"{" "*20}Baixado!")
                                sleep(2)
                                clear()
                                continue

                    elif esc == 2:
                        with open("links.txt", "r")as file:
                            for i in file:
                                url = i
                                yt = YouTube(url)
                                video = yt.streams.filter(only_audio=False).first()
                                downloaded_file = video.download()
                                base, ext = os.path.splitext(downloaded_file)

                                new_file = base + '.mp4'
                                if new_file == FileExistsError:
                                    new_file = base + '2.mp4'
                                os.rename(downloaded_file, new_file)

                                print(f"{" "*20}Baixado!")
                                sleep(2)
                                clear()
                                break
                    elif esc == 3:
                        print("Voltando ao inicio")
                        sleep(2)
                        clear()
                        break
                    else:
                        sleep(2)
                        clear()
                        print("Escolha invalida, tente novamente:")



                except ValueError:
                    print("Escolha invalida, tente novamente!")
                    continue

        case 2:
            while True:

                print('''
                        1 - Baixar audio com o link do youtube
                        2 - Baixar do arquivo txt com os links 
                        3 - sair 
                            ''')
                esc = int(input("> "))
                try:
                    if esc == 1:
                        while True:
                            print("digite sair caso deseja voltar ao inicio!")
                            url = input("informe(cole) o URL do youtube: ")
                            if url == 'sair':
                                break
                            else:
                                yt = YouTube(url)
                                video = yt.streams.filter(only_audio=True).first()
                                downloaded_file = video.download()
                                base, ext = os.path.splitext(downloaded_file)
                                new_file = base + '.mp3'
                                os.rename(downloaded_file, new_file)
                                print(f"{" "*20}Baixado!")
                                sleep(2)
                                clear()
                                continue

                    elif esc == 2:
                        with open("links.txt", "r")as file:
                            for i in file:
                                url = i
                                yt = YouTube(url)
                                video = yt.streams.filter(only_audio=True).first()
                                downloaded_file = video.download()
                                base, ext = os.path.splitext(downloaded_file)

                                new_file = base + '.mp3'
                                if new_file == FileExistsError:
                                    new_file = base + '2.mp3'
                                os.rename(downloaded_file, new_file)

                                print(f"{" "*20}Baixado!")
                                sleep(2)
                                clear()
                                break
                    elif esc == 3:
                        print("Voltando ao inicio")
                        sleep(2)
                        clear()
                        break
                    else:
                        sleep(2)
                        clear()
                        print("Escolha invalida, tente novamente:")


                except ValueError:
                    print("Escolha invalida, tente novamente!")
                    continue

        case 3:
            break

        case _:
            print("Opção invalida")

