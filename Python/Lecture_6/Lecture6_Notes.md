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

