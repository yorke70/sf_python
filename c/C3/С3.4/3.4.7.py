# with open('marks.txt', 'r') as file:
#     list_ = file.readlines()
#     print(list_)
#     for i in reversed(list_):
#         print(i, end='')
with open('marks.txt', 'a') as file:
    file.write('\n')
with open('marks.txt', 'r') as input_f:
    with open('marks_reversed.txt', 'w') as output_f:
        for line in reversed(input_f.readlines()):
            output_f.write(line)

with open('marks_reversed.txt') as file:
    for line in file:
        print(line, end='')
