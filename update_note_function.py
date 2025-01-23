from datetime import datetime
def update_note(note):
                                    # Вызываем функцию обновления заметки, в котором за аргумент принимается note
    print("\nТекущие данные заметки: ", '\n', note)
    note_field = ["username", "title", "content", "status", "issue_date"]
                                    # Поля заметки, которые будут подлежать обновлению
    while True:
                                    # Запускаем цикл, в котором надо выбрать поле для обновления
        note_field_to_update = input("\nКакие данные вы хотите обновить? "
                                   "(username, title, content, status, issue_date): ").lower()
        if note_field_to_update not in note_field:
            print("\nПожалуйста, выберите из списка!")
            continue
        new_value = input(f"\nВведите новое значение для {note_field_to_update}: ")
                                    # Когда выбрано нужное поле, просим ввести новое значение
        if note_field_to_update == "issue_date":
            try:
                datetime.strptime(new_value, "%d.%m.%Y")
            except ValueError:
                    print("\nНеверный формат даты! Пожалуйста, введите правильный формат даты, например 25.12.2024!")
                    continue
                                    # Если в качестве критерия выбрана дата дедлайна,
                                    # то запускаем блок на проверку ошибок и ввода правильного формата
        note[note_field_to_update] = new_value
        return note
if __name__ == "__main__":
    note = {
        'username': 'Роман',
        'title': 'Список покупок',
        'content': 'Купить продукты на неделю',
        'status': 'новая',
        'created_date': '27.11.2024',
        'issue_date': '30.11.2024'
    }

    if __name__ == "__main__":
        updated_note = update_note(note)    # Присваем словарю начальные данные ключ-значение
        print("\nОбновлённая заметка:")
        print(updated_note)