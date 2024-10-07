##To Do project


#This is the main loop that runs the program continuously
#while true, unless they select exit and the program breaks
while True:
    #prompt user to input add, show, edit, complete or exit and store in user_action
    user_action = input("Type add, show, edit, complete or exit: ")
    #takes the user action and strips any whitespace
    user_action = user_action.strip()
    
    #use match case structure that matches add, show, edit, complete or exit, depending on
    #the user input
    match user_action:
        #case add, this allows the user to update the todos list with their 
        #also there is a todos.txt file that gets written to with the todo values
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
        #case show, displays the items in the array so far
        #uses for loop and enumerate to display items in a numberical fashion
        #with a dash in between
        case 'show' | 'display':
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)
        #case edit, allow user to update todos list by selecting
        #index of todo item and replace it with a new input        
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number -= 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        #complete, this allows a user to remove a specific to do by number, like checking off the list
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        #case exit, breaks out of the loop once exit is input    
        case 'exit':
            break
        
print("Bye!")
    
