# Infinite loop to run the mini shell
while True:
    # Get user input
    cmd = input("mini-shell> ")

    # Exit command
    if cmd == "exit":
        print("Bye bye see you later")
        break  # Exit the loop

    # Hello command
    elif cmd == "hello":
        print("Hello, this is pentesting service")

    # Specific message command
    elif cmd == "I want to use your service":
        print("sorry this is developing now please coming soon...")

    # Unknown command
    else:
        print("command not found")

    # Show what command is being executed
    print(f"Executing: {cmd}")
