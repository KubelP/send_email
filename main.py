from data_base import DataBaseConnection
from mail_message import MailMessage
from mail_sending import MailSending

# from data_base
data_base = DataBaseConnection(r'C:\Users\Quantum\AppData\Local\Programs\Python\Python310\pycamp\send_email\books_borrows.db')
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