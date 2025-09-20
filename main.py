import os
from terminal_core.commands import execute_command

def main():
    print("Welcome to PyTerminal! Type 'exit' or 'quit' to close.\n")
    
    current_dir = os.getcwd()

    while True:
        try:
            command_input = input(f"{current_dir}> ").strip()

            if command_input.lower() in ["exit", "quit"]:
                print("Exiting PyTerminal. Goodbye!")
                break

            if not command_input:
                continue

            current_dir = execute_command(command_input, current_dir)

        except KeyboardInterrupt:
            print("\n[!] Keyboard interrupt detected. Type 'exit' to quit safely.")
        except Exception as e:
            print(f"[Error] Unexpected issue: {e}")

if __name__ == "__main__":
    main()
