text = input("Введите текст: ").upper()

print(f"Введено {len(set(text.split()))} уникальных слов")
