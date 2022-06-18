text_first = "Кит на море романтик"

def palindrom(r):
    text = r.lower()
    text = text.replace(" ", "")

    if text == text[::-1]:
        print(f'"{r}" - палиндром')
        return True
    else:
        print(f'"{r}" - это не палиндром')
        return False

palindrom(text_first)
palindrom("аппа")
palindrom(input("Ввести текст проверки на палиндром: "))
