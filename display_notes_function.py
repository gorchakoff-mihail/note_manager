def display_page(notes, page):
    start_index = 0 + page * 5
    end_index = 5 + page * 5
                                # notes[0:5] - первая страница
                                # notes[5:10] - вторая страница
    for index, note in enumerate(notes[start_index:end_index], start=1):  # f строки f string
        print(f"""
        Номер заметки: {index}
        Имя пользователя: {note['username']}
        Заголовок: {note['title']}
        Описание: {note['content']}
        Статус: {note['status']}
        Дата создания: {note['created_date']}
        Дедлайн: {note['issue_date']}
        """)
        print("_" * 80)  # str * int

def display_notes(notes, page_number=0):
    if len(notes) == 0:
        print('Список заметок пуст')
    else:
        display_page(notes, page_number)

if __name__ == '__main__':
    notes = [
        {'username': 'Снежана', 'title': 'Работа',
         'content': 'Начать заниматься любимым делом', 'status': 'Новая',
         'created_date': "20-01-2025", "issue_date": "21-04-2025"},
        {'username': 'Михаил', 'title': 'Обучение',
         'content': 'Научиться и применять навыки программирования', 'status': 'В процессе',
         'created_date': '20-12-2024', 'issue_date': '22-11-2025'},
        {'username': 'Артемий', 'title': 'Обучение',
         'content': 'Закончить колледж', 'status': 'В процессе',
         'created_date': '01-09-2024', 'issue_date': '30-05-2027'},
        {'username': 'Злата', 'title': 'Работа',
         'content': 'Найти высокооплачиваемую работу', 'status': 'Отложено',
         'created_date': '18-01-2025', 'issue_date': '30-01-2025'},
        {'username': 'Михаил', 'title': 'День рождения супруги',
         'content': 'Подарить подарок и не забыть поздравить', 'status': 'Новая',
         'created_date': '25-01-2025', 'issue_date': '31-01-2025'}
    ]
    display_notes(notes=notes, page_number=0)