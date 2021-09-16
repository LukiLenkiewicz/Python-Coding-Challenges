import sqlite3
from cryptography.fernet import Fernet

DATABASE_NAME = "passwords.db"

conn = sqlite3.connect(DATABASE_NAME)
c = conn.cursor()


def create_new_file():
    try:
        c.execute("SELECT * FROM passwords")
    except sqlite3.OperationalError:
        print("Tworzenie nowej tabeli")
        c.execute("""CREATE TABLE passwords (
                website_name text,
                website_password text
            )""")
        return {}
    else:
        data = c.fetchall()
        data = turn_into_dictionary(data)
        return data


def turn_into_dictionary(data):
    dic = {}
    for password in data:
        dic[password[0]] = password[1]
    return dic


def save_passwords(passwords):
    passwords = passwords.items()
    c.execute("DELETE FROM passwords")
    c.executemany("INSERT INTO passwords VALUES (?, ?)", passwords)
    conn.commit()


def get_key():
    ACCESS_PASSWORD_FILE_NAME = "keys.db"
    conn = sqlite3.connect(ACCESS_PASSWORD_FILE_NAME)
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM password_key_table")
        key = cur.fetchall()
        key = key[0][0]
        conn.close()
    except FileNotFoundError:
        print("Nie znaleziono klucza")
    else:
        key = key.encode()
        f = Fernet(key)
        return f
