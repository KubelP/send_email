from data_base import DataBaseConnection
from mail_message import MailMessage
from mail_sending import MailSending

# from data_base
data_base = DataBaseConnection('data_base.db') # name and directory of data base
data = data_base.data_base_con()

# from mail_message
message = MailMessage(data)
mail_message = message.mail_message()

# from mail_sending
user = '*******@gmail.com'  # sender login
password = '******' # sender password
mail_sending = MailSending(user, password, mail_message)

print('-'*15)
mail_sending.mail_sending()
print('-'*15)