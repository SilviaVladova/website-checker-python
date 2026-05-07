import sqlite3


connection = sqlite3.connect('test.db')
cursor = connection.cursor()


cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')


cursor.execute('INSERT INTO users (name) VALUES ("Silvia QA")')
connection.commit()


cursor.execute('SELECT name FROM users WHERE name="Silvia QA"')
result = cursor.fetchone()

if result:
    print(f" Базата данни работи! Намерен запис: {result[0]}")
else:
    print(" Тестът се провали: записът не беше намерен.")

connection.close()
