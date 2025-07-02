# Lists Module
---


##  `mypy`

`mypy` is a **static type checker** for Python. It checks your code for **type errors** *without running it*.
Python is dynamically typed by default, so types are not enforced at runtime — `mypy` helps you catch type-related bugs *before* they happen.

---

### ✅ Example

**Without type hints:**

```python
def add(x, y):
    return x + y
```
![image](https://github.com/user-attachments/assets/c9d48023-8e11-499e-9ff6-0839c7635d89)

This runs fine — but if someone calls `add(1, "2")`, Python won’t complain until it crashes at runtime.

---

**With type hints + mypy:**

```python
def add(x: int, y: int) -> int:
    return x + y
```
`mypy` will warn:

```
error: Argument 2 to "add" has incompatible type "str"; expected "int"
```
![image](https://github.com/user-attachments/assets/38ca917e-8d95-474a-9463-7b09629fd553)


---

Alright — let’s break down **global variables in Python** clearly.

---

# *global variable* in Python:

A **global variable** is a variable defined **outside of any function**. It can be accessed inside functions, but if you want to *modify* it inside a function, you must declare it `global`.

---

## ✅ Example: Read vs. Modify

### ✔️ **Reading a global variable**

```python
x = 10  # Global variable

def show():
    print(x)  # Works fine

show()  # Output: 10
```

> ✅ You can read a global variable inside a function **without `global`**.

---

### ❌ **Modifying without `global`**

```python
x = 10

def change():
    x = 20  # This creates a *local* variable named x

change()
print(x)  # Output: 10  (NOT changed!)
```

> ⚠️ Without `global`, `x` inside `change()` is treated as a new *local* variable — the global `x` is untouched.

---

### ✔️ **Modifying with `global`**

```python
x = 10

def change():
    global x  # Tell Python to use the global `x`
    x = 20

change()
print(x)  # Output: 20
```


---

| Action                 | Needs `global`? |
| ---------------------- | --------------- |
| Read global variable   | ❌               |
| Modify global variable | ✅               |

---




