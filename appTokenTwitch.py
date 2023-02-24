import requests

#이건 Twitch Developers에서 확인할 수 있습니다.
#응용 프로그램을 하나 추가해서 클라이언트 ID와 클라이언트PW를 가져올 수 있죠.
clientID = 'ID'
clientPW = 'PW'

#위의 변수에 값을 제대로 집어넣었다면 이 친구에게서 access_token을 가져올 수 있습니다.
#아닐 경우 오류를 반환해 줄 겁니다.
#req = requests.post(f'https://id.twitch.tv/oauth2/token?client_id={clientID}&client_secret={clientPW}&grant_type=client_credentials')
#print("req.text: "+req.text)

#app_token에 access_token을 집어넣읍시다. 처음에 실행할 경우에 이 밑은 전부 주석처리하고 실행합시다.
app_token = '앱토큰'

#app_token에 문제가 없을 시에 토큰 관련한 정보를 자바스크립트로 받을 수 있을 겁니다.
req = requests.get('https://id.twitch.tv/oauth2/validate', headers={"Authorization":f"Bearer {app_token}"})
print(req.json())