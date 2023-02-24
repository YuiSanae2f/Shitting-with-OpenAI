import functionsList
import socket

import gtts #tts 파일을 생성합니다.
import playsound #tts을 읽으려고 들고 옴
import random
import os

def read_twitch_chat(username, oauth_token, channel):
    # Connect to Twitch IRC server
    s = socket.socket()
    s.connect(("irc.chat.twitch.tv", 6667))

    # Send authentication information
    s.send(f"PASS {oauth_token}\r\n".encode())
    s.send(f"NICK {username}\r\n".encode())

    # Join the specified channel
    s.send(f"JOIN #{channel}\r\n".encode())

    # Continuously receive messages from the chat and print them
    while True:
        response = s.recv(2048).decode()
        if response == "PING :tmi.twitch.tv\r\n":
            s.send("PONG :tmi.twitch.tv\r\n".encode())
        else:
            #print(response)
            response_string = functionsList.aLine(response,"",False)
            print("\nKodey: " + response_string)

            #들고 온 거 TTS로 만들기
            tts = gtts.gTTS(text=response_string, lang='en')
            fileRandom_TTS = "voice" + str(random.random()) + ".mp3" #난수를 하나 생성

            #그 이유는 퍼미션 오류가 나기 때문에(그냥 파일을 랜덤 이름으로 만들었다가 지우기로 함)
            tts.save(fileRandom_TTS)
            playsound.playsound(fileRandom_TTS,True)
            os.remove(fileRandom_TTS)

read_twitch_chat('Kodey_Beacon','oauth:뒤에 있는 거','yuisanae2f')