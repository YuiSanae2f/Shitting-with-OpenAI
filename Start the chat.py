import os #뭐지 얘는
import openai #openAI에서 스카이넷을 데려옵니다.

import gtts #tts 파일을 생성합니다.
import playsound #tts을 읽으려고 들고 옴
import random

#openai.api_key는 openAI 사이트에서 가져다 쓰시면 됩니다. 제 거 그대로 쓰시면 고소 날릴 거에요.
openai.api_key = "여기다가 넣으시면 됩니다."

#얘는 대화체라는 거 헷갈리지 말라고 집어넣는 거에요
start_sequence = "\nAI: "
restart_sequence = "\nHuman: "

#규칙을 불러옵니다.
f = open("Rule.txt", 'r')
basic_rule = f.read()
f.close()

#지금까지 저장되어 있던 대화를 불러 옵니다.
f = open("Dialogue.txt", 'r')
dialogue = f.read()
f.close()

#이건 어색하지 말라고 넣는 거
print("Human: ")

while True:
    #temp에 키보드 입력 받아서 라인에 집어쳐넣을 거임
    temp = input()
    dialogue = dialogue + restart_sequence + "\n" + temp + start_sequence

    #입력받은 값을 라인에 꽃아버리기
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt = basic_rule + dialogue,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    #리스폰스 텍스트인가 들고 와서 콘솔에 출력할 거에요
    response_string = response['choices'][0]['text']
    print("\nAI:" + response_string + "\n\nHuman:")

    #들고 온 거 TTS로 만들기
    tts = gtts.gTTS(text=response_string, lang='en')
    fileRandom_TTS = "voice" + str(random.random()) + ".mp3" #난수를 하나 생성

    #그 이유는 퍼미션 오류가 나기 때문에(그냥 파일을 랜덤 이름으로 만들었다가 지우기로 함)
    tts.save(fileRandom_TTS)
    playsound.playsound(fileRandom_TTS,True)
    os.remove(fileRandom_TTS)

    #대화 로그에다가 AI가 한 말을 꽃아넣을 거에요.
    dialogue = dialogue + response_string + "\n"

    #대화한 걸 파일에 꽃아 넣기
    f = open("Dialogue.txt", 'w')
    f.write(dialogue)
    f.close()