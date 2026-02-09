""" Modulo per gestire una lista di cose da fare  """


todo_list = []

while True:
    todo = input('Cosa devi fare? (Premi q per uscire) ')
    if todo.lower() == 'q':
        break
    todo_list.append(todo)




for todo in todo_list:
    print(todo)



