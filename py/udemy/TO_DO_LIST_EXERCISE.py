todos = []
print("**********************")
while True:
    for i in range(len(todos)):
        print(f"{i+1}) {todos[i]}")
    print("********************")
    print("Enter a command. Type 'h' for help:")
    command = input("> ")
    if command == "q":
        break
    elif command.isnumeric():
        idx= int(command)-1
        if idx >= len(todos):
            print("There is no todo with that number!")
        else:
        todos.pop(num-1)
    else:
        todos.append(command)
print("Ok, goodbye!")