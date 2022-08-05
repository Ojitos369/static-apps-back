import datetime

from django.core.mail import EmailMultiAlternatives, EmailMessage
from static_apps.settings import EMAIL_DATA, DEFAULT_FROM_EMAIL

class EmailError:
    def __init__(self, err):
        self.to_email = [EMAIL_DATA['admin_email']]
        self.bcc_email = ['']
        self.email_subject = 'ERROR EN STATIC APPS'
        self.email_text = err
    
    def send(self):
        from_email = DEFAULT_FROM_EMAIL
        to_email = self.to_email
        bcc_email = self.bcc_email
        
        email_message = EmailMessage(
            subject = self.email_subject,
            body = self.email_text,
            from_email = from_email,
            to = to_email,
            bcc = bcc_email
        )
        
        if hasattr(self, 'file_names'):
            for file_name in self.file_names:
                with open(f'{self.rute_file}/{file_name[0]}', 'rb') as f:
                    email_message.attach(file_name[0], f.read(), file_name[1])
        print(f'sending email {datetime.datetime.now()}')
        email_message.send()
        print(f'email sended {datetime.datetime.now()}')
        return True