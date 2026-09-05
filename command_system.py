while True:
  command = input("Enter Command: ")
  if command == "help":
    print("Available commands: help, status, quit")
  elif command == "status":
    print("System is running")  
  elif command == "quit":
    print("Program closed")
    break
  else:
    print("Unknown command")