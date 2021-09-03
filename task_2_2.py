sentence = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
g_sentence = []
for i in sentence:
        if i.replace("+", "").replace("-", "").isdigit():
            if i.isdigit():
                g_sentence.append(f"'{int(i):02}'")
            else:
                g_sentence.append(f"'{i[0]}{int(i[1:]):02}'")
        else:
            g_sentence.append(i)
print(g_sentence)
print(" ".join(g_sentence))