'''main module of sending mail message as reminder to return book'''
from data_base import DataBaseCursor, DataBaseConnection
from mail_message import MailMessage
from mail_sending import MailSending

# from data_base - cursor
data_base_cursor = DataBaseCursor('********.db') #name or directory of data base for cursor
cursor = data_base_cursor.data_base_con_curs()

# from data_base - data base connection

data_base = DataBaseConnection(cursor)
data = data_base.data_base_con()

# from mail_message
message = MailMessage(data)
mail_message = message.mail_message()
print(mail_message)

# from mail_sending
USER = '*****@****.***'  # sender login
PASSWORD = '*******' # sender password
mail_sending = MailSending(USER, PASSWORD, mail_message)

print('-'*15)
mail_sending.mail_sending()
print('-'*15)
