# main.py

import os
import datetime
from groq_api import get_command_from_prompt

# {FOR LINX ENVIRONMENT , uncomment this and remove the executor_windows}
# from executor import execute_command

#FOR WINDOWS TERMINAL
from executor_windows import execute_command, is_command_safe



LOG_FILE = "logs/session_log.txt"
os.makedirs("logs", exist_ok=True)

def log_interaction(prompt, command, result):
    with open(LOG_FILE, "a") as f:
        f.write(f"\n[{datetime.datetime.now()}]\n")
        f.write(f"Prompt: {prompt}\n")
        f.write(f"Command: {command}\n")
        f.write(f"Result:\n{result}\n")

def main():
    print("🧠 LLM Terminal Assistant (Groq-powered)")
    
    # if not os.environ.get("GROQ_API_KEY"):
    #     print("❌ Error: GROQ_API_KEY not set in environment.")
    #     return

    while True:
        prompt = input("\n📝 Your request (or type 'exit'): ").strip()
        if prompt.lower() in ["exit", "quit"]:
            break

        print("🤖 Thinking...")

        try:
            command = get_command_from_prompt(prompt)
        except Exception as e:
            print(f"❌ Failed to fetch command: {e}")
            continue

        print(f"\n🛠️ Suggested Command:\n{command}")

        # if not is_command_safe(command):
        #     print("❌ Command not allowed for safety reasons.")
        #     continue

        confirm = input("✅ Run this command? (y/n): ").strip().lower()
        if confirm != "y":
            print("⏩ Skipped execution.")
            continue

        result = execute_command(command)
        print(f"\n📤 Output:\n{result}")

        log_interaction(prompt, command, result)

if __name__ == "__main__":
    main()
