# Files:

A **file** is a resource for storing data — text, images, binary data, logs, etc. Python provides built-in functions to **create**, **read**, **write**, and **modify** files easily.

---

## 📂 **2. Basic file operations**

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

