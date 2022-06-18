with open('marks.txt', 'r') as a:
    for line in a:
        temp = line.split()
        if int(temp[-1]) < 3:
            print(*temp[:2])
