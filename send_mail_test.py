'''module with tests for main_mail_sending'''
import mailcap
import sqlite3
from unittest.mock import patch
from data_base import DataBaseConnection
from mail_sending import MailSending

def test_data_base_connection():
    '''takes no parameters, creates data base in memory'''
    test_connection = sqlite3.connect(':memory:')
    test_cursor = test_connection.cursor()
    test_cursor.execute('''CREATE TABLE borrows
    (id INTIGER, 
    email TEXT,
    name TEXT,
    title TEXT,
    return_at)''')
    sample = (1, 'mail@.com', 'name', 'book_title', '01-01-2000')
    test_cursor.execute('INSERT INTO borrows VALUES(?, ?, ?, ?, ?)', sample)
    test_connection_cursor = DataBaseConnection(test_cursor)

    assert test_connection_cursor.data_base_con()[0] == ('mail@.com', 'name',\
         'book_title', '01-01-2000')

@patch('smtplib.SMTP_SSL')
def test_mail_sending(smtplib_mock):
    '''uses mock method to asssert call to smtplib '''
    test_sending = MailSending('test_login', 'test_password', [{'test_mail' : 'book_title'}])
    test_sending.mail_sending()
    smtplib_mock.assert_called()
    test_context = smtplib_mock.return_value.__enter__.return_value
    test_context.login.assert_called()
    test_context.sendmail.assert_called_with('test_login', 'test_mail', 'book_title')