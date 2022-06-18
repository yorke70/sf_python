a = "aaabbccccdaa"
count = 0
prev = a[0]
sum = ""
for i in a:
    if prev == i:
        count += 1
    if count >= 1 and prev != i:
        sum += prev + str(count)
        count = 1
    prev = i

sum += prev + str(count)
print(sum)
