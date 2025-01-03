username = input("Введите ваше имя: ")
title = [input("Введите заголовок заметки: "),
         input("Введите заголовок заметки: "),
         input("Введите заголовок заметки: ")] #отдельно вложенный список заголовков
content = input("Введите описание заметки: ")
status = input("Введите статус заметки: ")
created_date = input("Введите дату создания заметки в формате ДД/ММ/ГГГГ: ")
issue_date = input("Введите дату истечения заметки в формате ДД/ММ/ГГГГ: ")
note = [username, title, content, status, created_date, issue_date]
print(note)
