import os
with open('input.txt', 'w', encoding='utf8') as f:
    txt = os.listdir()
    for line in txt:
        f.writelines(line+"\n")
out = open('output.txt', 'w', encoding='utf8')
f = open("input.txt", 'r', encoding='utf8')
for line in f:
    out.writelines(line)
f.close()
out.close()
out = open('output.txt')
for line in out:
    print(line, end='')
out.close()
