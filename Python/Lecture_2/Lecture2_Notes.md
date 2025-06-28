# Lecture Topics
---
- **pip**
- **Useful scripts**  
- **Types of function**  
- **Strings**  
- **Help**  
- **Function**  
- **Global variable**  
- **Lambda**  
- **Quick task**  
- **Lab**  
- **Modules**  
- **Garbage Collector**  
- **List**  
- **Tuple**  
- **Set**  
- **Tasks**
---

# **`pip`** in Python:

---

### 📌 **What is `pip`?**

**`pip`** stands for **“Pip Installs Packages”** (it’s a recursive acronym).
It’s the **standard package manager** for Python.
You use `pip` to **install**, **upgrade**, and **uninstall** **Python packages** from the [Python Package Index (PyPI)](https://pypi.org/).

---

### ⚙️ **How to check if you have `pip` installed**

Open a terminal (or command prompt) and run:

```bash
pip --version
```
![image](https://github.com/user-attachments/assets/168d9a4f-b348-445f-9e01-173f694bc142)

![image](https://github.com/user-attachments/assets/9670f75b-6e55-49c1-a3b4-69259beb8318)

or sometimes:

```bash
python -m pip --version
```

![image](https://github.com/user-attachments/assets/d9769f61-e964-418f-a118-e17472c8f02c)

---

### 🚀 **Basic `pip` commands**

| Action                       | Command                              | Example                       |
| ---------------------------- | ------------------------------------ | ----------------------------- |
| Install a package            | `pip install package_name`           | `pip install requests`        |
| Install specific version     | `pip install package_name==1.2.3`    | `pip install numpy==1.24.0`   |
| Upgrade a package            | `pip install --upgrade package_name` | `pip install --upgrade flask` |
| Uninstall a package          | `pip uninstall package_name`         | `pip uninstall pandas`        |
| Show installed packages      | `pip list`                           |                               |
| Show info about a package    | `pip show package_name`              | `pip show matplotlib`         |
| Freeze (export) requirements | `pip freeze > requirements.txt`      |                               |
| Install from requirements    | `pip install -r requirements.txt`    |                               |

---

 **Count installed packages**:  
   ```bash
   pip freeze | wc -l
   ```
![image](https://github.com/user-attachments/assets/ae3b8f3c-85be-46e5-9efa-4050506c0694)

 **List all installed packages**:  
   ```bash
   pip list
   ```
![image](https://github.com/user-attachments/assets/4a95f34b-b479-46ce-b3f7-c51e23c92d4f)

   or  
   ```bash
   pip freeze
   ```
![image](https://github.com/user-attachments/assets/6a184054-a2d0-4fde-8009-b001341d88e6)


---

### 📍 **Where does `pip` install packages?**

By default, it installs to the **Python environment** you’re using —
either the **system Python**, a **virtual environment** (`venv`), or a **conda environment**.

---

### ✅ **Best practice**

When working on projects, it’s good practice to use a **virtual environment**
to isolate dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Linux/macOS
venv\Scripts\activate     # On Windows
pip install <package>
```
![image](https://github.com/user-attachments/assets/8c79f675-c2e7-4b9d-b9d7-ffe3e0c79a5c)

---


---

## ✅ 1️⃣ How to set up a **virtual environment** (`venv`)

### 📌 **Step 1: Create the `venv`**

In your project folder, open a terminal or command prompt and run:

```bash
python -m venv venv
```

* `python` — runs Python.
* `-m venv` — calls the built-in module to create a virtual environment.
* `venv` — the name of the folder that will hold the virtual environment (you can name it anything, but `venv` is common).

---

### 📌 **Step 2: Activate the `venv`**

**➡️ On macOS/Linux:**

```bash
source venv/bin/activate
```
![image](https://github.com/user-attachments/assets/f32d3444-74fe-4aa5-8ef6-37d6deff0467)


---

You’ll know it’s active because your terminal prompt will change:

```bash
(venv) $
```
![image](https://github.com/user-attachments/assets/533ce4fd-27ac-4e46-a130-d590969a9aef)

 **To deactivate (exit) your `venv`:**

Just run:

```bash
deactivate
```

![image](https://github.com/user-attachments/assets/a61d3237-6b70-4a97-ae60-bc4c278e78bd)


---

### 📌 **Step 3: Install packages in your `venv`**

Once activated, install any packages:

```bash
pip install requests flask
```

Packages will now install **inside the `venv`**, not globally.

---

## ✅ 2️⃣ How to create a `requirements.txt`

A `requirements.txt` file **lists all the packages** your project needs — so you (or someone else) can recreate the same environment.

---

### 📌 **Step 1: Install your packages**

While your `venv` is active:

```bash
pip install <your-packages>
```

---

### 📌 **Step 2: Generate `requirements.txt`**

Run:

```bash
pip freeze > requirements.txt
```

This writes all installed packages **and their versions** into `requirements.txt`.

Example:

```
flask==3.0.2
requests==2.31.0
```

---

### 📌 **Step 3: Install from `requirements.txt` later**

To recreate the same environment on another machine:

```bash
pip install -r requirements.txt
```

---

**`apt-cache show <package>`** — displays detailed information about a Debian/Ubuntu package, like version, description, dependencies, and maintainer.
**Example:** `apt-cache show python3-pip` shows info about the `python3-pip` package.

![image](https://github.com/user-attachments/assets/279cc454-b2e4-4c77-bad7-7e4004ba2c0b)

![image](https://github.com/user-attachments/assets/f5540122-ac64-40d4-a9a6-edcd7084c851)


---
# **Python Package Installation Methods:**

![image](https://github.com/user-attachments/assets/95dd140c-0b3c-457a-8c34-49d4857a8e05)


1. **apt (Recommended for System Packages)**
   - Command: `sudo apt install python3-<package>`
   - Pros:
     * Fully integrated with system updates
     * Dependency-safe (won't break system tools)
     * Managed by Debian/Ubuntu
   - Cons:
     * Often older versions
     * Limited selection
   - Best for: Core dependencies like `python3-dev`, `python3-venv`

2. **pip in Virtual Environments (Recommended for Projects)**
   - Setup:
     ```bash
     python3 -m venv myenv
     source myenv/bin/activate
     ```
   - Install: `pip install <package>`
   - Pros:
     * Latest package versions
     * Full PyPI ecosystem access
     * Isolated from system
   - Best for: Project-specific packages (Flask, Django, etc.)

3. **pipx (For Global Tools)**
   - Setup: `sudo apt install pipx`
   - Install: `pipx install <package>`
   - Pros:
     * Isolated installations
     * Safe for global CLI tools
   - Best for: Applications like `black`, `poetry`, `youtube-dl`

4. **System-wide pip (Not Recommended)**
   - Blocked by default (PEP 668)
   - Risky alternatives:
     ```bash
     pip install --user <package>  # May still cause conflicts
     pip install --break-system-packages <package>  # Dangerous
     ```

**Key Differences:**
- Stability: `apt` > `pipx` > `pip`
- Freshness: `pip` > `pipx` > `apt`
---


# When you have **multiple Python versions**, you must be careful **which `pip` you’re using**, because each Python version has its own `pip`.

---

###  **Key idea**

* **`pip`** installs packages for **the Python version it’s linked to**.
* You can easily end up with:

  * `pip3` → for Python 3
  * `pip3.10`, `pip3.11`, etc. → for specific Python 3 versions
* Or you might be using a **virtual environment**, which has its own `pip`.

---

###  **How to check**

**1️ Check which `pip` you’re using**

```bash
which pip
which pip3
which pip3.11
```

---

**2️ Check which Python version it’s tied to**

![image](https://github.com/user-attachments/assets/4609e6b1-b3ff-484e-88a9-6a9a7fdc4629)

```bash
pip --version
```
---

** Safer way: use `python -m pip`**

The best practice is to use:

```bash
python3.11 -m pip install somepackage
```

 This guarantees that `pip` is run by **that Python interpreter**, so you know exactly where the package will go.

---

###  **Common mistake**

Installing with `sudo pip` to the system Python can break things — especially if your OS uses that Python for system tools.
**Safer:** Use a `venv` or `--user`.

---
list all installed modules we have in python:

![image](https://github.com/user-attachments/assets/2ed76dd7-2d55-4dc4-9d0d-99b29572281c)

---
# Useful Scripts:

## psutil
psutil (short for Process and System Utilities) is a cross-platform Python library for retrieving information on running processes and system resource usage.
 **simple system monitor** using `psutil`.:

✅ Shows **CPU usage**
✅ Shows **RAM usage**
✅ Shows **Disk usage**
✅ Lists **top processes by CPU usage**

---

### 🖥️ **Mini System Monitor (using `psutil`)**

```python
import psutil
import time

def show_cpu():
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")

def show_memory():
    mem = psutil.virtual_memory()
    print(f"Memory Usage: {mem.percent}% ({mem.used / (1024**3):.2f} GB used of {mem.total / (1024**3):.2f} GB)")

def show_disk():
    disk = psutil.disk_usage('/')
    print(f"Disk Usage: {disk.percent}% ({disk.used / (1024**3):.2f} GB used of {disk.total / (1024**3):.2f} GB)")

def show_top_processes(n=5):
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    # Sort by CPU percent descending
    processes = sorted(processes, key=lambda p: p['cpu_percent'], reverse=True)
    print(f"\nTop {n} Processes by CPU usage:")
    for proc in processes[:n]:
        print(f"PID: {proc['pid']}, Name: {proc['name']}, CPU%: {proc['cpu_percent']}")

def main():
    while True:
        print("="*30)
        show_cpu()
        show_memory()
        show_disk()
        show_top_processes()
        time.sleep(5)  # Refresh every 5 seconds

if __name__ == "__main__":
    main()
```

---

### ⚙️ **How to run it**

1️⃣ Save this as `monitor.py`
2️⃣ Install `psutil` if you haven’t:

```bash
pip install psutil
```

3️⃣ Run it:

```bash
python monitor.py
```

![image](https://github.com/user-attachments/assets/eb75083d-76d1-4878-a6a9-c72992285145)

---

---
## OS module:

---

 **`os`** is a **built-in Python module** for **interacting with the operating system**.
It provides tools for:

* Working with **files and directories**
* Getting or setting **environment variables**
* Running **system commands**
* Managing **paths** (along with `os.path`)

It’s cross-platform: the same code works on Windows, macOS, Linux (with minor exceptions).

---

##  **Common things you can do**

| Task                          | Example                                    |
| ----------------------------- | ------------------------------------------ |
| Get current working directory | `os.getcwd()`                              |
| Change directory              | `os.chdir('/path')`                        |
| List files in a directory     | `os.listdir('.')`                          |
| Make new directories          | `os.mkdir('new_dir')`                      |
| Remove files or directories   | `os.remove('file.txt')`, `os.rmdir('dir')` |
| Run system commands           | `os.system('ls -l')`                       |
| Get environment variables     | `os.environ['HOME']`                       |
| Join paths safely             | `os.path.join()`                           |

---
### Python script that opens Nautilus file manager for **Downloads**, **Python**, and **venv** directories:

```python
#!/usr/bin/python3
import os
import subprocess

# Directory options (customize paths if needed)
directories = {
    "Downloads": os.path.expanduser("~/Downloads"),
    "Python": os.path.expanduser("~/Desktop/Python"),  # From your Desktop list
    "venv": os.path.expanduser("~/Desktop/venv")       # From your Desktop list
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
```
The script shows a numbered menu and open Nautilus in the selected directory.

![image](https://github.com/user-attachments/assets/224ab837-f2ee-4266-808f-955b38818015)

---
