# Infinite loop to keep the mini shell running
while True:
    # Get user input
    cmd = input("mini-shell> ")

    # Split input into parts (words)
    parts = cmd.split()

    # NOTE: This version does not handle empty input and may crash
    # If first word is "hello", print second word
    if parts[0] == "hello":
        print(parts[1])  # print the name or message after "hello"
