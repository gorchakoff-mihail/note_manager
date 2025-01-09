status_3 = {'1': 'Выполнено', '2': 'В процессе', '3': 'Отложено'}
                            # Создаём список статусов при помощи метода "словарь".
for key, value in status_3.items():
    print(key, '-', value)
                            # Использовал конструкцию для более удобного просмотра списка статусов пользователем.
current_status = input('Введите текущий статус заметки: ')
print(f'Текущий статус заметки: \n {status_3[current_status]}')
                            # Ввод и отображение текущего статуса
while True:                 # Использовал конструкцию для цикла при вводе некорректного статуса
    print('Список статусов: ')
    for key, value in status_3.items():
        print(key, '-', value)
                            # Повторно выводим список статусов для просмотра пользователем
    new_status = input('Ведите новый статус заметки: ')
    if new_status in status_3:
        break               # Ввод нового статуса и окончание цикла при вводе статуса из списка
    else:
        print('Такой статус не предусмотрен. Выберите из списка.')
                            # Вывод в консоль текста при некорректном вводе статуса
print(f'Обновлённый статус заметки: \n {status_3[new_status]}')
                            # Вывод в консоль текст и новый статус заметки