'''Modul sending message by e-mail'''
import smtplib

class MailSending:
    '''class sending e-mail used smtplib'''
    def __init__(self, user, password, message_pack):
        self.user = user
        self.password = password
        self.message_pack = message_pack

    def mail_sending(self):
        '''sending email'''
        for message in self.message_pack:
            for email in message:
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                    server.login(self.user, self.password)
                    server.sendmail(self.user, email, message[email])
                print('e-mail send')
