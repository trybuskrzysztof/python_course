todos = []

while True:
    user_action = input('Type add, show, edit or exit: ')
    user_action = user_action.strip().lower()

    match user_action:
        case 'add':
            todo = input('Enter a todo: ')
            todos.append(todo.title())
            todos.sort()
        case 'show' | 'display':
            if len(todos) == 0:
                print('List contains no items')
            else:
                for item in todos:
                    print(item)
        case 'edit':
            i = 1
            for item in todos:
                print(f'{i} - {item}')
                i += 1

            edit_element_index = int(input('Please choose number to edit from list above: '))
            edit_element_index = edit_element_index - 1
            edit_element_value = input(f"Please provide new value for '{todos[edit_element_index]}': ")
            todos[edit_element_index] = edit_element_value.title()
        case 'exit':
            break
        case _:
            print(f'Command {user_action} not recognized')

print('Bye!')
