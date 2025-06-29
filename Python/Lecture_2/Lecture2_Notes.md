
---

# **`pip`** in Python:

---

###  **What is `pip`?**

**`pip`** stands for **“Pip Installs Packages”** (it’s a recursive acronym).
It’s the **standard package manager** for Python.
You use `pip` to **install**, **upgrade**, and **uninstall** **Python packages** from the [Python Package Index (PyPI)](https://pypi.org/).

---

###  **How to check if you have `pip` installed**

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

###  **Basic `pip` commands**

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

###  **Where does `pip` install packages?**

By default, it installs to the **Python environment** you’re using —
either the **system Python**, a **virtual environment** (`venv`), or a **conda environment**.

---

###  **Best practice**

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

##  How to set up a **virtual environment** (`venv`)

###  **Step 1: Create the `venv`**

In your project folder, open a terminal or command prompt and run:

```bash
python -m venv venv
```

* `python` — runs Python.
* `-m venv` — calls the built-in module to create a virtual environment.
* `venv` — the name of the folder that will hold the virtual environment (you can name it anything, but `venv` is common).

---

###  **Step 2: Activate the `venv`**

** On macOS/Linux:**

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

###  **Step 3: Install packages in your `venv`**

Once activated, install any packages:

```bash
pip install requests flask
```

Packages will now install **inside the `venv`**, not globally.

---

##  How to create a `requirements.txt`

A `requirements.txt` file **lists all the packages** your project needs — so you (or someone else) can recreate the same environment.

---

###  **Step 1: Install your packages**

While your `venv` is active:

```bash
pip install <your-packages>
```

---

###  **Step 2: Generate `requirements.txt`**

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

###  **Step 3: Install from `requirements.txt` later**

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

###  **Mini System Monitor (using `psutil`)**

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

###  **How to run it**

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
---
 ### Python script to use gtts (Google Text-to-Speech) to convert Arabic text to speech

---


```python
from gtts import gTTS
import os

arabic_text = "مرحبًا بك في تجربة تحويل النص إلى كلام باستخدام بايثون."

tts = gTTS(text=arabic_text, lang='ar')
tts.save("arabic_speech.mp3")

print("Done! Saved as arabic_speech.mp3")

# Play the audio (Linux example using 'mpg123')
os.system("mpg123 arabic_speech.mp3")
```

---

**Steps:**

1. Install a simple MP3 player if needed:

   ```bash
   sudo apt-get install mpg123
   ```
2. Run the script:

   ```bash
   python Arabic_text_to_speach.py
   ```
![image](https://github.com/user-attachments/assets/5a0d902c-05f8-4102-824d-a29f68a020af)

---
#  **module**, **package**, and **binary** :

---

## 1️⃣ Module

* **What is it?**
  A **module** is **a single Python file** (`.py`) that contains Python code — variables, functions, classes.
* **Example:**

  ```python
  # my_module.py
  def say_hello():
      print("Hello")
  ```

  You can import it:

  ```python
  import my_module
  my_module.say_hello()
  ```

---

## 2️⃣ Package

* **What is it?**
  A **package** is a **folder** that contains a special `__init__.py` file (can be empty) plus **one or more modules or sub-packages**.
  This makes it possible to structure larger projects.
* **Example:**

  ```
  my_package/
  ├── __init__.py
  ├── module1.py
  └── module2.py
  ```

  Usage:

  ```python
  import my_package.module1
  ```

---

## 3️⃣ Binary

* **What is it?**
  A **binary** is a **compiled file** — it’s not Python source code but an executable program or compiled library (`.exe`, `.so`, `.dll`, `.bin`).
  In Python projects, you might have binaries as **compiled C extensions** or **executables installed by pip**.
* **Example:**

  * When you install `numpy`, parts of it are compiled C binaries for speed.
  * The `pip` command itself is a small binary wrapper that runs Python code.

---

# **the main use cases of `venv`**:

---

## ✅ **Main use cases of `venv`**

1. **Isolate project dependencies**

   * Keep each project’s Python packages separate.
   * Example: Project A needs `Django 2.2`, Project B needs `Django 4.2`.

2. **Avoid messing up system Python**

   * You don’t install packages globally.
   * No risk of breaking system tools that rely on the default Python.

3. **Reproducible environments**

   * You can freeze your dependencies (`pip freeze > requirements.txt`) and recreate the exact same environment on another machine.

4. **Test with different versions**

   * Easily create multiple virtual environments with different Python versions to test compatibility.

5. **Safe experimentation**

   * Try new libraries or tools without risk.
   * If something breaks, just delete the venv.

---

#  What is **`uv`**?

[`uv`](https://github.com/astral-sh/uv) is a **fast Python package manager** — it’s an **alternative to `pip`**, `virtualenv`, and `pip-tools` — **all in one**.
It’s written in Rust for high performance.

**Key features:**

* Creates virtual environments (like `venv`)
* Installs packages (like `pip`)
* Resolves and locks dependencies (like `pip-tools` or `poetry`)
* Extremely fast because it’s compiled in Rust.

---

##  **Why is `uv` considered better than `pip` (in some cases)?**

| Aspect                    | `pip`                                        | `uv`                                                  |
| ------------------------- | -------------------------------------------- | ----------------------------------------------------- |
| **Speed**                 | Pure Python → slower                         | Rust → much faster installs & dependency resolution   |
| **Dependency resolution** | `pip` resolves on the fly                    | `uv` uses a modern, robust resolver — fewer conflicts |
| **Lock files**            | Needs `pip-tools` or `poetry` for lock files | Built-in `uv pip compile` → simple locking            |
| **Virtual environments**  | Use `venv` or `virtualenv` separately        | `uv` can create & manage envs directly                |
| **Modern UX**             | `pip` is basic                               | `uv` has modern CLI design, helpful output            |

---

##  When to use **`uv`**

* You want faster installs for big projects.
* You want modern dependency resolution (reliable lock files).
* You like having `pip`, `venv`, and `pip-tools` features in **one tool**.
* You want a modern toolchain similar to what `poetry` or `hatch` offer, but faster.

---

##  When `pip` is fine

* You need the default, standard tool that works everywhere.
* You want minimal extra tools for simple scripts.
* You work in an environment where `uv` is not available yet.

---

##  Bottom line

**`pip`** is the official, standard package manager — always available.
**`uv`** is a **modern, super-fast** alternative — great for local dev if you want speed and built-in lock files.

---

---
# Built-in Functions vs Object Methods:

**Built-in Functions**

* **Example:** `len(name)`
* `len()` is a **built-in function** — it’s part of Python’s global functions that work on many types (strings, lists, tuples, etc.).
* You pass an **object** (like `name`) as an argument to the function.
* So `len(name)` returns the length of `name`.

🔹 **General-purpose:** Works on different object types, not tied to a single type.

---

**Object Methods**

* **Example:** `name.lower()`
* `.lower()` is a **method** — a function that **belongs to a specific object** type (in this case, strings).
* You call it **directly on the object**: `name.lower()`.
* This converts the string to lowercase.

🔹 **Specific-purpose:** Tied to the object’s type — `lower()` works only for strings.

---

✅ **Key difference:**

* **Built-in functions:** `len()`, `print()`, `type()`, etc. — called independently.
* **Object methods:** `.lower()`, `.append()`, `.split()` — called *on* the object.

---


---
# String
remember: python is searchable not memorizable language.

https://colab.research.google.com/drive/1jhSCMppRfMYDxlTn-sN5hAe2UVIhaGkp

https://www.w3schools.com/python/python_strings.asp

---


# `help` in Python

The `help()` function is Python’s built-in interactive help system.
It’s used to:

* Read documentation about functions, modules, classes, methods, etc.
* Quickly check what something does.
* Explore available attributes and methods.

---

## ✅ How to use `help`

**1️⃣ Get help for a built-in function**

```py
help(len)
```

→ Shows help for the `len()` function.

---

**2️⃣ Get help for a module**

```py
import os
help(os)
```

→ Shows help for the entire `os` module.

---

**3️⃣ Get help for a specific method**

```py
name = "Elalawy"
help(name.lower)
```

→ Shows help for the `.lower()` string method.

---

**4️⃣ Enter the interactive help system**
Just type:

```py
help()
```

Then you get an interactive prompt:

```
help> modules
```

or:

```
help> keywords
```

Exit with `quit`.

---

## ✅ Example

```py
>>> help(str)
```

Gives you all documentation about the `str` class and its methods.

---


# **Special Methods** in Python

* Special methods (also called **dunder methods** — short for *Double UNDERSCORE*) are **built-in hooks** that you define inside a class.
* Their names start and end with double underscores: `__like_this__`.
* Python uses them to give your objects special behaviors, like how they should be printed, compared, added, etc.

---

## 🔑 Common examples:

| Special Method | Purpose                                                                           |
| -------------- | --------------------------------------------------------------------------------- |
| `__init__`     | Called when you create a new object (the constructor).                            |
| `__str__`      | Defines what `print(object)` shows.                                               |
| `__repr__`     | Defines the “official” string representation (used in the REPL, logs, debugging). |
| `__len__`      | Called when you use `len(object)`.                                                |
| `__add__`      | Defines what happens when you do `object1 + object2`.                             |
| `__eq__`       | Defines behavior for `==` comparisons.                                            |

---

## ✅ Example:

```python
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"The book title is '{self.title}'"

    def __len__(self):
        return len(self.title)

my_book = Book("Python Basics")
print(my_book)       # Uses __str__
print(len(my_book))  # Uses __len__
```

**Output:**

```
The book title is 'Python Basics'
13
```

---


# `dir()` in Python

![image](https://github.com/user-attachments/assets/bee1f214-7c30-4151-b456-3b18f5a600ad)


* `dir()` is a **built-in function**.
* It returns a **list of all attributes** and **methods** that belong to an object.
* It’s very useful for exploring what you can do with a module, class, or variable.

---

##  How to use `dir()`

**1️⃣ Check what’s in the current scope:**

```python
dir()
```

This shows all names defined in your current script or session.

---

** See attributes/methods of an object:**

```python
name = "Python"
print(dir(name))
```

You’ll see a list like:

```
['__add__', '__class__', '__contains__', ..., 'capitalize', 'lower', 'split', ...]
```

---

** Common use:**
Developers use `dir()` with `help()` to explore:

```python
import os
print(dir(os))
```

→ Shows all functions and variables inside the `os` module.

---

# Functions
![image](https://github.com/user-attachments/assets/ae75ebc3-9e2d-42cd-94b5-e78d269381fd)

---

###  **What is a function?**

A **function** is a reusable block of code that performs a specific task.
You define it once and call (use) it whenever you want.

---

###  **Basic syntax**

```python
def function_name(parameters):
    # code block
    return value  # optional
```

---

###  **Example**

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Muhammad")   # Output: Hello, Muhammad!
```

---

###  **Returning values**

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)   # Output: 8
```

---

###  **Default parameters**

```python
def greet(name="World"):
    print(f"Hello, {name}!")

greet()          # Output: Hello, World!
greet("Alice")   # Output: Hello, Alice!
```

---

### ✅ **Keyword arguments**

```python
def power(base, exponent):
    return base ** exponent

print(power(2, 3))            # 8
print(power(exponent=3, base=2))  # 8
```

---

###  **Variable number of arguments**

* **`*args`** → accepts any number of **positional** arguments
* **`**kwargs`** → accepts any number of **keyword** arguments

```python
def show_args(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

show_args(1, 2, 3, name="Ali", age=25)
# Positional: (1, 2, 3)
# Keyword: {'name': 'Ali', 'age': 25}
```

---

###  **Lambda functions**

A short way to write small anonymous functions:

```python
add = lambda x, y: x + y
print(add(2, 3))  # 5
```

---

### In Python, when you call a function, **all positional arguments must come before keyword arguments**.
### If you mix the order, Python raises:

```
SyntaxError: positional argument follows keyword argument
```

---

###  **Example of the error**

```python
def order(item, quantity, price):
    print(f"Item: {item}, Quantity: {quantity}, Price: {price}")

#  This will raise an error:
order(item="Book", 2, price=10)
```

**Why?**
Because `item="Book"` is a keyword argument, but `2` (positional) comes *after* it.

---

###  **Correct ways**

**All positional first:**

```python
order("Book", 2, 10)
```

**Or keyword arguments after positional:**

```python
order("Book", quantity=2, price=10)
```

**Or all keyword:**

```python
order(item="Book", quantity=2, price=10)
```

---

#### default with oring:

```python
def my_function(name: str | None = "test", age=0) -> None:
    print(f"Name: {name}, Age: {age}")
    return None
```

This **defines** a function with:

* `name`: a `str` or `None` (type hint) — default is `"test"`.
* `age`: default is `0`.

---

#### Adding parameter data types good practice:


* Type hints act as built-in documentation.

* Others don’t need to guess the expected input or output.

```python
def add(x: int, y: int) -> int:
    return x + y
```


---
# variadic functions:

---

##  **What is a variadic function?**

A **variadic function** accepts **any number of arguments** — instead of a fixed number.
In Python, this is done with:

* `*args` → collects **positional arguments** into a tuple.
* `**kwargs` → collects **keyword arguments** into a dict.

---

## ✅ **Basic example**

```python
def my_variadic_function(*args):
    print(args)

my_variadic_function(1, 2, 3)
# Output: (1, 2, 3)
```

---

## ✅ **Positional and keyword**

```python
def my_variadic_function(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

my_variadic_function(1, 2, 3, name="Ali", age=22)

# Output:
# Positional: (1, 2, 3)
# Keyword: {'name': 'Ali', 'age': 22}
```

---

## ✅ \*\*Combining normal, \*args, and **kwargs**

```python
def example(a, b, *args, **kwargs):
    print(f"a: {a}, b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

example(1, 2, 3, 4, 5, name="Ali", country="Egypt")

# a: 1, b: 2
# args: (3, 4, 5)
# kwargs: {'name': 'Ali', 'country': 'Egypt'}
```

---

## ✅ **Unpacking when calling**

```python
def show(x, y, z):
    print(x, y, z)

values = (1, 2, 3)
show(*values)  # Unpacks tuple

kv = {"x": 10, "y": 20, "z": 30}
show(**kv)     # Unpacks dict
```

---

## ✅ **Why use variadic functions?**

* For flexible APIs (e.g., `print`).
* For forwarding arguments to other functions.

---

####  variadic keyword arguments (`**kwargs`) - how to properly document dictionary-style usage for users:

---

```python
def my_function(**kids) -> None:
    """
    This function accepts keyword arguments representing children's names.
    It prints the type of the 'kids' dictionary and the name of 'child1' (if provided).

    Args:
        **kids: Keyword arguments where:
            - Key: A string like 'child1', 'child2', etc.
            - Value: The child's name (e.g., 'Tobias').

    Example:
        >>> my_function(child1="Alice", child2="Tobias", child3="Linus")
        <class 'dict'>
        Alice
    """
    print(f"{type(kids)}")
    print(f"{kids.get('child1', 'No child1 provided')}")

my_function(child2="Tobias", child3="Linus")  # Output: <class 'dict'>, "No child1 provided"
```

---

### **How to Document for Users:**
To ensure users understand how to interact with the dictionary-style (`**kwargs`) function, include:  

1. **Parameter Description**:  
   - Clearly state that `**kids` accepts arbitrary keyword arguments.  
   - Describe the expected format (e.g., keys like `child1`, values as names).  

2. **Example Usage**:  
   - Show how to call the function with named arguments.  
   - Highlight handling of missing keys (e.g., `get()` with a default).  

---








