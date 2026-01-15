while True:
    cmd = input("mini-shell> ")
    parts = cmd.split()
    if parts[0] == "hello":
        print(parts[1])
