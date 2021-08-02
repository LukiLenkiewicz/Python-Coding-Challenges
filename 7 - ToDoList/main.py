import json


def todolist():
    tasks = {}
    user_command = ''
    while user_command != 'exit':
        user_command = input('Podaj komendę użytkownika: ')
        split_user_command = user_command.split()
        command_check = split_user_command[0]
        print(tasks)
        if command_check.lower() == 'add':
            tasks = add_task(tasks, user_command)
            print("Zadanie dodane z powodzeniem.")
        elif command_check.lower() == 'remove':
            if int(split_user_command[1]) in list(tasks.keys()):
                del tasks[int(split_user_command[1])]
                print("Zadanie usunięte z powodzeniem")
            else:
                print("Nie ma takiego ID.")
        elif command_check.lower() == 'resolve':
            resolve_task()
        elif command_check.lower() == 'help':
            print(f"add dodaje zadanie\nremove usuwa zadanie\nresolve oznacza zadanie jako wykonane\n help wyświetla pomoc")
        else:
            print("Niepoprawna komenda użytkownika")

        print(tasks)
        for i, j in tasks:
            print(i ,' ', j)


def add_task(tasks, task_description):
    task_id = 1
    while True:
        if task_id not in list(tasks.keys()):
            #tasks[task_id] = task_description[4:]
            tasks[task_id] = {'Status': 'NEW', 'Description': task_description[4:]}
            return tasks
        else:
            task_id += 1


def remove_task():
    pass


def resolve_task():
    pass

# tasks = {}
#
# """konwersja z pythona na plik w formacie JSON"""
# with open('tasks.json', 'w') as file:
#     json.dump(tasks, file)
#
# """konwersja z jsona na python"""
# with open('tasks.json', 'r') as file:
#     tasks = json.loads(file)

todolist()
