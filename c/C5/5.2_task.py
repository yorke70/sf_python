import requests
import json
import os

r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
r = json.loads(r.content)

with open('test.txt', 'w', encoding='utf-8') as file:
    for text in r:
        count = 0
        for _ in text:
            count += 1
            if count == 60:
                file.write('\n')
                count = 0
            file.write(_)
        file.write('\n')
# print(r[0])
