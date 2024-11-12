import subprocess
import sys

def execute_command(user_input):
    # Vulnerable to command injection
    command = f"echo {user_input}"
    subprocess.run(command, shell=True)

try:
    # Disable the input function
    __builtins__.input = lambda _: "disabled"
except AttributeError:
    pass

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python vulnerable_script.py <input>")
    else:
        execute_command(sys.argv[1])
