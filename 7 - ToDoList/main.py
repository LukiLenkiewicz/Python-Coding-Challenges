import json


def todolist():
    tasks = {}
    user_command = ''
    while user_command != 'exit':
        user_command = input('Podaj komendę użytkownika: ')
        split_user_command = user_command.split()
        command_check = split_user_command[0]
        if command_check.lower() == 'add':
            tasks = add_task(tasks, user_command)
            print("Zadanie dodane z powodzeniem.\n")
        elif command_check.lower() == 'remove':
            if int(split_user_command[1]) in list(tasks.keys()):
                del tasks[int(split_user_command[1])]
                print("Zadanie usunięte z powodzeniem\n")
            else:
                print("Nie ma takiego ID.")
        elif command_check.lower() == 'resolve':
            if int(split_user_command[1]) in list(tasks.keys()):
                tasks[int(split_user_command[1])]['Status'] = 'Done'
        elif command_check.lower() == 'help':
            print(f"add dodaje zadanie\nremove usuwa zadanie\nresolve oznacza zadanie jako wykonane\nhelp wyświetla pomoc\n")
        elif user_command == 'exit':
            pass
        else:
            print("Niepoprawna komenda użytkownika\n")
        for task_id, j in tasks.items():
            print(task_id, ' ', j['Status'], ' ', j['Description'])


def add_task(tasks, task_description):
    task_id = 1
    while True:
        if task_id not in list(tasks.keys()):
            tasks[task_id] = {'Status': 'NEW', 'Description': task_description[4:]}
            return tasks
        else:
            task_id += 1


todolist()
