# import os
# start_pass = os.getcwd()
# os.chdir("..")
# second_pass = os.getcwd()
# os.chdir(start_pass)
# print(start_pass, second_pass, os.getcwd(), sep="\n")
# print(os.listdir())

f = open("test.txt", 'w', encoding='utf8')
f.write("This is first test string\n")
f.write("This is second test string\n")
f.close()
f = open("test.txt", 'r', encoding='utf8')
print(f.read(10))
print(f.read())
f.close()
f = open('test.txt', 'a', encoding='utf8')
sequence = ['other string\n', '123\n', 'test test\n']
f.writelines(sequence)
f.close()
f = open('test.txt', 'r', encoding='utf8')
print(*f.readlines())
f.close()
with open('test.txt') as f:
    for line in f:
        print(line, end='')

