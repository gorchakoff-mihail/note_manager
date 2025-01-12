from datetime import datetime, date
today = date.today()                            # Получаем текущую дату, при помощи оператора "today"
current_date = today.strftime('%d/%m/%Y')       # Задаём формат текущей даты
print(f'\nТекущая дата: {current_date}')        # Выводим текущую дату
while True:                                     # Задаём цикл для проверки данных пользователя
    try:
        issue_data = input('\nВведите дату истечения заметки в формате ДД/MM/ГГГГ: ')
        datetime.strptime(issue_data, '%d/%m/%Y')
        break
    except ValueError:
        print('\nВведённая дата не соответствует формату.')
                                                # Вывод текста на экран, если введённые данные некорректны
print('\nДедлайн: ', issue_data)                # Вывод на эран даты дедлайна
current_date = datetime.strptime(current_date, '%d/%m/%Y')
issue_data = datetime.strptime(issue_data, '%d/%m/%Y')
                                                # Форматируем текущую дату и дедлайна в единый формат
date_analysis = issue_data - current_date       # Вычислем разницу между датами
date_analysis = date_analysis.days              # форматируем разницу между датами при помощи атрибута "day"
if date_analysis > 0:                           # Условие: "Если разница между датами больше 0"
    print(f'\nДо дедлайна осталось {date_analysis} дней')
                                                # Выводим на экран при вышеуказанном условии
elif date_analysis == 0:                        # Уловие: "При разнице между датами равной 0"
    print('\nДедлайн истекает сегодня!')
                                                # Выводим на экран при вышеуказанном условии
else:                                           # Если оба условия не подходят
    print(f'\nДедлайн истёк {date_analysis} дней назад')
                                                # Выводим на экран при истечении срока заметки