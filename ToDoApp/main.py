##To Do project


#This is the main loop that runs the program continuously
#while true, unless they select exit and the program breaks
while True:
    #prompt user to input add, show, edit, complete or exit and store in user_action
    user_action = input("Type add, show, edit, complete or exit: ")
    #takes the user action and strips any whitespace
    user_action = user_action.strip()
    
    
    
    if 'add' in user_action:
        todo = user_action[4:]

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('files/todos.txt', 'w') as file:
                 file.writelines(todos)

        
    elif 'show' in user_action:

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
               
    elif 'edit' in user_action:
        number = int(input("Number of the todo to edit: "))
        number -= 1

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()
           
        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + "\n"

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)


        #complete, this allows a user to remove a specific to do by number, like checking off the list
    elif 'complete' in user_action:
        number = int(input("Number of the todo to complete: "))

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()
        index = number - 1
        todo_to_remove = todos[index]
        todos.pop(index)

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)
            
        message = f"Todo {todo_to_remove} was removed from the list"
        print(message.strip('\n'))



        #case exit, breaks out of the loop once exit is input    
    elif 'exit' in user_action:
        break
        
print("Bye!")
    
