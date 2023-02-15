todos = []

while True:
    user_action = input('Type add, show or exit: ')
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
        case 'exit':
            break
        case _:
            print(f'Command {user_action} not recognized')

print('Bye!')
