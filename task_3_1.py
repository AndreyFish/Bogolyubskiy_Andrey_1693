print(f"\n\n{'*' *30} task_1 {'*' *30}\n")

num_dict = {"zero": "ноль", "one": "один",
              "two": "два", "three": "три",
              "four": "четыре", "five": "пять",
              "six": "шесть", "seven": "семь",
              "eight": "восемь", "nine": "девять", "ten": "десять"}

def num_translate(word):
    return num_dict.get(word)

print(num_translate(input("Введите название цифры от 0 до 10 на английском: ")))