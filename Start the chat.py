import os
#from pdb import Restart
#from this import d
import openai

#openai.api_key�� openAI ����Ʈ���� ������ ���ø� �˴ϴ�. �� �� �״�� ���ø� ��� ���� �ſ���.
openai.api_key = "���⿡ string �������� �־� ������ �˴ϴ�."

#��� ��ȭü��� �� �򰥸��� ����� ����ִ� �ſ���
start_sequence = "\\nAI:"
restart_sequence = "\\nHuman: "

#���� �Է����� �̴Ͻÿ������� �� �ſ���
f = open("test.txt", 'r')
basic_rule = f.readline()
dialogue = f.readline()
f.close()

#�̰� ������� ����� �ִ� ��
print("Human: ")

while True:
    #temp�� Ű���� �Է� �޾Ƽ� ���ο� �����ĳ��� ����
    temp = input()
    dialogue = dialogue + temp + start_sequence

    #�Է¹��� ���� ���ο� �ɾƹ�����
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

    #�������� �ؽ�Ʈ�ΰ� ���� ��� ����
    response_string = response['choices'][0]['text']
    print("\nAI:\n" + response_string + "\n\nHuman: ")
    dialogue = dialogue + response_string + restart_sequence

    #��ȭ�� �� ���Ͽ� �ɾ� �ֱ�
    f = open("test.txt", 'w')
    f.write(basic_rule)
    f.write(dialogue)
    f.close()