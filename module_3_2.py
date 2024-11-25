def send_email(message, recipient, sender = "university.help@gmail.com"):
    flag1 = None
    flag2 = None
    flag3 = None

    for i in recipient:
        flag1 = True
        if i == '@':
            flag1 = True
            break
        else:
            flag1 = False

    for i in sender:
        flag2 = True
        if i == '@':
            flag2 = True
            break
        else:
            flag2 = False

    for j in ['.com', '.ru', '.net']:
        if recipient[-len(j):] and sender[-len(j):] != j:
            flag3 = False
        else:
            flag3 = True
            break

    for g in [flag1, flag2, flag3]:
        if g == True:
            continue
        else:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    if sender == recipient:
        print('Нельзя отправить самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')