import sqlite3 

class DataBaseConnection:
    def __init__(self, data_base):
        self.data_base = data_base
    
    def data_base_con(self):  
        with sqlite3.connect(self.data_base) as connection: 
            cursor = connection.cursor()
            cursor.execute('SELECT email, name, title FROM borrows WHERE return_at>?', ('13-04-2022 23:59:59', ))
            data = cursor.fetchall()
            return data





data_base1 = DataBaseConnection(r'C:\Users\Quantum\AppData\Local\Programs\Python\Python310\pycamp\send_email\books_borrows.db')
for a in data_base1.data_base_con():
    print(a)
    