def palindrom(str):
    new_str = ""
    for i in str:
        new_str = i + new_str
    return new_str


if __name__ == "__main__":
    str = "hello, world!"
    print("Исходная строка: " + str)
    print(palindrom(str))
