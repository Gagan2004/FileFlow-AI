# executor_windows.py

import subprocess
import re
import os

# Windows-compatible commands (add more as needed)
ALLOWED_COMMANDS = [
    "dir", "mkdir", "del", "move", "copy", "echo", "type", "rmdir"
]

def clean_command(command: str) -> str:
    """
    Clean markdown formatting and trim whitespace.
    """
    command = command.strip()
    command = re.sub(r"^```(cmd|powershell|bash)?", "", command)
    command = re.sub(r"```$", "", command)
    return command.strip()

def is_command_safe(command: str) -> bool:
    """
    Check whether a command is allowed.
    """
    command = clean_command(command).lower()
    return any(command.startswith(cmd) for cmd in ALLOWED_COMMANDS) and "del /s /q C:\\" not in command



def fix_unix_touch_to_type(command: str) -> str:
    if "touch " in command:
        lines = command.strip().splitlines()
        fixed = []
        for line in lines:
            parts = line.strip().replace("touch ", "").split()
            for filename in parts:
                fixed.append(f'type nul > {filename.strip()}')
        return "\n".join(fixed)
    return command

def fix_unix_find_to_dir(command: str) -> str:
    if "find" in command and "-type f" in command and "-name" in command:
        # Extract file pattern
        import re
        pattern_match = re.search(r'-name\s+"(.+?)"', command)
        pattern = pattern_match.group(1) if pattern_match else "*.*"
        return f'dir /s /b {pattern}'
    return command

def fix_unix_mv_to_rename(command: str) -> str:
    if "mv " not in command:
        return command

    lines = command.strip().splitlines()
    fixed_lines = []

    for line in lines:
        line = line.strip()
        if line.startswith("mv "):
            parts = line[3:].strip().split()
            if len(parts) >= 2:
                old_name = parts[0].rstrip("/").strip()
                new_name = parts[1].rstrip("/").strip()
                fixed_lines.append(f'rename "{old_name}" "{new_name}"')
            else:
                fixed_lines.append(f':: [ERROR]: Unable to parse mv command: {line}')
        else:
            fixed_lines.append(line)

    return "\n".join(fixed_lines)






def execute_command(command: str) -> str:
    command = clean_command(command)
    command = fix_unix_touch_to_type(command)
    command = fix_unix_find_to_dir(command)
    command = fix_unix_mv_to_rename(command)

    try:
        results = []
        for line in command.strip().splitlines():
            if not line.strip():
                continue
            result = subprocess.run(
                line.strip(),
                shell=True,
                capture_output=True,
                text=True
            )
            if result.stderr:
                results.append(f"[ERROR]: {result.stderr.strip()}")
            elif result.stdout.strip():
                results.append(result.stdout.strip())
        return "\n".join(results) or "[Command executed successfully]"
    except Exception as e:
        return f"[UNEXPECTED ERROR]: {str(e)}"
