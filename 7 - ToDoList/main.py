import json
import os

JSON_FILE_NAME = 'tasks.json'
EXIT_COMMAND = 'exit'


def todolist():
    tasks = create_new_file()
    user_command = ''
    while user_command != EXIT_COMMAND:
        print_tasks(tasks)
        user_command = input('Podaj komendę użytkownika lub wpisz "help" aby uzyskać pomoc: ')
        tasks = checking_user_input(tasks, user_command)
        save_task(tasks)


def create_new_file():
    if os.path.exists(JSON_FILE_NAME):
        with open(JSON_FILE_NAME, 'r') as file:
            return json.load(file)
    else:
        print('Tworzenie pustej listy zadań')
        tasks = {}
        with open(JSON_FILE_NAME, 'w') as file:
            json.dump(tasks, file)
        return tasks


def add_task(tasks, task_description):
    task_id = 1
    while True:
        if str(task_id) not in list(tasks.keys()):
            tasks[str(task_id)] = {'Status': 'NEW', 'Description': task_description[4:]}
            print(f"Zadanie \"{tasks[str(task_id)]['Description']}\" dodane z powodzeniem.\n")
            return tasks
        else:
            task_id += 1


def remove_task(task_id, tasks):
    if task_id in list(tasks.keys()):
        del tasks[task_id]
        print("Zadanie usunięte z powodzeniem\n")
        return tasks
    else:
        print("Nie ma takiego ID")
        return tasks


def resolve_task(task_id, tasks):
    if task_id in list(tasks.keys()):
        tasks[task_id]['Status'] = 'DONE'
        return tasks
    else:
        print("Nie ma takiego ID.")
        return tasks


def print_tasks(tasks):
    if len(tasks) == 0:
        print("Lista zadań jest pusta.")
    else:
        for task_id, task in tasks.items():
            print(f"{task_id} {task['Status']} {task['Description']}")


def split_user_input(command):
    command = command.split()
    return command[0], command


def checking_user_input(tasks, user_command):
    ADDING_TASK_COMMAND = 'add'
    REMOVE_TASK_COMMAND = 'remove'
    RESOLVE_TASK_COMMAND = 'resolve'
    PRINT_HELP_COMMAND = 'help'
    command_check, split_user_command = split_user_input(user_command)
    if command_check.lower() == ADDING_TASK_COMMAND:
        tasks = add_task(tasks, user_command)
    elif command_check.lower() == REMOVE_TASK_COMMAND:
        tasks = remove_task(split_user_command[1], tasks)
    elif command_check.lower() == RESOLVE_TASK_COMMAND:
        tasks = resolve_task(split_user_command[1], tasks)
    elif command_check.lower() == PRINT_HELP_COMMAND:
        print(f'"add <treść zadania>" dodaje zadanie\n"remove <ID zadania>" usuwa zadanie\n"resolve <ID zadania>" '
              f'oznacza zadanie jako wykonane\n"exit" opuszcza program\n"help" wyświetla pomoc\n')
    elif user_command == EXIT_COMMAND:
        pass
    else:
        print("Niepoprawna komenda użytkownika\n")
    return tasks


def save_task(tasks):
    with open(JSON_FILE_NAME, 'w') as file:
        json.dump(tasks, file)


todolist()
