def send_email(message, recipient, *,sender = "university.help@gmail.com"):
    if '@' not in recipient:
        adress_flag = False
    elif "@" not in sender:
        adress_flag = False
    elif ".com" or ".ru" or ".net" not in recipient:
        adress_flag = False
    elif ".com" or ".ru" or ".net" not in sender:
        adress_flag = False
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    else:
        if sender == recipient:
            print(f'Нельзя отправить письмо самому себе!')
        elif sender == "university.help@gmail.com:":
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        else:
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

print(send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com'))
print(send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com'))
print(send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk'))
print(send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru'))
