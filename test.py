while True:
 cmd = input("mini-shell> ")
 if cmd == "exit" :
  print("Bye bye see you later")
 elif cmd == "hello":
  print("Hello,this is pentesting service")
 elif cmd == "I want to use your service":
  print("sorry this is developing now please coming soon...")
 else:
  print("command not found")
 break
 print(f"Executing: {cmd}")
