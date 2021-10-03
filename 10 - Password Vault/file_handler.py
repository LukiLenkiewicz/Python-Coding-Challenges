import sqlite3
from cryptography.fernet import Fernet
import bcrypt
from constants import PASSWORDS_DATABASE, KEY_ACCESS_DATABASE, PASSWORD_KEY_TABLE_NAME, ACCESS_KEY_TABLE_NAME


conn = sqlite3.connect(PASSWORDS_DATABASE)
c = conn.cursor()


def get_passwords():
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
        return turn_into_dictionary(c.fetchall())


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
    key = load_file(PASSWORD_KEY_TABLE_NAME)
    key = key.encode()
    return Fernet(key)


def user_login():
    hashed = load_file(ACCESS_KEY_TABLE_NAME)
    check_password_corectness(hashed)


def load_file(table_name):
    conn = sqlite3.connect(KEY_ACCESS_DATABASE)
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM "+table_name+"")
        key = cur.fetchall()
        key = key[0][0]
        conn.close()
    except FileNotFoundError:
        print("Nie znaleziono pliku")
    else:
        return key


def check_password_corectness(hashed):
    hashed = hashed.encode()
    access_password = input("Podaj hasło: ")
    access_password = access_password.encode()
    while not bcrypt.checkpw(access_password, hashed):
        access_password = input("Podałeś złe hasło, spróbuj ponownie: ")
        access_password = access_password.encode()
    print("Dostęp przyznany")
