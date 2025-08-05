
# secure_script.py
import os
import ast
import getpass
import subprocess

print("=== Secure Script ===")

# --- Step 1: Secure login ---
username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")

# --- Step 2: Safe math evaluation ---
cmd = input("\nEnter a math operation (e.g., 2 + 2): ")
try:
    result = ast.literal_eval(cmd)
    if isinstance(result, (int, float)):
        print("Result:", result)
    else:
        print("Only numeric expressions are allowed.")
except Exception as e:
    print("Invalid input:", e)

# --- Step 3: Safe file read from a fixed folder ---
SAFE_FOLDER = "files"  # Create this folder manually
os.makedirs(SAFE_FOLDER, exist_ok=True)
filename = input("\nEnter filename to read (inside 'files/' folder): ").strip()
safe_path = os.path.join(SAFE_FOLDER, os.path.basename(filename))

try:
    with open(safe_path, "r") as f:
        print(f"\nContents of {filename}:")
        print(f.read())
except FileNotFoundError:
    print("File not found or not allowed.")
except Exception as e:
    print("Error reading file:", e)

# --- Step 4: Safe system command execution ---
allowed_commands = {
    "date": ["date"],
    "whoami": ["whoami"],
    "uptime": ["uptime"]
}
user_cmd = input("\nEnter a command (date, whoami, uptime): ").strip().lower()
if user_cmd in allowed_commands:
    try:
        result = subprocess.run(allowed_commands[user_cmd], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print("Error running command:", e)
else:
    print("Command not allowed.")
