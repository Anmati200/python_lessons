def send_email(message, recipient, sender = "university.help@gmail.ru"):
    if ("@" not in recipient or "@" not in sender or
        not ( recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net')) or
        not ( sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net'))):
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.ru":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")

send_email("Тестовое письмо с неправильной почтой", "Victor@yandex.ew")
send_email("Привет", "Anton-matyunin_2001@mail.ru", "Anton-matyunin_2001@mail.ru")
send_email("Стандартная отправка на почту", "Anton-matyunin_2001@mail.ru")
send_email("другой sender", "Anton-matyunin_2001@mail.ru", "Anton-matyunin_2001@yandex.net")