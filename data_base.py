'''This module unpack data base and returns data'''

import sqlite3, datetime

class DataBaseConnection:
    '''Class connect to data base (takes data_base argument) and returns
         data in list of tuples '''
    def __init__(self, data_base):
        self.data_base = data_base
        self.return_at = datetime.datetime.today()

    def data_base_con(self):
        '''function create cursor to data base and returns data from it'''
        with sqlite3.connect(self.data_base) as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT email, name, title, return_at\
                 FROM borrows WHERE return_at < ?', (self.return_at, ))
            data = cursor.fetchall()
            return data
