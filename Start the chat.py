import os
#from pdb import Restart
#from this import d
import openai

#openai.api_key는 openAI 사이트에서 가져다 쓰시면 됩니다. 제 거 그대로 쓰시면 고소 날릴 거에요.
openai.api_key = "여기에 string 형식으로 넣어 버리면 됩니다."

#얘는 대화체라는 거 헷갈리지 말라고 집어넣는 거에요
start_sequence = "\\nAI:"
restart_sequence = "\\nHuman: "

#파일 입력으로 이니시에이팅을 걸 거에요
f = open("test.txt", 'r')
basic_rule = f.readline()
dialogue = f.readline()
f.close()

#이건 어색하지 말라고 넣는 거
print("Human: ")

while True:
    #temp에 키보드 입력 받아서 라인에 집어쳐넣을 거임
    temp = input()
    dialogue = dialogue + temp + start_sequence

    #입력받은 값을 라인에 꽃아버리기
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt = dialogue,
        #temperature=0.9,
        #max_tokens=150,
        #top_p=1,
        #frequency_penalty=0.0,
        #presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    #리스폰스 텍스트인가 뭔가 들고 오기
    response_string = response['choices'][0]['text']
    print("\nAI:\n" + response_string + "\n\nHuman: ")
    dialogue = dialogue + response_string + restart_sequence

    #대화한 걸 파일에 꽃아 넣기
    f = open("test.txt", 'w')
    f.write(basic_rule)
    f.write(dialogue)
    f.close()