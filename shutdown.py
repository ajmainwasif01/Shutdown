def shutdown(command):
   
    if command.lower() == "yes":
        return "Shutting down..."
    elif command.lower() == "no":
        return "Shutdown canceled!"
    else:
        return "Invalid input! Please enter 'yes' or 'no'."


user_input = input("Do you want to shut down? (yes/no): ")
print(shutdown(user_input))
