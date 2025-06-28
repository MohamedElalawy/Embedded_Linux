#!/usr/bin/python3
import os
import subprocess

# Directory options (customize paths if needed)
directories = {
    "Downloads": os.path.expanduser("~/Downloads"),
    "Python": os.path.expanduser("~/python"),  # From your Desktop list
    "venv": os.path.expanduser("~/venv")       # From your Desktop list
}

def main():
    print("Available directories:")
    for i, (name, path) in enumerate(directories.items()):
        print(f"{i}: {name}")
    
    try:
        choice = int(input("Select directory (0-2): "))
        selected_name = list(directories.keys())[choice]
        selected_path = directories[selected_name]
        
        if os.path.exists(selected_path):
            subprocess.run(["nautilus", selected_path])
        else:
            print(f"Error: Path doesn't exist - {selected_path}")
    
    except (ValueError, IndexError):
        print("Invalid input. Please enter 0, 1, or 2")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
