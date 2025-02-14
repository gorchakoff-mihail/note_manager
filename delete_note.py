# Создаем список заметок с тестовыми данными
notes = [
    {
        'id': 1,
        'username': 'Алексей',
        'title': 'Список покупок',
        'description': 'Купить продукты на неделю'
    },
    {
        'id': 2,
        'username': 'Мария',
        'title': 'Учеба',
        'description': 'Подготовиться к экзамену'
    },
    {
        'id': 3,
        'username': 'Алексей',
        'title': 'Встреча',
        'description': 'Встреча с друзьями'
    }
]

# Вывод текущего списка заметок
print("Текущие заметки:")
for note in notes:
    print(f"{note['id']}. Имя: {note['username']}")
    print(f"   Заголовок: {note['title']}")
    print(f"   Описание: {note['description']}\n")

# Запрос критерия для удаления
search_term = input("Введите имя пользователя или заголовок для удаления заметки: ")

# Проверка, что ввод не пустой
if not search_term:
    print("Ошибка: критерий поиска не может быть пустым.")
else:
    # Создаем новый список для хранения заметок, которые нужно оставить
    notes_to_keep = []
    notes_to_delete = []

    # Поиск заметок для удаления
    for note in notes:
        if note['username'] == search_term or note['title'] == search_term:
            notes_to_delete.append(note)
        else:
            notes_to_keep.append(note)

    # Проверка, найдены ли заметки для удаления
    if not notes_to_delete:
        print("Заметок с таким именем пользователя или заголовком не найдено.")
    else:
        # Вывод заметок, которые будут удалены
        print("\nСледующие заметки будут удалены:")
        for note in notes_to_delete:
            print(f"{note['id']}. Имя: {note['username']}")
            print(f"   Заголовок: {note['title']}")
            print(f"   Описание: {note['description']}\n")

        # Запрос подтверждения удаления
        confirm = input("Вы уверены, что хотите удалить эти заметки? (да/нет): ")

        if confirm == 'да':
            # Обновление списка заметок
            notes = notes_to_keep

            # Обновление ID заметок
            for i, note in enumerate(notes, 1):
                note['id'] = i

            # Вывод результата
            print("\nЗаметки успешно удалены.")
            if notes:
                print("\nОстались следующие заметки:")
                for note in notes:
                    print(f"{note['id']}. Имя: {note['username']}")
                    print(f"   Заголовок: {note['title']}")
                    print(f"   Описание: {note['description']}\n")
            else:
                print("Список заметок пуст.")
        else:
            print("\nУдаление отменено.")
