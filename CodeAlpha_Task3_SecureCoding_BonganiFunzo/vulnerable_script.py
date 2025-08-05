
# vulnerable_script.py
import os

# 1. Hardcoded credentials
username = "admin"
password = "1234"

# 2. Using eval on user input (very dangerous)
cmd = input("Enter a math operation (e.g., 2 + 2): ")
print("Result:", eval(cmd))

# 3. Insecure file access (no input validation)
filename = input("Enter filename to read: ")
with open(filename, "r") as f:
    print(f.read())

# 4. Executing shell commands from user input (command injection)
command = input("Enter a system command to run: ")
os.system(command)
