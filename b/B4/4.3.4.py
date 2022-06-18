def reverse_str(text):
    if len(text) == 0:
        return ''
    else:
        return text[-1] + reverse_str(text[:-1])

text = "tesx"
print(reverse_str(text))
print(text[::-1])
