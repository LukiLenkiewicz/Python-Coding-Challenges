import json

JSON_FILE_NAME = "hidden_passwords.json"


def create_new_file():
    try:
        with open(JSON_FILE_NAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Tworzenie pustej listy haseł")
        passwords = {}
        with open(JSON_FILE_NAME, 'w') as file:
            json.dump(passwords, file)
        return passwords


def save_task(passwords):
    with open(JSON_FILE_NAME, 'w') as file:
        json.dump(passwords, file)
