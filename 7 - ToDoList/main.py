import json
import os

JSON_NAME = 'tasks.json'


def todolist():
    tasks = creating_new_file()
    print_tasks(tasks)
    user_command = ''
    while user_command != 'exit':
        user_command = input('Podaj komendę użytkownika: ')
        split_user_command = user_command.split()
        command_check = split_user_command[0]
        if command_check.lower() == 'add':
            tasks = add_task(tasks, user_command)
            print("Zadanie dodane z powodzeniem.\n")
        elif command_check.lower() == 'remove':
            if split_user_command[1] in list(tasks.keys()):
                del tasks[split_user_command[1]]
                print("Zadanie usunięte z powodzeniem\n")
            else:
                print("Nie ma takiego ID.")
        elif command_check.lower() == 'resolve':
            if split_user_command[1] in list(tasks.keys()):
                tasks[split_user_command[1]]['Status'] = 'Done'
            else:
                print("Nie ma takiego ID.")
        elif command_check.lower() == 'help':
            print(f"add dodaje zadanie\nremove usuwa zadanie\nresolve oznacza zadanie jako wykonane\nhelp wyświetla"
                  f" pomoc\n")
        elif user_command == 'exit':
            pass
        else:
            print("Niepoprawna komenda użytkownika\n")

        save_task(tasks)


def creating_new_file():
    if os.path.exists(JSON_NAME):
        with open(JSON_NAME, 'r') as file:
            return json.load(file)
    else:
        print('Tworzenie pustej listy zadań')
        tasks = {}
        with open(JSON_NAME, 'w') as file:
            json.dump(tasks, file)
        return tasks


def add_task(tasks, task_description):
    task_id = 1
    while True:
        if str(task_id) not in list(tasks.keys()):
            tasks[str(task_id)] = {'Status': 'NEW', 'Description': task_description[4:]}
            return tasks
        else:
            task_id += 1


def print_tasks(tasks):
    if len(tasks) == 0:
        print("Lista zadań jest pusta.")
    else:
        for task_id, j in tasks.items():
            print(task_id, ' ', j['Status'], ' ', j['Description'])


def save_task(tasks):
    with open(JSON_NAME, "w") as file:
        json.dump(tasks, file)


todolist()
