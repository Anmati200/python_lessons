#Произвольное число параметров

def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.lower() in i.lower():
            same_words.append(i)
    return print(same_words)

single_root_words('Пар', 'Напарник', 'Фраза', 'Пара', 'Прага', 'Приз', 'Аквапарк')
single_root_words('Мел', 'Корабль', 'Мельник', 'Сомелье', 'Смета')