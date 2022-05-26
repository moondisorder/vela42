print('''
  _____         _           
 |_   _|__   __| | ___  ___ 
   | |/ _ \ / _` |/ _ \/ __|
   | | (_) | (_| | (_) \__ \
   |_|\___/ \__,_|\___/|___/
                           
 ''')
todos = []
while True:
    for i in range(len(todos)):
        print(f"{i+1}) {todos[i]}")
    print("********************")
    print("Enter a command. Type 'h' for help:")
    command = input("> ")
    if command == "q":
        break
    else:
        todos.append(command)
print("Ok, goodbye!")