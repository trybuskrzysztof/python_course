while True:
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.strip().lower()

    match user_action:
        case 'add':
            todo = input('Enter a todo: ') + "\n"

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show' | 'display':
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            # new_todos = [item.strip('\n') for item in todos]

            if len(todos) == 0:
                print('List contains no items')
            else:
                for item_index, item in enumerate(todos, start=1):
                    item = item.strip('\n')
                    row = f"{item_index}-{item}"
                    print(row)
        case 'edit':
            number = int(input("Number of the todo to edit"))
            number = number - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            # i = 1
            # for item in todos:
            #     print(f'{i} - {item}')
            #     i += 1
            #
            # edit_element_index = int(input('Please choose number to edit from list above: '))
            # edit_element_index = edit_element_index - 1
            # edit_element_value = input(f"Please provide new value for '{todos[edit_element_index]}': ")
            # todos[edit_element_index] = edit_element_value.title()
        case 'complete':
            number = int(input('Please choose number of item to complete: '))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index]
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

        case 'exit':
            break
        case _:
            print(f'Command {user_action} not recognized')

print('Bye!')
