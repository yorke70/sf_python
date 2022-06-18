def fun(num):
    a = list(str(num))
    print(" ".join(a[0:4]), sep="")
    if a[0:4] == a[:3:-1]:
        return True
    else:
        return False

if __name__ == "__main__":
    print(fun(int(input("введите число с четным количеством цифр:"))))

