# import requests
# import json
#
#
# r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')  # делаем запрос на сервер по переданному адресу
# texts = json.loads(r.content)
# print(type(texts))
#
# for text in texts:
#     print(text[:50], "\n")
#
import requests
# import json
#
#
# r = requests.get('https://api.github.com')
#
# d = json.loads(r.content)
# print(type(d))
# print(d['following_url'])
import requests
import json

data = {'key' : 'value'}

r = requests.post('https://httpbin.org/post', json = json.dumps(data))  # отправляем пост-запрос
print(r.content)  # содержимое ответа и его обработка происходит так же, как и с ГЕТ-запросами, разницы никакой нету
