file_dir = 'files/todos.txt'

while True:
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.strip().lower()

    if user_action.startswith('add'):
        todo = user_action[4:] + "\n"

        with open(file_dir, 'r') as file:
            todos = file.readlines()

        todos.append(todo + '\n')

        with open(file_dir, 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('show'):
        with open(file_dir, 'r') as file:
            todos = file.readlines()

        # new_todos = [item.strip('\n') for item in todos]

        if len(todos) == 0:
            print('List contains no items')
        else:
            for item_index, item in enumerate(todos, start=1):
                item = item.strip('\n')
                row = f"{item_index}-{item}"
                print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            with open(file_dir, 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open(file_dir, 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('remove'):
        try:
            number = int(user_action[9:])

            with open(file_dir, 'r') as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open(file_dir, 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print(f'Command {user_action} not recognized')

print('Bye!')
