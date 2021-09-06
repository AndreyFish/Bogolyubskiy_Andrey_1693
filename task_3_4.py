def thesaurus_adv(*names):
    names_dict = {}
    for name in sorted(names):
        n, s = name.split()
        val = names_dict.setdefault(s[0], {n[0]: [name]})
        n_val = val.setdefault(n[0], [name])
        if name not in n_val:
            n_val.append(name)
    return names_dict

print(thesaurus_adv("Мохамед Абдулмаджид", "Эъзоз Обод", "Ыыху Ибенпалу",
                    "Бен Сладан", "Насрулла Мустафаев", "Нарик Мунян",
                    "Мира Петрова", "Эзольда Иванова", "Антон Пирожков"))