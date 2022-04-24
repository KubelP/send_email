'''This module creat message to send by email'''

class MailMessage:
    '''Class creat message from data unupacked in class DataBaseConnection'''
    def __init__(self, data):
        self.data = data
        self.message_pack = []

    def mail_message(self):
        '''Creating message and return final message as message_pack'''
        for mail, name, title in self.data:
            message_to_send = {mail : f'{name}!!!! You are late with return\
                 date of my book titeled {title}'}
            self.message_pack.append(message_to_send)
        return self.message_pack
