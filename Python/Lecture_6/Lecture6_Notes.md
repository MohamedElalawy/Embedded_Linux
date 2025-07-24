# Files:

A **file** is a resource for storing data — text, images, binary data, logs, etc. Python provides built-in functions to **create**, **read**, **write**, and **modify** files easily.

---

## 📂 ** Basic file operations**

Python’s built-in `open()` function is the key:

```python
file_object = open("filename", "mode")
```

**Common modes:**

| Mode  | Description                       |
| ----- | --------------------------------- |
| `'r'` | Read (default)                    |
| `'w'` | Write (overwrites file)           |
| `'a'` | Append (adds to end)              |
| `'b'` | Binary mode (`rb`, `wb`)          |
| `'x'` | Create new file, error if exists  |
| `'+'` | Read and write (`r+`, `w+`, `a+`) |

---

## 📖 **3. Reading a file**

```python
# Example: read whole file
with open("example.txt", "r") as f:
    content = f.read()
    print(content)

# Read line by line
with open("example.txt", "r") as f:
    for line in f:
        print(line.strip())
```

`with` handles closing the file automatically.

---

## ✍️ **4. Writing to a file**

```python
# Overwrite or create
with open("example.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("Another line.")

# Append to existing file
with open("example.txt", "a") as f:
    f.write("\nAppended line.")
```

---

## 📜 **5. Working with binary files**

```python
# Write binary data
with open("image.png", "rb") as source:
    data = source.read()

with open("copy.png", "wb") as dest:
    dest.write(data)
```

---

## ⚙️ **6. Checking file existence**

Use `os` or `pathlib`:

```python
import os

if os.path.exists("example.txt"):
    print("File exists!")

# Or with pathlib
from pathlib import Path

file = Path("example.txt")
if file.is_file():
    print("File exists!")
```

---

## 🧹 **7. Closing files**

`with` handles it for you:

```python
with open("example.txt") as f:
    pass  # auto-closes

# Without `with`:
f = open("example.txt")
# do stuff
f.close()
```

---

Always use `with open(...)` — it’s safer and cleaner!

---

<img width="987" height="496" alt="image" src="https://github.com/user-attachments/assets/aefea8c6-cc68-4fe6-b5bb-54bfc9ef9558" />

---

<img width="1716" height="942" alt="image" src="https://github.com/user-attachments/assets/30930ceb-e962-4c81-8025-23c9e934fe5b" />

---
#  `try`, `except`, `else`, and `finally`

##  How it works

* **`try`**: You put code here that might raise an exception.
* **`except`**: If an exception happens in the `try` block, Python jumps here.
* **`else`**: If no exception happens, Python runs the `else` block (optional).
* **`finally`**: Runs **no matter what**, whether there was an exception or not (often used for cleanup).

---

##  Example

Here’s a **complete example**:

```python
try:
    print("Trying to open file...")
    f = open("nonexistent.txt", "r")
except FileNotFoundError:
    print("File not found! Handling exception.")
else:
    print("No exception occurred! Reading file...")
    content = f.read()
    print(content)
    f.close()
finally:
    print("This runs no matter what.")
```

**Output:**

```
Trying to open file...
File not found! Handling exception.
This runs no matter what.
```
---
## Exception hierarchy in python
<img width="2100" height="1001" alt="image" src="https://github.com/user-attachments/assets/e7424a7c-a72c-43cc-a42d-35bcdb4d70e6" />

---

Got it — here’s a quick rundown of **`py-notifier`** and how you can use it!

---

## `py-notifier`

`py-notifier` is a simple Python library to show native system notifications — so your Python script can pop up a notification on Windows, Linux, or macOS.

It’s great for quick reminders, status alerts, or just making a script more user-friendly.

---


```bash
pip install py-notifier
```

---
##  **Basic usage**

```python
from pynotifier import Notification

Notification(
    title='Process Complete',
    description='Your AVR init function was generated!',
    duration=5,  # seconds
    urgency=Notification.URGENCY_NORMAL
).send()
```

---

# `pandas`,  the powerhouse for handling tabular data (like CSVs) in Python.

---

##  **What is pandas?**

**`pandas`** is a Python library for:

* Loading and saving data (CSV, Excel, SQL, JSON…)
* Analyzing, filtering, and transforming data
* Handling missing values
* Doing stats and group operations

---

##  **Key objects**

* **`DataFrame`** → table of rows & columns (like an Excel sheet)
* **`Series`** → a single column (or row)

---

##  **Install it**

```bash
pip install pandas
```

---


# OpenCV

**OpenCV** (Open Source Computer Vision Library) is a **powerful library** for **real-time image and video processing**, computer vision, and some basic machine learning.
It’s written in C++ but has great Python bindings.

---

##  **What can you do with OpenCV?**

* Read, write, and display images and videos
* Apply filters and transformations (blur, rotate, resize)
* Detect objects (faces, eyes, cars, people)
* Track motion in video
* Work with shapes, contours, colors
* Integrate with deep learning models (e.g., YOLO, Haar cascades)

---

# wrapper & property functions

---

## ✅ **1️⃣ What is a Wrapper Function?**

A **wrapper** is a **normal function or decorator** that *wraps* another function to add or modify its behavior.

**Typical use:** Logging, timing, checking permissions, resource management.

**Example:** A simple decorator as a wrapper:

```python
def my_wrapper(func):
    def wrapped():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapped

@my_wrapper
def say_hello():
    print("Hello!")

say_hello()
```

**Output:**

```
Before function runs
Hello!
After function runs
```

➡️ The `wrapped` function is a **wrapper**: it calls the original function *and does extra work*.

---

## ✅ **2️⃣ What is a Property Function?**

A **property** in Python is a special way to control **attribute access** in classes.
You write `getter` / `setter` methods, but use them like normal attributes.

---

**Example:**

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        print("Getting celsius")
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        print("Setting celsius")
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = value

temp = Temperature(25)
print(temp.celsius)   # Calls the getter
temp.celsius = 100    # Calls the setter
```

**Output:**

```
Getting celsius
25
Setting celsius
```

➡️ Here, `@property` makes `celsius` **look like an attribute**, but it’s actually calling a function behind the scenes.

---

## ✅ ✅ **Key difference**

| Concept      | Purpose                                                                                         |
| ------------ | ----------------------------------------------------------------------------------------------- |
| **Wrapper**  | A function that *wraps* another function — usually decorators — to add or modify behavior.      |
| **Property** | A special way to expose a method like an attribute, often used in classes for safe data access. |

---

##  **Real Example with both**

Sometimes you’ll see both in use:

```python
def log_access(func):
    def wrapper(*args, **kwargs):
        print(f"Accessing {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

class Person:
    def __init__(self, name):
        self._name = name

    @property
    @log_access
    def name(self):
        return self._name

p = Person("Alice")
print(p.name)
```

✅ Here:

* `log_access` is a **wrapper decorator**
* `name` is a **property**

---
