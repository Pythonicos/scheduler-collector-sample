def send_mail(mail_list: {}):
    for mail in mail_list:
        print("E-mail enviado para {contact} with subject: {subject}"
              .format(contact=mail["contact"], subject="subject"))
