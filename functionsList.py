import os #뭐지 얘는
import openai #openAI에서 스카이넷을 데려옵니다..

import gtts #tts 파일을 생성합니다.
import playsound #tts을 읽으려고 들고 옴
import random

def aLine(temp):
    #openai.api_key는 openAI 사이트에서 가져다 쓰시면 됩니다. 제 거 그대로 쓰시면 고소 날릴 거에요.
    openai.api_key = "여기에 넣으시면 돼요"

    #얘는 대화체라는 거 헷갈리지 말라고 집어넣는 거에요
    start_sequence = "\\nAI:"
    restart_sequence = "\\nHuman: "

    #파일 입력으로 이니시에이팅을 걸 거에요
    f = open("test.txt", 'r')
    basic_rule = f.readline()

    #서브룰과 그것을 전부 합칠 때 쓸 무언가
    Rule_Add = []
    RuleC = ""

    #서브룰을 불러옵니다. 줄 수는 ruleCount에서 들고 올 거에요
    ruleCount = f.readline()
    for i in range(0,int(ruleCount)):
        Rule_Add.append(f.readline())
        RuleC = RuleC + Rule_Add[i]
    dialogue = f.readline()
    f.close()

    dialogue = dialogue + temp + start_sequence

    #본격적인 AI로 전굽기
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt = basic_rule + RuleC + dialogue,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    #리스폰스 들고 오기
    response_string = response['choices'][0]['text']
    response_string.replace('\n', '\\n')
    dialogue = dialogue + response_string + restart_sequence

    #리스폰스 텍스트인가 들고 와서 콘솔에 출력할 거에요
    f = open("test.txt", 'w')
    f.write(basic_rule)

    #나머지 정보들을 여기에 보관합니다.
    f.write(ruleCount)
    f.write(RuleC)
    f.write(dialogue)
    f.close()

    print("AI returns")
    return response_string#.replace('\\n', '\n')