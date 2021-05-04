import json


with open("tg_1.json", 'r', encoding="utf-8") as f:
    text = f.read()
    data = json.loads(text)
    for i in data['chats']['list']:
        sms = i['messages']
        for j in sms:
            text = j['text']
            if type(text) == str:
                print(text)
