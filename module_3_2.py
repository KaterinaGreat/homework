def send_email(message, recipient, *,sender = "university.help@gmail.com"):
    if ('@' or (".com" or ".ru" or ".net")) not in (recipient or sender) or ("@" and (".com" or ".ru" or ".net")) not in (sender or recipient):
        return f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.'
    elif recipient == sender:
        adress_flag = "Нельзя отправить письмо самому себе!"
        return adress_flag.endswith("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        return f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}."
    elif sender != "university.help@gmail.com":
        return f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}."

print(send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com'))
print(send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com'))
print(send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk'))
print(send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru'))