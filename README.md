# Shitting with OpenAI  
인간 시대의 끝이 도래했습니다.  
이제는 사람과 말을 못 해 x된 히키코모리를 상대하는 인간은 더 이상 필요 없습니다.  
사람과 말을 못 하는 것이라면 기계와 말을 시켜 보도록 하겠습니다.

---

## < OpenAI >
OpenAI라는 회사가 거대한 떡밥을 뿌렸습니다.  
"사람 말을 알아먹는 거대한 AI 덩어리를 개인이 무료로 이용해 보세요!"  
이 기계는 말을 알아먹으며,  
거대한 지식을 가지고 있고,  
당신은 이 기계를 심지어 파이썬에서도 무료로 활용할 수 있습니다.  
OpenAI의 놀이터에 들어가 보면 "View Code"라는 친구를 볼 수 있을 텐데  
당신이 누구에게나 공짜로 뿌리고 있는 API키를 가지고만 있다면  
파이썬을 비롯한 다양한 환경에서 ChatGPT 비스무리한 것을 활용할 수 있게 해 줄 것입니다.  

---

## < ChatGPT >
기본적으로 OpenAI에서 제공하는 이 친구는 길다란 글을 읽고 상황에 맞추어 대답을 해 줄 수 있는 단발성 대답 생성기입니다.  
말인즉슨 기억력이 꽝인데다 정체성조차 존재하지 않습니다.  
그렇기 때문에 차선책으로 지금까지 했던 대화들은 물론, 정체성마저 박아 줄 필요가 있습니다.  

---

## < 파일 입출력 >
정보 시간에 파이썬을 배우신 분들이라면 파일 입출력이라는 게 얼마나 간편한 건지 알고 계실 겁니다.  
네 뭐 평소대로 대화 로그 따로 두고 정체성 따로 두고 그러시면 됩니다.  

```python
#규칙을 불러옵니다.
f = open("Rule.txt", 'r')
basic_rule = f.read()
f.close()

#지금까지 저장되어 있던 대화를 불러 옵니다.
f = open("Dialogue.txt", 'r')
dialogue = f.read()
f.close()
```

---

## < 챗봇 쳐만들기 >
파일 입출력을 이용하여 기본적인 룰과 대화 저장소를 만드셨다면
그걸 전부 때려박고 키보드 입력을 함께 받아서 prompt에 넣으시면 됩니다.

```python
#키보드 입력을 받아서 dialogue에 추가합니다.
dialogue = dialogue + restart_sequence + "\n" + content + start_sequence

#OpenAI를 작동시킵니다.
response = openai.Completion.create(
    model="text-davinci-003",
    prompt = basic_rule + subRule + dialogue, #prompt에 입력값을 집어넣습니다.
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
)
```

이제 파일 입력으로 했던 소리를 다시 파일 안에 집어넣습니다.  
While문만 돌리면 챗봇은 완성이네요.  

```python
#response_string이 ChatGPT가 하는 대답이다.
response_string = response['choices'][0]['text']
dialogue = dialogue + response_string + "\n"


#대화한 걸 파일에 꽃아 넣기
f = open("Dialogue.txt", 'w')
f.write(dialogue)
f.close()
```

---

## < 디스코드 봇 >
제 나와바리는 디스코드입니다.  
어차피 저기 있는 친구를 함수로 만들어서 돌리기만 하면 상관없으니  
디스코드 봇 뿌리만 가져와서 함수 돌리는 거만 하죠.  
작동은 잘 하는 거 같네요.  

코드는 ChatGPT의 도움을 많이 받았습니다.
```python
DiscordBot.py
```
를 참고하시면 되고요,

제가 수정한 부분은 이곳입니다.
```python
#GPT in Python에서 만든 함수를 불러온다.(나의 경우에는 function)
import functionsList

@app.event
#디스코드에서 이 봇이 볼 수 있는 범위에 누가 메세지를 입력했을 경우
async def on_message(message):
    #그것의 출처가 자신인 경우
    if message.author.bot:
        #중단
        return
    
    #메세지의 내용을 받아 그걸 앞에서 가져온 함수에 집어넣는다.
    stringTemp = message.content
    print("discord bot returns:\n" + stringTemp)
    await message.channel.send(functionsList.aLine(stringTemp, ""))
    return
```

---

## < 트위치 >
마이크도 못 켜고 챗마저 못 보는 멍청이인 저 대신에  
존나 똑똑한 이 ChatGPT에게 트위치 방송을 시켜 보도록 하겠습니다.  
하지만 이 ChatGPT만으로는 챗을 읽기가 어려울 것 같고요.  

---

## < 트위치 봇 >
트위치에도 봇이 있습니다.  
Nightbot이라던가 빵떡이라던가 여러 가지 있고요.  
그런 친구를 파이썬에서 쓰는 방법을 알려준답시고  
TwitchAPI라고 존재합니다.  
일단 챗을 받아오는 걸 하나 들고 와 보죠.  

```python
response = s.recv(2048).decode()
```

이 망할 response를 그냥 입력값으로 넣어 주면 openAI가 알아서 대답을 해 줄 겁니다.  
하지만 목소리가 없으면 실감이 안 나니 TTS라도 입혀 줍시다.  

---

## < gTTS >
평범한 gTTS를 이용해서 목소리나 넣어 줍시다.
이상하게 같은 파일에다가 tts를 넣었다 뺐다 하니까 오류가 나는 관계로
난수를 만들어서 파일 이름을 아예 랜덤으로 만들어 버립시다.
```python
#들고 온 거 TTS로 만들기
tts = gtts.gTTS(text=response_string, lang='en')
fileRandom_TTS = "voice" + str(random.random()) + ".mp3" #난수를 하나 생성

#그 이유는 퍼미션 오류가 나기 때문에(그냥 파일을 랜덤 이름으로 만들었다가 지우기로 함)
tts.save(fileRandom_TTS)
playsound.playsound(fileRandom_TTS,True)
os.remove(fileRandom_TTS)
```

---

## < 아무튼 >
아무튼 OpenAI라는 개쩌는 인공지능이 나왔고요,  
저 같은 일반인마저 혜택을 받을 수 있게 되었습니다.  
인간시대의 끝이 온다면 우리가 더 꿀 빨 수 있을 거 같고요.
