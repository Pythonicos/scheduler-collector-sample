import requests
from parser import get_parser
from email_sender import send_mail


def get_posts():
    output = []
    for parser, url in url_list:
        response = requests.get(url)
        output.append(get_parser(parser).parse(response))
    return output


def send_posts(update_list):
    contact_list = ["ohrlando@gmail.com"]
    mails = [{
                 "contact": contact_list,
                 "subject": "New %s updates" % site_name,
                 "content": content
             } for site_name, content in update_list]

    send_mail(mails)


if __name__ == '__main__':
    url_list = [("Google", "http://www.google.com"), ("Uol", "http://www.uol.com.br/")]

    updates = get_posts()
    send_posts(updates)
