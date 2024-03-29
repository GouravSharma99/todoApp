from functions import get_todos , write_todos

def exit():
    print("Jai ho")
    return "bye bye"

while True:
    user_action = input("Enter add , show , edit , complete or exit : ").strip().lower()

    if user_action.startswith("add"):
        todo = user_action[4:].capitalize() + "\n"
        
        todos = get_todos()
        
        todos.append(todo)
        
        write_todos(todos)
            
        
    elif user_action.startswith("show"):
        
        todos = get_todos()
        
        for index, item in enumerate(todos, start=1):
            row = f'{index}-{item}'
            print(row, end="")
            
    elif user_action.startswith("edit"):

        try:
            edit_todo = int(user_action[5:].strip())
            new_todo = input("Enter the new todo : ")
            todos[edit_todo - 1] = new_todo + "\n"
            
            write_todos(todos)
                
            print("updated successfully")
            
        except:
            print("Command Invalid")
            continue

    elif user_action.startswith("complete"):
        try:
            completed_todo = int(user_action[9:].strip())
            task_done = todos.pop(completed_todo - 1)
            
            write_todos(todos)
                
            print(f'{task_done.rstrip('\n')} completed succesfully and removed from todo list !! ')
            
        except IndexError:
            print("Item with mentioned value is not present")

    elif user_action.startswith("exit"):
        print(exit())
        break

    else:
        print("You enter wrong choice !! Plz try again \n")

print(10+20)
print("See you again")

