from bs4 import BeautifulSoup
import requests



base = "https://ru.stackoverflow.com/"
html = requests.get(base).content
soup = BeautifulSoup(html, 'lxml')
div = soup.find('div', id='question-mini-list')
a = div.find_all('a', class_='s-link')
temp_a = []
final_a = {}
for _ in range(a):
    if 's-link__muted' not in str(_):
       temp_a.append(_)

for _ in temp_a:
    print(_.getText(), base + _.get('href'))
    final_a[_.getText()] = base + _.get('href')

for key, value in final_a.items():
    print(key, ' -> ', value)


