1# Python Course - Goals & Applications

## Core Python Concepts
- GUI Development
- Socket Programming  
- Multi-threading  

## Python as a Foundation For
- Machine Learning  
- Data Analysis  
- Web Development (Django, etc.)  

## Key Features of Python
- Object-Oriented Programming (OOP)  
- Open Source  
- Dynamic Typing  

## Practical Applications
- Scripting  
- Automation  
- Testing  

## Modern Software Development
"Software is not just C anymore"  
Python offers versatile solutions across domains


---

The **difference between an interpreter and a compiler** lies in **how they translate and execute code** written in a programming language like Python, C, or Java.



### 🔁 Interpreter

* **Definition**: Translates and executes code **line by line**.
* **Execution**: Runs the program **directly** without creating a separate file.
* **Speed**: Slower because it translates code on the fly.
* **Error Handling**: Stops at the **first error** it encounters.
* **Examples**:

  * Python
  * JavaScript
  * Ruby
---

### ⚙️ Compiler

* **Definition**: Translates the **entire program** into machine code **before** running it.
* **Execution**: Produces a separate **executable file** (e.g., `.exe`).
* **Speed**: Faster at runtime since it's already translated.
* **Error Handling**: Shows **all errors** at once during compilation.
* **Examples**:

  * C
  * C++
  * Rust

---

### Summary Table

| Feature            | Interpreter            | Compiler              |
| ------------------ | ---------------------- | --------------------- |
| Translation method | Line by line           | Whole program at once |
| Output             | No file, just executes | Creates executable    |
| Speed              | Slower                 | Faster                |
| Error handling     | One at a time          | All at once           |
| Examples           | Python, JS             | C, C++                |

---

## Detailed breakdown of the Python interpreter process:


### Python Interpreter Execution Pipeline
![image](https://github.com/user-attachments/assets/f70ed5d7-24c0-45cf-bda2-f8b658cbf624)

#### 1. **Lexical Analysis (Lexing) <1>**
   - **What happens**: 
     - Source code (`velivelli.py`) is broken into tokens (keywords, identifiers, literals, operators).
     - Example for `print("hello world")`:
       - Tokens: `[print, (, "hello world", )]`
   - **Purpose**: 
     - Convert raw text into meaningful language components.

#### 2. **Parsing <2>**
   - **What happens**: 
     - Tokens are structured into an Abstract Syntax Tree (AST).
     - Example AST for `print("hello world")`:
       ```
       Call(func=Name(id='print'), args=[Constant(value='hello world')])
       ```
   - **Purpose**: 
     - Validate syntax and create a hierarchical execution plan.

#### 3. **Compilation <3> → Bytecode Generation**
   - **What happens**: 
     - AST is compiled into platform-independent bytecode.
     - Bytecode instructions (e.g., `LOAD_NAME`, `CALL_FUNCTION`).
     - Stored in `.pyc` files (e.g., `__pycache__/velivelli.pyc`) for reuse.
   - **Example Bytecode** (via `dis.dis`):
     ```
     0 LOAD_NAME      0 (print)
     2 LOAD_CONST     0 ('hello world')
     4 CALL_FUNCTION  1
     6 RETURN_VALUE
     ```

#### 4. **Python Virtual Machine (PVM) <4> Execution**
   - **What happens**: 
     - PVM reads bytecode line-by-line and converts it to machine-specific operations.
     - Uses a stack-based approach:
       1. Pushes `print` and `"hello world"` onto the stack.
       2. Executes `CALL_FUNCTION` to run `print()`.
   - **Purpose**: 
     - Abstracts hardware differences (cross-platform compatibility).

#### 5. **Machine Code & I/O Operations (IOIO)**
   - **Final Step**: 
     - The OS executes machine instructions.
     - Output: `hello world` appears on the terminal.

---



### Key Components
- **`.pyc` Files**: Cached bytecode for faster subsequent runs.
- **PVM**: The runtime engine (part of CPython).
- **Dynamic Nature**: No explicit "linking" step (unlike C).

---

### Why This Matters
- **Performance**: Bytecode caching avoids re-parsing.
- **Portability**: Same bytecode runs on any PVM (Windows/Linux/macOS).
- **Debugging**: Inspect bytecode with `dis` module to optimize code.
---
## Detailed explanation of the Python bytecode:

Bytecode is computer object code that an interpreter converts into binary machine code so it can be read by a computer's hardware processor.

The interpreter is typically implemented as a virtual machine (VM) that translates the bytecode for the target platform. The machine code consists of a set of instructions that the processor understands.

Bytecode is platform-independent and more efficient than source code, but not as low-level as machine-specific binary. It serves as an intermediate step in execution, enabling portability across different systems while maintaining faster performance than direct source interpretation.
![image](https://github.com/user-attachments/assets/8c1b7d14-4844-41de-94ca-0dc2e1fe4bcd)

![image](https://github.com/user-attachments/assets/039dbb8b-74d6-4dd7-8f7a-a68ac79a0f31)


---
#### **Run the disassembler**
```bash
python -m dis file.py
```
Or for interactive inspection:
```python
import dis
dis.dis(compile("x = 10; print(x)", "<string>", "exec"))
```
---
| Line # | Byte Offset | Opcode           | Argument | Description                                                                 |
|--------|-------------|------------------|-----------|-----------------------------------------------------------------------------|
| 1      | 0           | LOAD_CONST       | 0 (10)    | Loads the constant value 10 onto the stack                                  |
|        | 2           | STORE_NAME       | 0 (x)     | Stores the top of stack (10) into the variable named 'x'                   |
| 2      | 4           | LOAD_NAME        | 1 (print) | Loads the print function onto the stack                                     |
|        | 6           | LOAD_NAME        | 0 (x)     | Loads the value of variable x onto the stack                                |
|        | 8           | CALL_FUNCTION    | 1         | Calls the print function with 1 argument (consumes 2 stack items: fn and arg) |
|        | 10          | POP_TOP          | -         | Removes the top of stack (the None return value from print)                |
|        | 12          | LOAD_CONST       | 1 (None)  | Loads None onto the stack (implicit return value)                          |
|        | 14          | RETURN_VALUE     | -         | Returns the top of stack (None) to the caller                              |

---
## PVM
The **Python Virtual Machine (PVM)** is the component of the Python interpreter that **executes bytecode instructions**.

![image](https://github.com/user-attachments/assets/29344943-130e-4f7d-aaaa-b099ff274455)

it simply iterprets bytecode into machine code and executes it

---

When you run a Python program:

1. ✅ The **Python source code** (`.py` file) is **compiled** into **bytecode** (a lower-level, platform-independent representation).
2. ✅ This **bytecode** is sent to the **Python Virtual Machine (PVM)**.
3. ✅ The **PVM** interprets and executes each bytecode instruction step-by-step.

---

##  Simple Analogy

* 📝 You write Python code → `x = 10`
* 🧾 Python compiles it into bytecode → `LOAD_CONST`, `STORE_NAME`, etc.
* ⚙️ The **PVM reads those instructions** and performs the actual work → store `10` in memory as `x`.
---

## 📦 Where Is the PVM?

* The PVM is part of the **CPython** interpreter (the standard Python implementation in C).
* When you install Python from python.org or with `apt install python3`, you're using **CPython**, and it includes the PVM.

---

## Python Compiler:

![image](https://github.com/user-attachments/assets/93fda292-3d94-4126-85b4-b5335990dbbc)

### Python Implementation Variants

| Implementation | Key Characteristics |
|---------------|---------------------|
| **CPython** | Stack-based interpreter (with optional `with-pyston` or `-X cpu_count` speedups in Python 3.13+) |
| **PyPy** | Uses the same bytecode specification but adds a tracing JIT (Just-In-Time) compiler that optimizes hot loops into native machine code |
| **MicroPython / CircuitPython** | Minimalist VM with a reduced opcode set, designed to run on microcontrollers and embedded systems |
| **Jython / Graal-Python** | Translates Python bytecode into JVM bytecode, executing on the Java Virtual Machine |
| **IronPython** | Compiles Python code to the .NET Common Intermediate Language (CIL), running on the .NET CLR |

---
# Execution ways:

![image](https://github.com/user-attachments/assets/d14f02c9-9e75-44e0-a43f-c74a39567d36)

---
## OR:

![image](https://github.com/user-attachments/assets/9e8f3622-9a5d-4649-89d5-de372084aa6e)

The line:

```python
#!/usr/bin/env python3
```

is called a **shebang** (or hashbang), and it's used at the **top of a script file** to tell the operating system **how to execute the file**.

---

## ✅ What It Does

* `#!` tells the OS: "Use the program that follows to run this script"
* `/usr/bin/env python3` tells it to **find `python3` in the system’s `PATH`**

So when you make your script executable and run it like this:

```bash
./test.py
```

The OS runs:

```bash
/usr/bin/env python3 test.py
```

---

### Benefits:

* ✅ More **portable** across systems (Windows Subsystem for Linux, macOS, various Linux distros)
* ✅ Uses the **first `python3`** found in the user’s `PATH`, which might be a virtualenv or custom install

---
# The difference between `main.py` and `main.c` lies at the **core of how interpreted and compiled languages work**, and it shows clearly how **Python (dynamic + portable)** and **C (static + target-specific)** differ in their execution models.


---

## 🧾 1. Basic Nature

| Aspect            | `main.py` (Python)                          | `main.c` (C)                            |
| ----------------- | ------------------------------------------- | --------------------------------------- |
| **Language Type** | Interpreted                                 | Compiled                                |
| **Extension**     | `.py`                                       | `.c`                                    |
| **Execution**     | Run through an interpreter (e.g. Python VM) | Must be compiled into machine code      |
| **Portability**   | High (runs on any machine with Python)      | Low (must be compiled per architecture) |

---

## 🛠️ 2. What Happens When You Run Each One

### ➤ `main.py` (Python)

You write:

```python
print("Hello from Python!")
```

When you run it:

```bash
python3 main.py
```

Under the hood:

1. Python **compiles the source code to bytecode** (`main.pyc`).
2. The **Python Virtual Machine (PVM)** interprets the bytecode line by line.
3. The bytecode is **platform-independent** — it can run on any machine that has a Python interpreter.

✅ **It works anywhere** — Windows, macOS, Linux, Raspberry Pi — as long as Python is installed.

---

### ➤ `main.c` (C)

You write:

```c
#include <stdio.h>
int main() {
    printf("Hello from C!\n");
    return 0;
}
```

To run it, you must **compile it**:

```bash
gcc main.c -o main
./main
```

Under the hood:

1. `main.c` is compiled by `gcc` (or another compiler) into **machine code** for your CPU (e.g., x86\_64).
2. The generated binary (e.g. `main.exe` or `main.out`) is **architecture- and OS-specific**.

   * Linux x86 binary won’t run on Windows.
   * ARM binary won’t run on x86.

❌ **It is not portable** — must be **recompiled for each target**.

---

## 🖥️ 3. Portability Explained

| Question                                           | Python (`main.py`)                | C (`main.c`)                                    |
| -------------------------------------------------- | --------------------------------- | ----------------------------------------------- |
| Can I run it directly on Linux, Windows, or macOS? | ✅ Yes, same file                  | ❌ No, must recompile                            |
| Can I send this file to a friend on another OS?    | ✅ Yes, just install Python        | ❌ No, you must send a binary built for their OS |
| Does it contain CPU-specific instructions?         | 🚫 No (uses bytecode)             | ✅ Yes (compiled to machine code)                |
| What makes it run?                                 | Python interpreter (`python.exe`) | Native OS and CPU                               |

---

## ⚙️ 4. Why `main.py` is Portable

Because of:

1. **Interpreted Nature** – Python doesn’t need to be compiled to native machine code first.
2. **Python Virtual Machine (PVM)** – handles platform differences internally.
3. **Dynamic Typing and Late Binding** – Python checks types and does linking at runtime.

---

## 🔩 5. Why `main.c` Must Be Built for Each Target

Because:

1. C is **compiled to native machine instructions** (like MOV, ADD, etc. for Intel or ARM).
2. The generated binary depends on:

   * CPU architecture (x86, ARM, RISC-V…)
   * OS conventions (syscalls, dynamic libraries, file formats like ELF or PE)
3. Each platform has **different ABIs (Application Binary Interfaces)**.

---

## 🔧 Example: Compilation Targets

| Platform           | `main.py`                 | `main.c` (compiled binary)               |
| ------------------ | ------------------------- | ---------------------------------------- |
| Linux x86\_64      | ✅ Works (with Python)     | ✅ Works if compiled on/for Linux x86\_64 |
| Windows x86\_64    | ✅ Works (with Python)     | ❌ Won’t work unless recompiled           |
| Raspberry Pi (ARM) | ✅ Works (with Python ARM) | ❌ Must recompile for ARM                 |
| macOS              | ✅ Works (with Python)     | ❌ Must recompile for macOS               |

---

## 🧪 Summary Table

| Feature                | Python (`main.py`)      | C (`main.c`)                   |
| ---------------------- | ----------------------- | ------------------------------ |
| Language Type          | Interpreted             | Compiled                       |
| Output                 | Bytecode executed by VM | Machine code executed directly |
| Portability            | High (cross-platform)   | Low (platform-dependent)       |
| Needs Compilation      | No (optional `.pyc`)    | Yes (always)                   |
| Requires Runtime       | Python Interpreter      | Native OS & CPU                |
| Architecture Dependent | No                      | Yes                            |
| OS Dependent           | No                      | Yes                            |

---

## 🧠 Real-World Implication

* Python is excellent for **scripts, automation, portability**, and **cross-platform development**.
* C is excellent for **performance**, **low-level hardware control**, and **embedded systems** — but requires **platform-specific builds**.

---
# raw string in detail.

---

## 🧵 What Is a Raw String in Python?

A **raw string** is a string **where backslashes (`\`) are treated as literal characters**, not as escape characters.

You write a raw string by prefixing the string with `r` or `R`:

```python
normal_str = "C:\\Users\\Muhammad"
raw_str = r"C:\Users\Muhammad"
```

Both result in the same string **visually**, but the **interpretation** differs.

---

### 📌 Why Use Raw Strings?

Because in **normal strings**, backslashes are used for **escape sequences**, like:

| Escape | Meaning             |
| ------ | ------------------- |
| `\n`   | Newline             |
| `\t`   | Tab                 |
| `\\`   | Backslash           |
| `\"`   | Quote inside string |

This can make file paths or regular expressions very hard to read.

### 🧪 Example

```python
print("C:\\Users\\Muhammad")  # Normal string
print(r"C:\Users\Muhammad")   # Raw string
```

Both will print:

```
C:\Users\Muhammad
```

But raw string is easier to write.

---

### 🧬 Where Are Raw Strings Useful?

#### ✅ File Paths

```python
path = r"C:\new_folder\test\name.txt"
```

#### ✅ Regular Expressions

```python
import re
pattern = r"\d+\.\d+"   # Matches a float like "123.45"
re.match(pattern, "123.45")
```

If you didn’t use `r""`, you'd have to write `\\d+\\.\\d+`.

---

### ⚠️ Raw Strings Still Use Quotes

```python
r"Hello\nWorld"   # Output: Hello\nWorld (literally, not a newline)
```

Raw strings **don’t escape the backslash**, but still require:

* **Quotes**
* Proper syntax (e.g. `r"abc\"` is invalid because `\"` ends the string)

---

### ⚠️ Caveat

Raw strings **cannot end with an odd number of backslashes**:

```python
r"C:\new_folder\"     # ❌ SyntaxError!
```

You need to double the final backslash:

```python
r"C:\new_folder\\"    # ✅ Works fine
```

---

## ✅ Summary

| Concept         | Explanation                                 |
| --------------- | ------------------------------------------- |
| Raw String      | A string that treats backslashes as literal |
| Syntax          | Prefix with `r` or `R` (e.g. `r"..."`)      |
| Best Use Cases  | File paths, regular expressions             |
| Escape behavior | No escape sequences (e.g., `\n` stays `\n`) |

---


Yes, in Python, **everything is an object** — and this is one of the core design principles of the language.

---

## 🧱 What Does "Everything Is an Object" Mean?

It means **every value in Python** — whether it's a number, string, function, class, list, or even `None` — is an **instance of some class**, and therefore an **object** with associated **attributes** and **methods**.

---

### 🔍 Example 1: Integers Are Objects

```python
x = 10
print(type(x))        # <class 'int'>
print(x.bit_length()) # 4
```

Even `10` is an object of class `int`, and it has methods like `.bit_length()`.

---

### 🔍 Example 2: Functions Are Objects

```python
def greet():
    print("Hello!")

print(type(greet))     # <class 'function'>
greet.name = "Greeter" # You can even attach attributes
```

Functions are **first-class objects** in Python. You can:

* Assign them to variables
* Pass them as arguments
* Return them from other functions
* Add custom attributes

---

### 🔍 Example 3: Classes Are Objects

```python
class MyClass:
    pass

print(type(MyClass))     # <class 'type'>
```

Even your class definition is an **object** of type `type`.

---

### 🔍 Example 4: None Is an Object

```python
print(type(None))    # <class 'NoneType'>
```

---

## 🧠 Why Is This Powerful?

Because of this model, Python has:

* **Duck typing**: If it walks like a duck and quacks like a duck...
* **Dynamic introspection**: You can inspect or modify objects at runtime.
* **Flexible design patterns**: Functions, classes, and even modules can be passed around or manipulated.
* **Metaprogramming**: You can change class behavior dynamically.

---

## 🧬 Internals: Objects and Classes

When you write:

```python
x = 5
```

Under the hood:

* `x` is a **name** (reference).
* `5` is an **object** (instance of `int`).
* The variable `x` points to that object.

Even operators are just syntactic sugar for method calls:

```python
x + y   →   x.__add__(y)
x < y   →   x.__lt__(y)
```

---


# 🧹 Python's Garbage Collector

## …and why Python isn't always ideal for memory-critical applications.

---

## 📌 What Is Garbage Collection?

**Garbage collection (GC)** is the process of **automatically freeing memory** that is no longer being used by the program. This helps avoid memory leaks and reduces manual memory management errors.

In **Python**, this is handled by the **`gc` module** and the **reference counting mechanism** built into the CPython interpreter (the default Python implementation).

---

## 🧠 How Python's Garbage Collection Works

Python mainly uses **two techniques**:

### 1. **Reference Counting**

* Every object in Python keeps a count of how many references point to it.
* When that count drops to 0, the object is **immediately deleted**.

```python
a = []
b = a  # ref count = 2
del a  # ref count = 1
del b  # ref count = 0 → memory is freed
```

### 2. **Cycle Detector**

* Reference counting **fails** with **circular references**:

```python
a = []
b = [a]
a.append(b)
```

* This creates a loop; neither `a` nor `b` can be freed by ref counting alone.
* Python's **garbage collector** (in `gc` module) detects and breaks these cycles.

---

## 🧼 The `gc` Module

You can interact with it manually:

```python
import gc

gc.collect()     # Manually trigger garbage collection
gc.disable()     # Turn off automatic GC
gc.get_stats()   # Get GC stats
```

---

## ⚠️ Why Python Isn't Great for Memory-Critical Applications

### 1. **High Memory Overhead**

* Even small integers, strings, and basic objects in Python carry **metadata** (like ref counts and type info).
* Example: A single integer can use **24+ bytes**, whereas in C it’s just **4 bytes**.

### 2. **Lack of Manual Memory Control**

* In C/C++, you have `malloc` and `free` (or `new`/`delete`) to control allocation.
* Python abstracts memory away — **you can’t control it precisely**.

### 3. **Garbage Collection Pause**

* The cycle detector can pause execution for a brief moment.
* This can cause **latency** in real-time or high-performance applications (e.g., games, trading systems).

### 4. **Fragmentation**

* Python's memory allocator (`pymalloc`) can lead to **heap fragmentation**, especially with many short-lived objects.

### 5. **Hidden Object Creation**

* Python creates many **temporary and intermediate objects**, especially with dynamic typing.

Example:

```python
a = [1, 2, 3]
b = sum(a)  # multiple internal objects are created during this operation
```

---

## 🛠️ Where This Matters

Python is **not the best choice** for:

| Use Case                   | Why Not Python                        |
| -------------------------- | ------------------------------------- |
| Embedded Systems           | Limited RAM/CPU; need precise control |
| Real-time Systems (RTOS)   | GC pauses and high-level abstractions |
| Large-scale Gaming Engines | High memory and performance needs     |
| Low-level drivers/firmware | Python can’t run there at all         |

---

## ✅ But Why Python Is Still Amazing

* **Easy to use and read**
* Great for **rapid development**
* Has tons of **libraries and frameworks**
* Ideal for **data science, automation, scripting, and web backends**

For memory-critical apps, people often:

* Use **C/C++ modules** in performance-critical parts
* Use **PyPy**, which has a better garbage collector
* Use **Cython** to convert Python to C-level code

---

## ✅ Summary

| Topic                 | Python Behavior                                   |
| --------------------- | ------------------------------------------------- |
| Memory management     | Automatic (ref count + cycle detection)           |
| Manual control        | ❌ No (unlike C/C++)                               |
| Memory efficiency     | ❌ High overhead                                   |
| Real-time suitability | ❌ Not ideal                                       |
| Flexibility/Ease      | ✅ Excellent for most general-purpose applications |

---

# Python Data types:

![image](https://github.com/user-attachments/assets/8e0bfcb2-e12d-4e98-98fd-dbec3917565b)

# convert string to list:
![image](https://github.com/user-attachments/assets/835766a2-f3fa-4630-85cf-2375b61778e2)

---

## 🧠 Main Python Data Types:

### 1. **Numeric Types**

Used to store numbers.

#### a. `int` (Integer)

Whole numbers (positive or negative)

```python
a = 10
b = -5
```

#### b. `float` (Floating-point)

Decimal or fractional numbers

```python
pi = 3.14
g = -9.81
```

#### c. `complex` (Complex Number)

Numbers with real and imaginary parts

```python
z = 2 + 3j
```

---

### 2. **Dictionary**

Stores key-value pairs.
Mutable and unordered.

```python
person = {"name": "Alice", "age": 25}
print(person["name"])  # Output: Alice
```

---

### 3. **Boolean**

Represents truth values: `True` or `False`
Often used in conditions.

```python
print(10 > 9)        # True
print(bool("Hello")) # True
print(bool(15))      # True
print(10 > 9)        # True
print(1 > 2)         # False
print(bool("Hello")) # True
print(bool(15))      # True
print(bool(False))   # False
print(bool(None))    # False
print(bool(0))       # False (line 10 had '@' which was invalid, replaced with 0)
print(bool(""))      # False (empty string)
print(bool(()))      # False (empty tuple)
print(bool([]))      # False (empty list)
print(bool({}))      # False (empty set/dict - fixed from second empty tuple)
```
![image](https://github.com/user-attachments/assets/8fe63fdd-5270-4e21-8987-dae4fa0ba665)


---

### 4. **Set**

Unordered collection of unique elements

```python
fruits = {"apple", "banana", "apple", "orange"}
print(fruits)  # Output: {'apple', 'banana', 'orange'}
```
Ah, got it! Here's the explanation and code for using **sets with tree** and **sets with hashmap** in **Python**:

---

## ✅ Set Using Hashmap (Default `set`)

Python’s built-in `set` is implemented using a **hash table** (hashmap).

### 🔹 Characteristics:

* **Unordered** (insertion order preserved in Python 3.7+)
* **Very fast** lookups: average **O(1)** for add, remove, and check
* Automatically **removes duplicates**

### ✅ Example:

```python
s = set()
s.add(10)
s.add(5)
s.add(20)
s.add(10)  # Duplicate, won't be added again

print(s)  # Output (unordered): {10, 20, 5}
print(5 in s)  # True
```

---

## 🌳 Set Using Tree (Using `SortedContainers` or `bisect`)

Python does not have a built-in tree-based set, but you can use the third-party library `sortedcontainers` or the built-in `bisect` module to simulate it.

### 🔹 Option 1: Using `SortedSet` from `sortedcontainers`

(Install using `pip install sortedcontainers`)

```python
from sortedcontainers import SortedSet

tree_set = SortedSet()
tree_set.add(10)
tree_set.add(5)
tree_set.add(20)

print(tree_set)  # Output: SortedSet([5, 10, 20])
print(10 in tree_set)  # True
```

* **Sorted** automatically
* Backed by a **balanced tree**
* Insertion/removal/search: **O(log n)**

---


---

## 🔚 Summary

| Feature     | `set` (Hashmap)           | `SortedSet` (Tree)           |
| ----------- | ------------------------- | ---------------------------- |
| Ordering    | No (insertion order only) | Yes (sorted)                 |
| Lookup Time | O(1) average              | O(log n)                     |
| Best For    | Fast lookup               | Ordered data, range queries  |
| Module      | Built-in                  | `sortedcontainers` or custom |

---

### 5. **Sequence Types**

Ordered collection of items.

#### a. `str` (String)

Immutable sequence of Unicode characters

```python
message = "Hello, World!"
print(message[0])  # Output: H
```
![image](https://github.com/user-attachments/assets/53cc11c8-44cf-4b85-be58-55b32a2d8662)


#### b. `list`

Mutable sequence of items

```python
numbers = [1, 2, 3, 4]
numbers.append(5)
```
![image](https://github.com/user-attachments/assets/26d5fa21-3d5a-4a16-8f6c-dfccdd3e824c)


#### c. `tuple`

Immutable sequence of items

```python
coordinates = (10.0, 20.0)
```
![image](https://github.com/user-attachments/assets/f4b0301b-0d0a-47a2-93a1-d8bf8dc03638)


---

## 📌 Notes:

* Python is **dynamically typed**, meaning you don't need to declare types explicitly.
* Everything in Python is an **object**.

---

## 🛠️ Example Program (All Data Types)

```python
# Numeric
a = 42          # int
b = 3.14        # float
c = 2 + 5j      # complex

# Boolean
is_valid = True

# Dictionary
student = {"name": "Laila", "grade": "A"}

# Set
unique_numbers = {1, 2, 3, 2}

# Sequence Types
text = "Python"          # String
items = [1, "a", 3.5]    # List
point = (5, 9)           # Tuple

print(type(a), type(text), type(student))

```
![image](https://github.com/user-attachments/assets/61ac8e97-ae84-459e-9fef-850944c8036f)

### Use sets for membership tests (e.g., x in collection) when dealing with large datasets.
### Use lists when order matters or duplicates are needed.
![image](https://github.com/user-attachments/assets/a8e37316-30fb-4d4c-afec-d7c5b55bdea5)

---

## slicing

```python
x = ["moatasem", 1, 2.5, 3, 4, 5, 8, 9]  # Single-level list with 8 elements

x[1] = 55  # Replaces the second element (index 1) from 1 to 55

print(x[0])    # Prints first element: "moatasem"
print(x[1])    # Prints second element (now 55): 55

# Slicing operations:
print(x[1:3])  # Prints elements from index 1 to 2 (exclusive 3): [55, 2.5]
print(x[-1])   # Prints last element: 9
print(x[-2])   # Prints second last element: 8
print(x[2:])   # Prints from index 2 to end: [2.5, 3, 4, 5, 8, 9]
print(x[1:4:2]) # Prints every 2nd element from index 1 to 3: [55, 3] (indices 1 and 3)
```
![image](https://github.com/user-attachments/assets/c19b96ff-b1c1-414e-b133-9e83a6ee483c)

![image](https://github.com/user-attachments/assets/568d9c29-be44-4187-9d22-10c699bd246c)

# Operators:
---

## 🔢 1. **Arithmetic Operators**

Used for basic math operations.

| Operator | Description         | Example  | Result |
| -------- | ------------------- | -------- | ------ |
| `+`      | Addition            | `5 + 2`  | `7`    |
| `-`      | Subtraction         | `5 - 2`  | `3`    |
| `*`      | Multiplication      | `5 * 2`  | `10`   |
| `/`      | Division (float)    | `5 / 2`  | `2.5`  |
| `//`     | Floor Division      | `5 // 2` | `2`    |
| `%`      | Modulus (remainder) | `5 % 2`  | `1`    |
| `**`     | Exponentiation      | `2 ** 3` | `8`    |

---

## 🧮 2. **Assignment Operators**

Used to assign and update values.

| Operator | Example   | Equivalent To   |
| -------- | --------- | --------------- |
| `=`      | `x = 5`   | Assign 5 to `x` |
| `+=`     | `x += 2`  | `x = x + 2`     |
| `-=`     | `x -= 2`  | `x = x - 2`     |
| `*=`     | `x *= 2`  | `x = x * 2`     |
| `/=`     | `x /= 2`  | `x = x / 2`     |
| `//=`    | `x //= 2` | `x = x // 2`    |
| `%=`     | `x %= 2`  | `x = x % 2`     |
| `**=`    | `x **= 2` | `x = x ** 2`    |

---

## 🔍 3. **Comparison Operators**

Used to compare values.

| Operator | Description      | Example  | Result  |
| -------- | ---------------- | -------- | ------- |
| `==`     | Equal            | `5 == 5` | `True`  |
| `!=`     | Not equal        | `5 != 3` | `True`  |
| `>`      | Greater than     | `5 > 3`  | `True`  |
| `<`      | Less than        | `5 < 3`  | `False` |
| `>=`     | Greater or equal | `5 >= 5` | `True`  |
| `<=`     | Less or equal    | `5 <= 4` | `False` |

---

## 🔗 4. **Logical Operators**

Used to combine conditional statements.

| Operator | Description         | Example          | Result  |
| -------- | ------------------- | ---------------- | ------- |
| `and`    | True if both True   | `True and False` | `False` |
| `or`     | True if one is True | `True or False`  | `True`  |
| `not`    | Inverts the result  | `not True`       | `False` |

---

## 🧠 5. **Identity Operators**

Compare **memory location**, not value.

| Operator | Description           | Example      | Result       |
| -------- | --------------------- | ------------ | ------------ |
| `is`     | Same object in memory | `x is y`     | `True/False` |
| `is not` | Not same object       | `x is not y` | `True/False` |

> Note: `is` is not for value comparison. Use `==` for that.

![image](https://github.com/user-attachments/assets/3b15ed53-2039-463f-86fa-950f089a84e8)

---

## 📦 6. **Membership Operators**

Check if value is in sequence (like list, string).

| Operator | Description           | Example            | Result |
| -------- | --------------------- | ------------------ | ------ |
| `in`     | Found in sequence     | `'a' in 'cat'`     | `True` |
| `not in` | Not found in sequence | `'x' not in 'cat'` | `True` |


---

## 🧮 7. **Bitwise Operators**

Operate at the **binary level** (bit-by-bit).

| Operator | Name        | Example  | Binary        | Result                |        |        |            |
| -------- | ----------- | -------- | ------------- | --------------------- | ------ | ------ | ---------- |
| `&`      | AND         | `5 & 3`  | `0101 & 0011` | `0001` = 1            |        |        |            |
| \`       | \`          | OR       | \`5           | 3\`                   | \`0101 | 0011\` | `0111` = 7 |
| `^`      | XOR         | `5 ^ 3`  | `0101 ^ 0011` | `0110` = 6            |        |        |            |
| `~`      | NOT         | `~5`     | `~0101`       | `-6` (2's complement) |        |        |            |
| `<<`     | Left Shift  | `5 << 1` | `0101 → 1010` | 10                    |        |        |            |
| `>>`     | Right Shift | `5 >> 1` | `0101 → 0010` | 2                     |        |        |            |

---

## ✅ Operator Precedence (Simplified)

| Precedence  | Operators                                    |    |
| ----------- | -------------------------------------------- | -- |
| 1 (Highest) | `()` (parentheses)                           |    |
| 2           | `**`                                         |    |
| 3           | `+`, `-` (unary), `~`                        |    |
| 4           | `*`, `/`, `//`, `%`                          |    |
| 5           | `+`, `-` (binary)                            |    |
| 6           | `<<`, `>>`                                   |    |
| 7           | `&`                                          |    |
| 8           | `^`                                          |    |
| 9           | \`                                           | \` |
| 10          | `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `in` |    |
| 11          | `not`                                        |    |
| 12          | `and`                                        |    |
| 13          | `or`                                         |    |

---

![image](https://github.com/user-attachments/assets/36064f51-28bb-4288-926f-99db2a700bc7)

![image](https://github.com/user-attachments/assets/7b761c22-a63f-416f-91f3-4811adf531bb)

![image](https://github.com/user-attachments/assets/3b15ed53-2039-463f-86fa-950f089a84e8)

![image](https://github.com/user-attachments/assets/a1ae274b-aa78-46b0-8ddb-4aa54a7aa9c7)

![image](https://github.com/user-attachments/assets/360f73b0-d8b3-4af7-b703-ffef1fa9c34f)

### **Explanation of Mutable vs. Immutable Types in Python**

This code demonstrates the difference between **mutable** (modifiable) and **immutable** (unmodifiable) types in Python, focusing on **memory addresses**, **value comparison (`==`)**, and **object identity (`is`)**.

---

### **Part 1: Mutable Objects (Lists)**
#### **Key Observations:**
1. **Different Memory Addresses (`id(a) != id(b)`)**  
   - Lists are **mutable**, so Python creates **separate objects** even if their contents are identical.  
   - Modifying `a` (e.g., `a.append(2)`) won’t affect `b`.

2. **`==` vs. `is`**  
   - `==` checks **value equality** (`[1] == [1]` → `True`).  
   - `is` checks **object identity** (since `a` and `b` are distinct, `False`).

---

### **Part 2: Immutable Objects (Integers)**
#### **Key Observations:**
1. **Same Memory Address (`id(a) == id(b)`)**  
   - Small integers (like `1`) are **interned** (cached) by Python for optimization.  
   - Both `a` and `b` point to the **same `1` object** in memory.

2. **`is` Returns `True`**  
   - Since `a` and `b` reference the **identical interned object**, `is` evaluates to `True`.

---

### **Why the Difference?**
| Feature          | Mutable (e.g., `list`) | Immutable (e.g., `int`) |
|------------------|-----------------------|------------------------|
| **Memory**       | Unique objects        | Shared (interned)      |
| **Modifiable**   | Yes (e.g., `a.append(2)`) | No (e.g., `a += 1` creates a new object) |
| **`is` Behavior**| `False` (new objects) | `True` (shared objects) |

---

### **Garbage Collector’s Role**
- **Mutable Objects:** Garbage collector frees memory when variables (`a`, `b`) are deleted or go out of scope.  
- **Immutable Objects:** Small integers are **never garbage-collected** due to interning (they’re permanently cached).  

---

### **Practical Implications**
1. Use `==` to compare **values**.  
2. Use `is` to check if two variables reference the **exact same object** (useful for `None`, `True`, `False`, or interned integers).  
3. Avoid `is` with mutable objects unless you explicitly need identity checks.  

This behavior highlights Python’s trade-offs between **memory efficiency** (interning) and **flexibility** (mutable objects).

![image](https://github.com/user-attachments/assets/ee490a59-8d13-43e0-9a53-e4b9b8a5e626)

![image](https://github.com/user-attachments/assets/670892a6-d8b8-420f-9af9-a1e85a912e7c)

![image](https://github.com/user-attachments/assets/799a896c-9473-4e6f-9c0b-254971e2567e)


### **Explanation of Memory Address Changes for `a = 1` and `a = 2`**

This code demonstrates how Python handles **immutable integers** in memory, particularly focusing on:  
1. **Memory addresses (`id()`)**  
2. **Interning of small integers**  
3. **Why reassignment changes the memory address**  

---

### **Key Observations**
1. **Different Memory Addresses for `1` and `2`**  
   - Each integer (`1`, `2`) is stored at a **unique memory location**.  
   - When `a` is reassigned from `1` to `2`, `id(a)` changes because `2` is a **different object** in memory.

2. **Interning of Small Integers**  
   - Python **interns** (caches) small integers (typically `-5` to `256`) for optimization.  
   - Both `1` and `2` are interned, so their memory addresses are **constant during the program’s execution**.  
     - If you run `a = 1` and `b = 1` elsewhere, `id(a) == id(b)` will be `True`.

3. **Immutability of Integers**  
   - Integers are **immutable**. Reassigning `a = 2` doesn’t modify the original `1`; it creates a **new reference** to `2`.  
   - The original `1` remains in memory (if other references exist) but is **no longer tied to `a`**.

---

### **Why Does This Happen?**
| Step | Action            | Memory Behavior                                                                 |
|------|-------------------|---------------------------------------------------------------------------------|
| 1    | `a = 1`           | `a` points to the interned `1` at address `140726999139240`.                    |
| 2    | `print(id(a))`    | Outputs the address of the interned `1`.                                        |
| 3    | `a = 2`           | `a` now points to the interned `2` at a **new address** (`140726999139272`).   |
| 4    | `print(id(a))`    | Outputs the address of the interned `2`.                                        |

---

### **Garbage Collector’s Role**
- The integer `1` **is not garbage-collected** after `a = 2` because:  
  - It’s interned (Python keeps it alive for potential reuse).  
  - If no other variables reference `1`, it remains in memory but is **eligible for cleanup** (though interning makes this rare for small integers).  

---

### **Contrast with Mutable Objects**
For comparison, **mutable objects** (like lists) behave differently:
```python
a = [1]
print(id(a))  # Address X
a = [2]      # Reassignment creates a NEW list object.
print(id(a))  # Address Y (different from X)
```
- Unlike integers, lists are **never interned**, so each `[]` creates a new object.  

---

### **Key Takeaways**
1. **Immutable objects** (`int`, `str`, `tuple`) cannot be modified in-place; reassignment creates a new object.  
2. **Small integers** are interned, so their memory addresses are reused across variables.  
3. **`id()` changes** when reassigning to a new value because the variable points to a different object.  

**Example: Interning in Action**  
```python
x = 1
y = 1
print(x is y)  # True (same interned object)

x = 257
y = 257
print(x is y)  # False (not interned, new objects)
``` 

This behavior ensures Python balances **performance** (via interning) with **memory efficiency**.

---

# IF:

![image](https://github.com/user-attachments/assets/35bce83f-2828-4b44-8c88-ef2fe0ce3ab5)

![image](https://github.com/user-attachments/assets/9af93bc9-7219-4377-aa3d-9fbc7d91373e)

The logic flow is:
   - First check if `a > b` → print "A"
   - Else check if `a == b` → print "="
   - Else → print "B"

---
Great! You're looking at a Python snippet that uses both `pass` and the ellipsis (`...`). Let's explain both in detail and their differences.

---

## 🔹 `pass` Statement

### ✅ Purpose:

`pass` is a **null operation** — it does nothing. It's used when a statement is syntactically required but you don't want to execute any code.

### 🧠 Use Cases:

* Placeholder for future code
* Creating empty classes/functions
* Inside conditionals or loops when no action is needed yet

### 🔍 Example:

```python
def main():
    pass  # I will implement this function later
```

---

## 🔹 `...` (Ellipsis Object)

### ✅ Purpose:

Ellipsis (`...`) is an actual Python object: `Ellipsis`. It's mostly used as a **placeholder**, just like `pass`, but with **slightly different behavior**.

### 🧠 Use Cases:

* Placeholder in incomplete functions
* Used in **NumPy** for advanced indexing
* Helps tools like linters or IDEs distinguish placeholders from empty code

### 🔍 Example:

```python
def main():
    ...  # equivalent to Ellipsis
```

You can even assign it:

```python
x = ...
print(x)  # Output: Ellipsis
```

---

## ⚖️ Difference Between `pass` and `...`

| Feature     | `pass`                         | `...` (Ellipsis)          |
| ----------- | ------------------------------ | ------------------------- |
| Type        | Statement                      | Expression / Object       |
| Output      | Does nothing                   | Returns `Ellipsis`        |
| Syntax role | Only used in empty code blocks | Can be used as expression |
| Used in     | Any block needing placeholder  | Same, plus NumPy indexing |
| Example     | `if x: pass`                   | `if x: ...`               |

---

## 🧪 Your Code Explanation

```python
flag = True

if flag:
    pass          # placeholder, does nothing

# commented out:
# def main():
#     pass

def main():
    ...           # also a placeholder

print("Hello, World!")
```

This is just a **skeleton program** where you're defining placeholders and printing `"Hello, World!"`.

---

✅ **Conclusion:**
Use `pass` when you want to "skip" a block of code. Use `...` when you want to signal a **future implementation**, especially in modern code or with tools like linters or documentation generators.


