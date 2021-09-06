num_dict = {"zero": "ноль", "one": "один",
              "two": "два", "three": "три",
              "four": "четыре", "five": "пять",
              "six": "шесть", "seven": "семь",
              "eight": "восемь", "nine": "девять", "ten": "десять"}
def num_translate(word):
    in_word = word.lower()
    if word.istitle() and in_word in num_dict:
        return  num_dict.get(in_word).title()
    return  num_dict.get(word)
print(num_translate(input("Введите название цифры от 0 до 10 на английском с загланой буквы: ")))