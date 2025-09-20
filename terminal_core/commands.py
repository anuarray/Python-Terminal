import os
import shutil
from utils.helpers import error_message

def execute_command(command_input, current_dir):
    parts = command_input.split()
    command = parts[0]
    args = parts[1:]

    if command == "ls":
        return ls_command(current_dir)
    elif command == "pwd":
        print(current_dir)
        return current_dir
    elif command == "cd":
        return cd_command(args, current_dir)
    elif command == "mkdir":
        mkdir_command(args, current_dir)
        return current_dir
    elif command == "rm":
        rm_command(args, current_dir)
        return current_dir
    else:
        error_message(f"Command '{command}' not found.")
        return current_dir

def ls_command(current_dir):
    try:
        items = os.listdir(current_dir)
        for item in items:
            print(item)
    except Exception as e:
        error_message(f"Error listing directory: {e}")
    return current_dir

def cd_command(args, current_dir):
    if not args:
        error_message("Usage: cd <directory>")
        return current_dir

    new_path = os.path.abspath(os.path.join(current_dir, args[0]))
    if os.path.isdir(new_path):
        return new_path
    else:
        error_message(f"No such directory: {args[0]}")
        return current_dir

def mkdir_command(args, current_dir):
    if not args:
        error_message("Usage: mkdir <folder_name>")
        return

    folder_path = os.path.join(current_dir, args[0])
    try:
        os.makedirs(folder_path)
        print(f"Directory '{args[0]}' created successfully.")
    except FileExistsError:
        error_message("Directory already exists.")
    except Exception as e:
        error_message(f"Error creating directory: {e}")

def rm_command(args, current_dir):
    if not args:
        error_message("Usage: rm <file_or_folder>")
        return

    target_path = os.path.join(current_dir, args[0])
    try:
        if os.path.isdir(target_path):
            shutil.rmtree(target_path)
            print(f"Directory '{args[0]}' removed successfully.")
        elif os.path.isfile(target_path):
            os.remove(target_path)
            print(f"File '{args[0]}' removed successfully.")
        else:
            error_message("No such file or directory.")
    except Exception as e:
        error_message(f"Error removing file/directory: {e}")
