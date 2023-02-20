while True:
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.strip().lower()

    match user_action:
        case 'add':
            todo = input('Enter a todo: ') + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()

            todos.append(todo)
            todos.sort()
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show' | 'display':
            if len(todos) == 0:
                print('List contains no items')
            else:
                for item_index, item in enumerate(todos, start=1):
                    row = f"{item_index}-{item}"
                    print(row)
        case 'edit':
            i = 1
            for item in todos:
                print(f'{i} - {item}')
                i += 1

            edit_element_index = int(input('Please choose number to edit from list above: '))
            edit_element_index = edit_element_index - 1
            edit_element_value = input(f"Please provide new value for '{todos[edit_element_index]}': ")
            todos[edit_element_index] = edit_element_value.title()
        case 'complete':
            number = int(input('Please choose number of item to complete: '))
            todos.pop(number - 1)
        case 'exit':
            break
        case _:
            print(f'Command {user_action} not recognized')

print('Bye!')
