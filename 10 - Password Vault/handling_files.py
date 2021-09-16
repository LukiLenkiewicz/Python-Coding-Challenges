import sqlite3
from cryptography.fernet import Fernet
import bcrypt

PASSWORDS_DATABASE = "passwords.db"
KEY_ACCESS_DATABASE = "keys.db"

conn = sqlite3.connect(PASSWORDS_DATABASE)
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
    conn = sqlite3.connect(KEY_ACCESS_DATABASE)
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


def user_login():
    conn = sqlite3.connect(KEY_ACCESS_DATABASE)
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM access_key_table")
        hashed = cur.fetchall()
        hashed = hashed[0][0]
        conn.close()
    except FileNotFoundError:
        print("Nie znaleziono pliku")
    else:
        check_password_corectness(hashed)


def check_password_corectness(hashed):
    hashed = hashed.encode()
    access_password = input("Podaj hasło: ")
    access_password = access_password.encode()
    while not bcrypt.checkpw(access_password, hashed):
        access_password = input("Podałeś złe hasło, spróbuj ponownie: ")
        access_password = access_password.encode()
    print("Dostęp przyznany")
