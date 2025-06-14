# # executor.py
# import subprocess
# import shlex

# ALLOWED_COMMANDS = ["ls", "mkdir", "rm", "mv", "cp", "touch", "cat", "echo"]

# def is_command_safe(command: str) -> bool:
#     return any(command.startswith(cmd) for cmd in ALLOWED_COMMANDS) and "rm -rf /" not in command

# def execute_command(command: str) -> str:
#     try:
#         result = subprocess.run(shlex.split(command), capture_output=True, text=True, check=True)
#         return result.stdout.strip()
#     except subprocess.CalledProcessError as e:
#         return f"Error: {e.stderr.strip()}"

# executor.py
import subprocess
import shlex
import re

# Define commands considered safe for execution
ALLOWED_COMMANDS = [
    "ls", "mkdir", "rm", "mv", "cp", "touch", "cat", "echo", "pwd", "cd"
]

def clean_command(command: str) -> str:
    """
    Cleans the command string:
    - Removes Markdown formatting (```bash ... ```)
    - Strips leading/trailing whitespace
    """
    command = command.strip()
    command = re.sub(r"^```(bash)?", "", command)
    command = re.sub(r"```$", "", command)
    return command.strip()

# def is_command_safe(command: str) -> bool:
#     """
#     Check if the command is in the list of allowed commands.
#     Prevents dangerous operations like 'rm -rf /'
#     """
#     command = clean_command(command)
#     return any(command.startswith(cmd) for cmd in ALLOWED_COMMANDS) and "rm -rf /" not in command

def execute_command(command: str) -> str:
    """
    Execute the given shell command and return the result.
    """
    command = clean_command(command)
    try:
        result = subprocess.run(
            shlex.split(command),
            shell =True,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip() or "[Command executed successfully]"
    except subprocess.CalledProcessError as e:
        return f"[ERROR]: {e.stderr.strip()}"
    except Exception as e:
        return f"[UNEXPECTED ERROR]: {str(e)}"
