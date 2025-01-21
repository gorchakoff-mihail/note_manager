from datetime import datetime, date
current_date = date.today()
status_3 = {'1': 'Новая', '2': 'В процессе', '3': 'Выполнена'}
create_note = {}
username = 'Имя пользователя'
title = 'Заголовок заметки'
content = 'Описание заметки'
status = 'Статус заметки'
created_date = 'Дата создания заметки'
issue_date = 'Дедлайн'
create_note.update({username: input("Введите ваше имя: ")})
create_note.update({title: input("Введите заголовок заметки: ")})
create_note.update({content: input('Введите описание заметки: ')})
print('Введите статус заметки из списка')
while True:
     print('\nСписок статусов: ')
     for key, value in status_3.items():
         print(key, '-', value)
     new_status = input('\nВедите новый статус заметки: ')
     if new_status in status_3:
         break
     else:
         print('\nТакой статус не предусмотрен. Выберите из списка.')
create_note.update({status: status_3[new_status]})
create_note.update({created_date: current_date.strftime('%d/%m/%Y')})
while True:                                     # Задаём цикл для проверки данных пользователя
    try:
        issue_data = input('\nВведите дату дедлайна в формате ДД/MM/ГГГГ: ')
        datetime.strptime(issue_data, '%d/%m/%Y')
        break
    except ValueError:
        print('\nВведённая дата не соответствует формату.')
                                                # Вывод текста на экран, если введённые данные некорректны
#current_date = datetime.strptime(current_date, '%d/%m/%Y')
issue_data = datetime.strptime(issue_data, '%d/%m/%Y')
create_note.update({issue_date: issue_data.strftime('%d/%m/%Y')})
print(create_note)