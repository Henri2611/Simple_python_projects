todo_list = []

def displayList():
    if len(todo_list) == 0:
        print("your to-do list is empty")
    else:
        for i, x in enumerate(todo_list, start = 1):
            print(f"{i}.{x}")

def addItems(item):
    if item not in todo_list:
        todo_list.append(item)
        print(f"Added: {item}")
        
    else:
        print("Item already exists")

def removeItems(item):
    try:
        if item:
            todo_list.remove(item)
            print(f"{item} is deleted ")
    except ValueError:
        print("Item not found")
        
def userInput():
    while True:
        displayList()
        userTask = input("Type '+' to add a task, '-' to Delete a task, or 'exit' to quit: ");
        if userTask == '+':
            task = input("Enter a task: ")
            if task:
                addItems(task)

        elif userTask == '-':
            task = input("Delete a task: ")
            if task:
                removeItems(task)
                
        elif userTask.lower() == 'exit':
            confirm = input("Are you sure you want to exit? (y/n): ")
            if confirm.lower() == 'y':
                print("Exiting...")
                break
            
        else:
            print("Invalid Input")
            
userInput()
