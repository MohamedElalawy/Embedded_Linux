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

# lambda expression

A **lambda expression** (or **lambda function**) is a **small anonymous function** — that means it doesn’t have a name like a normal function defined with `def` in Python or similar constructs in other languages.

Here’s a **basic example in Python**:

```python
# Normal function
def add(x, y):
    return x + y

# Equivalent lambda expression
add_lambda = lambda x, y: x + y

print(add_lambda(2, 3))  # Output: 5
```

**Key points about lambda expressions:**

* They can have **any number of arguments**, but only **one expression**.
* They return the result of that expression automatically.
* They are often used for **short, simple functions**, especially when passing as arguments to higher-order functions like `map()`, `filter()`, or `sorted()`.

---

**Example uses:**

```python
# Using lambda with map()
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16]

# Using lambda with filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]

# Using lambda with sorted()
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
pairs.sort(key=lambda x: x[1])
print(pairs)  # [(1, 'one'), (3, 'three'), (2, 'two')]
```

---



# 📌 1️⃣ What does `import` do?

When you write:

```python
import math
```

Python:

* Searches for a **module** named `math` (either a built-in module, a `.py` file, or a package directory).
* Loads its **compiled bytecode** (or compiles the source to bytecode if needed).
* Creates a **module object**.
* Binds the module object to the name `math` in your namespace.

---

## 📌 2️⃣ How does Python find the module?

Python uses the **module search path**, defined by:

```python
import sys
print(sys.path)
```

`sys.path` is a list of directories that Python searches **in order**:

1. The script’s **directory**.
2. The **PYTHONPATH** environment variable (if set).
3. Standard **site-packages** directories.
4. Built-in modules.

---

## 📌 3️⃣ How does Python execute the module?

When Python finds the `.py` file:

* It **compiles** it to bytecode (`.pyc` in `__pycache__`).
* Executes it **once** (defines functions, classes, variables).
* Stores the module in `sys.modules` **cache**.

Next time you `import` the same module in the same process, Python uses the **cached copy** instead of re-executing the file.

---

## 📌 4️⃣ Import variations

✅ **Full module import**:

```python
import os
print(os.path)
```

✅ **Selective import**:

```python
from math import sqrt
```

This imports only `sqrt` **into your namespace**.

✅ **Alias**:

```python
import numpy as np
```

✅ **Package imports**:
A directory with `__init__.py` is a **package**:

```plaintext
mypackage/
  __init__.py
  module1.py
```

You can do:

```python
from mypackage import module1
```

---

## 📌 5️⃣ The `__import__` function

Internally, `import` is just **syntax sugar** for:

```python
__import__('math')
```

But you almost never call this directly — it’s what the interpreter uses.

---

## 📌 6️⃣ Relative imports (in packages)

Inside packages, you can use **relative imports**:

```python
from . import sibling_module
from .. import parent_package_module
```

---

# importing in Python is *not* the same as literally copying the code into your file:

---

### 🔍 ✅ What actually happens?

When you do:

```python
import mymodule
```

Python does **not** paste the text of `mymodule.py` into your file.
Instead:
1️⃣ Python **runs** `mymodule.py` *once* (if it hasn’t been imported before).
2️⃣ This creates a **module object** in memory — think of it like a box with all the names (functions, classes, variables) defined inside `mymodule.py`.
3️⃣ The name `mymodule` in your file **points to** this module object.
4️⃣ When you call `mymodule.some_function()`, Python looks up `some_function` *inside* the module object.

---

### 🔬 ✅ Why it’s different from copy-paste

If you **copied** the module code into your file:

* The copied code would execute *in your file’s global namespace*, so all its functions and variables would be mixed with yours.
* With `import`, the module’s variables stay **inside the module object**, preventing name clashes.

---

### 📂 ✅ Example

**`math.py`** (Python’s internal `math` is built-in, but let’s pretend):

```python
# math.py
PI = 3.14

def area(radius):
    return PI * radius ** 2
```

**Your file**:

```python
import math

print(math.area(5))
print(math.PI)
```

* Here, `math` is **one name** pointing to the `math` module object.
* `PI` and `area` stay **inside** that module. They don’t pollute your global variables.

---

### ✅ So, importing ≠ copy-paste

✔ `import` = *execute once* → create namespace → bind it.
❌ copy-paste = all code merges directly into your file’s global scope.

---
---
---

![image](https://github.com/user-attachments/assets/9eb9b1fa-23bb-498f-a9c5-430296a98c04)

__name__ == "module_name": When the file is imported.
__name__ == "__main__": When the file is executed directly.

![image](https://github.com/user-attachments/assets/d9268524-c62e-43ff-9984-1f6f1b321701)

---
![image](https://github.com/user-attachments/assets/16f3849a-6e09-46f4-8c57-09f993fabb8d)

---

# **function overwriting** (or *redefinition*) in Python:

---

## ✅ How function overwriting works in Python

In Python:

* **Functions are just variables** that hold a reference to a callable object.
* If you **define a function with the same name again**, the old function gets *replaced* in that namespace.

---

### 🔍 Example

```python
def greet():
    print("Hello!")

greet()  # Output: Hello!

def greet():
    print("Hi there!")

greet()  # Output: Hi there!
```

🔑 What happened?

* `def greet()` the first time creates a function object and binds it to the name `greet`.
* The second `def greet()` **creates a *new* function object** and re-binds the name `greet` to it.
* The old function is discarded if no other name points to it.

---

## ✅ Does Python warn you?

Nope — Python just does it silently. The last definition *wins*.

---

## ✅ Same with importing

Imagine:

```python
def greet():
    print("Hello!")

from mymodule import greet
```

* If `mymodule` also has a `greet`, then your `greet` gets overwritten with the one from the module.
* The local name just points to the *new* function.

---

## ✅ So is this bad?

It’s not *bad* — it’s just how Python’s name binding works:

* The namespace is **dynamic**.
* If you redefine a function, the old version is gone (unless you saved it).

---

## ✅ You can overwrite on purpose

Sometimes people overwrite functions on purpose:

```python
def add(a, b):
    return a + b

# Monkey patch to log calls:
_old_add = add

def add(a, b):
    print(f"Adding {a} and {b}")
    return _old_add(a, b)

print(add(2, 3))
```

---

##  Key takeaway

* Python doesn’t have `function overloading` like C++ or Java.
* There’s **only the latest definition** for each name.
* If you want multiple behaviors, use `if` statements, `*args`, or decorators.

---
# **packages**, **foldering**, `from . import` and `__init__.py`:
---

## 📂 ✅ 1️⃣ Foldering: modules vs. packages

**🔹 Module:**
A single `.py` file — like `math.py`.

**🔹 Package:**
A **folder** containing an `__init__.py` file and other modules or sub-packages.

Example:

```
myproject/
│
├── main.py
└── mypackage/
    ├── __init__.py
    ├── module1.py
    ├── module2.py
    └── subpackage/
        ├── __init__.py
        └── module3.py
```

✅ *Key point:*
A folder is treated as a **package** only if it has an `__init__.py` file (in older Python versions, this was mandatory; in Python 3.3+ it’s optional for simple namespace packages, but still good practice).

---

## 📌 ✅ 2️⃣ What does `__init__.py` do?

* It makes the folder **importable** as a package.
* It’s executed when you `import` the package.
* It can initialize package-level variables, import submodules, or set `__all__`.

Example `__init__.py`:

```python
# mypackage/__init__.py

print("mypackage is being imported")

from . import module1  # Import module1 when package is imported
version = "1.0"
```

So:

```python
import mypackage
mypackage.module1.some_function()
print(mypackage.version)
```

---

## 📌 ✅ 3️⃣ `from . import` — relative imports

**Relative imports** are used *inside packages* to import sibling or parent modules.

* `.` = *current package*
* `..` = *one level up*
* `...` = *two levels up*, and so on.

Example:

```python
# mypackage/module1.py

from . import module2   # Import sibling
from .subpackage import module3  # Import subpackage’s module
```

So, if you do:

```python
import mypackage.module1
```

then `module1` will import `module2` and `subpackage.module3`.

---

## 📌 ✅ 4️⃣ Why use relative imports?

* They help organize **large packages**.
* They avoid conflicts with similarly named modules in `sys.path`.
* They keep your package **self-contained**.

---

## ✅ 5️⃣ Example: putting it all together

```
myproject/
│
├── main.py
└── mypackage/
    ├── __init__.py
    ├── module1.py
    ├── module2.py
```

**`module1.py`:**

```python
from . import module2

def func1():
    print("This is func1")
    module2.func2()
```

**`module2.py`:**

```python
def func2():
    print("This is func2")
```

**`main.py`:**

```python
from mypackage import module1

module1.func1()
```

**Output:**

```
This is func1
This is func2
```

---

## ✅ Key points recap

✔ **Foldering:** Organize related code in directories.
✔ `__init__.py`: Makes a folder a package, runs on import.
✔ `from . import`: Relative import inside a package.
✔ Use **dot notation** to access submodules.

---



#  **`__all__`** and **forwarding** in Python:

---

## ✅ 1️⃣ `__all__` — what it does

`__all__` is a **list of strings** in a module or package that says:

> *“If someone does `from mymodule import *`, only import these names.”*

**Key points:**

* `__all__` only affects `from ... import *`.
* `import mymodule` or `from mymodule import something` ignores `__all__`.
* By convention, `_private` names are skipped by `*` too.

---

### 🔍 Example: module with `__all__`

```python
# utils.py

__all__ = ['foo']

def foo():
    print("foo")

def bar():
    print("bar")
```

```python
from utils import *

foo()  # ✅ Works
bar()  # ❌ NameError: bar is not defined
```

But:

```python
import utils
utils.bar()  # ✅ Works, __all__ does not block normal import
```

---

## ✅ 2️⃣ Forwarding — what it means

**Forwarding** means a *package* exposes names from its submodules *at the top level* by re-importing them in `__init__.py`.

This lets users write:

```python
from mypackage import foo
```

instead of:

```python
from mypackage.module1 import foo
```

---

### 🔍 Example: forwarding with `__init__.py`

```
mypackage/
  __init__.py
  module1.py
  module2.py
```

**module1.py**

```python
def foo():
    print("foo from module1")
```

**module2.py**

```python
def bar():
    print("bar from module2")
```

****init**.py**

```python
from .module1 import foo
from .module2 import bar

__all__ = ['foo', 'bar']  # Forward only these names!
```

Now:

```python
from mypackage import foo, bar  # ✅ They’re forwarded!
foo()
bar()
```

Without this, you’d need:

```python
from mypackage.module1 import foo
```

---

## ✅ 3️⃣ `__all__` + forwarding

When you **combine** them:

* `from .module1 import foo` **forwards** the symbol.
* `__all__ = ['foo']` **controls what `from mypackage import *` gives you**.

So:

```python
from mypackage import *  # Only foo and bar are imported
```

---

## ✅ 4️⃣ Forwarding can hide your structure

A big package might have 50 files.
You don’t want users to dig into internals:

```python
mypackage/
  __init__.py
  _internal.py
  api.py
```

```python
# _internal.py
def _secret(): ...

# api.py
def public(): ...
```

```python
# __init__.py
from .api import public

__all__ = ['public']
```

Now:

* `from mypackage import *` => only `public`
* `from mypackage import public` => works
* `mypackage._internal` is hidden by convention (underscore).

---

## ✅ 🔑 Final takeaway

| Concept    | What it does                                               |
| ---------- | ---------------------------------------------------------- |
| `__all__`  | Controls what `from ... import *` picks up                 |
| Forwarding | Makes submodules’ names available at the package top level |

Used together, they let you design a **clean public API** while hiding messy details.

---

---

# ✅ Why use `try: except` with `import`?

The main reasons are:
1️⃣ **Optional imports** — gracefully handle when an extra module isn’t installed.
2️⃣ **Fallbacks** — try to import a preferred module, and if it fails, use a backup.
3️⃣ **Cross-version compatibility** — e.g., Python 2 vs 3 differences.
4️⃣ **Platform-specific code** — e.g., `win32` vs `posix`.

---

## ✅ Basic syntax

```python
try:
    import fancy_module
except ImportError:
    fancy_module = None
```

This says:

* Try to import `fancy_module`.
* If it’s not installed, don’t crash — instead, handle it later.

---

## ✅ Example 1: Optional feature

```python
try:
    import numpy as np
except ImportError:
    np = None

def do_stuff():
    if np:
        print(np.array([1, 2, 3]))
    else:
        print("Numpy is not available.")
```

---

## ✅ Example 2: Fallback

```python
try:
    import ujson as json  # UltraJSON (faster)
except ImportError:
    import json  # Built-in fallback
```

---

## ✅ Example 3: Compatibility

```python
try:
    from StringIO import StringIO  # Python 2
except ImportError:
    from io import StringIO  # Python 3
```

---

## ✅ Example 4: Platform-specific

```python
try:
    import winreg  # Windows only
except ImportError:
    winreg = None
```

---

## ✅ Important detail

The only error caught is **`ImportError`** — not *any* error!

```python
try:
    import something
except ImportError:
    # OK: import failed
```

But:

```python
try:
    import something
except:
    # Bad: catches *any* exception,
    # hides bugs like SyntaxError, AttributeError, etc.
```

So **always** catch `ImportError`, not plain `except`.

---

---

## ✅ 1️⃣ What does “absolute path” mean in Python?

* **Absolute import** = `import mypackage.module.submodule`
  → *This means the full *Python module path*, not a filesystem path like `/home/user/...`*

* **Absolute *filesystem path*** → Python does **not** allow you to directly do:

  ```python
  import /home/user/my_script.py  # ❌ This won’t work
  ```

Instead, Python imports **modules** by name, not by file path.
Your file must be in a folder that’s on **`sys.path`** (the module search paths).

---

## ✅ 2️⃣ The usual way — module path

Let’s say your project is:

```
myproject/
 ├── main.py
 ├── helpers/
 │   ├── __init__.py
 │   └── tools.py
```

You can import `tools.py` **absolutely** from `main.py`:

```python
import helpers.tools
```

Or:

```python
from helpers import tools
```

✅ This works because `myproject` is your working directory → it’s on `sys.path`.

---

## ✅ 3️⃣ But what if you have a **real filesystem path**?

Example:

```
/home/user/scripts/my_script.py
```

and you want to import it dynamically?

You need **`importlib`**:

```python
import importlib.util

# Path to your file
path = '/home/user/scripts/my_script.py'

# Name to give it (can be anything)
module_name = 'my_script'

spec = importlib.util.spec_from_file_location(module_name, path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Now you can use it:
module.some_function()
```

✅ This *dynamically* loads the file by absolute path.

---

## ✅ 4️⃣ Another option — add to `sys.path`

If you want Python’s normal `import` to see it:

```python
import sys

sys.path.append('/home/user/scripts')

import my_script
```

But adding to `sys.path` is a bit hacky — `importlib` is better for single-file loading.

---

## ✅ 🔑 Bottom line

| What you want                | How                                |
| ---------------------------- | ---------------------------------- |
| Absolute **import**          | `import package.subpackage.module` |
| Absolute **filesystem path** | Use `importlib.util`               |
| Temporary sys.path           | `sys.path.append()`                |

---
# Garbage Collector:

---

## ✅ What is the Garbage Collector?

The **Garbage Collector** is Python’s automatic memory manager.
Its job is to:

* Track *objects* in memory.
* Free up memory by deleting objects that are **no longer needed** (unreachable).

**Without GC**, your program would keep using more memory until it crashes.

---

## ✅ How does it work?

Python’s GC has **two main parts**:

---

### 1️⃣ Reference Counting

This is the core:

* Every Python object has a **reference count** (number of variables/references pointing to it).
* When the count drops to **zero**, Python *immediately deletes* that object to free memory.

Example:

```python
a = []
b = a  # ref count = 2
del a  # ref count = 1
del b  # ref count = 0 → object is freed
```

Most objects are cleaned up this way — fast and simple.

---

### 2️⃣ Cyclic Garbage Collector

But there’s a problem:

* **Reference counting alone can’t handle cycles!**

Example:

```python
a = []
b = []
a.append(b)
b.append(a)
```

Here:

* `a` points to `b` → `b` points to `a`
* Even if you `del a` and `del b`, the reference count never drops to 0 → memory leak!

So Python has a **cyclic GC** to detect and break *reference cycles*.

---

## ✅ Generational Garbage Collection

Python’s GC uses the **Generational Hypothesis**:

> *Most objects die young.*

So:

* Python puts objects in **3 generations**: **0, 1, 2**
* New objects start in generation 0.
* Surviving objects are promoted to older generations.
* Generation 0 is collected most often, generation 2 the least often (older objects are likely to be long-lived).

---

## ✅ How it works in CPython

In CPython (the main Python implementation):

* Reference counting is always active.
* The **gc module** manages the cycle collector.

You can control it:

```python
import gc

gc.collect()  # Force a collection
gc.get_count()  # See how many objects are in each generation
gc.disable()   # Disable cycle collector (not ref counting!)
gc.enable()    # Re-enable it
```

---

## ✅ Practical notes

* For most code, you **don’t need to think about the GC** — it just works.
* You only care if:

  * You’re leaking memory in complex object graphs.
  * You work with C extensions or large cycles.
  * You need to tune performance (rare for normal scripts).

---

## ✅ Key takeaway

| Part                   | What it does                                    |
| ---------------------- | ----------------------------------------------- |
| **Reference Counting** | Deletes objects as soon as no references exist. |
| **Cycle Collector**    | Detects and deletes unreachable cycles.         |
| **Generations**        | Optimizes when/how often to collect.            |

---

![image](https://github.com/user-attachments/assets/671e8580-fd04-4f3f-a22f-fd93b0818f68)

* You make a list: `[1, 2, 3]`
* `x` *refers* to it.
* Then you do `x1 = x` → now `x1` *also refers* to the same list.
* The `id()` confirms: both names point to the **same object** in memory → same ID.

---

### ✅ How does the GC see this?

* The list `[1, 2, 3]` is an object on the **heap**.
* It has a **reference count** of **2**:

  * One from `x`
  * One from `x1`

---

### 📌 What happens when your program ends?

* When the script ends, **both `x` and `x1` go out of scope** → their references are destroyed.
* The reference count of the list drops from **2 → 0**.
* Because the count is now **zero**, Python’s **reference counting** mechanism *immediately frees* the memory for that list.
* There’s **no cycle** here, so the **cycle detector** is not needed.

---

### ✅ So the GC role here:

* It sees a simple reference count → no cycles.
* When `x` and `x1` are gone, the list is collected.
* This is *typical* — Python’s GC mostly relies on **reference counting** for simple cases like this.

---


# List:

---

## ✅ 1️⃣ What is a list?

A **list** is a built-in **ordered**, **mutable**, **dynamic** sequence type.

* **Ordered** → items keep their order.
* **Mutable** → you can change it: add, remove, modify.
* **Dynamic** → resizes automatically.
* Can hold **any data type**, even mixed types.

```python
my_list = [1, 2, 3, "hello", [4, 5]]
```

---

## ✅ 2️⃣ How to create a list

**Literals**

```python
a = [1, 2, 3]
```

**Constructor**

```python
b = list()        # Empty list
c = list("hello") # ['h', 'e', 'l', 'l', 'o']
```

---

## ✅ 3️⃣ Accessing elements

* **Indexing** (0-based):

```python
a = [10, 20, 30]
print(a[0])  # 10
```

* **Negative indexing**:

```python
print(a[-1]) # 30 (last item)
```

* **Slicing**:

```python
print(a[1:])   # [20, 30]
print(a[:2])   # [10, 20]
print(a[::2])  # [10, 30] (step)
```

---

## ✅ 4️⃣ Modifying lists

**Change element**

```python
a[0] = 99  # [99, 20, 30]
```

**Add elements**

```python
a.append(40)     # Add to end
a.insert(1, 15)  # Insert at index 1
a.extend([50, 60]) # Add multiple
```

**Remove elements**

```python
a.pop()    # Remove last
a.pop(1)   # Remove by index
a.remove(99) # Remove by value
del a[0]   # Remove by index
a.clear()  # Remove all
```

---

## ✅ 5️⃣ Looping over lists
![image](https://github.com/user-attachments/assets/a3bf2f10-a5e6-4624-97ce-98af55111a35)

```python
for item in a:
    print(item)

for index, item in enumerate(a):
    print(index, item)
```

---

## ✅ 6️⃣ Membership test

```python
if 20 in a:
    print("Yes")
```

---

## ✅ 7️⃣ Built-in functions

* `len(a)` → number of elements
* `min(a)` → smallest (if comparable)
* `max(a)` → largest
* `sum(a)` → sum (for numbers)
* `sorted(a)` → returns new sorted list
* `a.sort()` → sorts in place

---

## ✅ 8️⃣ Nested lists

Lists can contain lists:

```python
matrix = [[1, 2], [3, 4]]
print(matrix[1][0])  # 3
```

---

## ✅ 9️⃣ Copying lists

**Wrong way** → just copies reference:

```python
b = a  # same object!
```

**Correct way** → make a *new* list:

```python
b = a.copy()
b = a[:]
import copy
b = copy.deepcopy(a)  # for nested lists
```

---

## ✅ 🔟 List comprehensions

**Powerful syntax** for creating new lists:

```python
squares = [x**2 for x in range(5)]
# [0, 1, 4, 9, 16]

evens = [x for x in range(10) if x % 2 == 0]
```

---

## ✅ 1️⃣1️⃣ Lists are dynamic arrays

* Python lists are implemented as **dynamic arrays** (like C++ `vector`).
* They allocate extra memory so appending is amortized **O(1)**.
* `sys.getsizeof()` can show you memory usage.

---

## ✅ 1️⃣2️⃣ Lists vs tuples

| Feature  | `list`        | `tuple`    |
| -------- | ------------- | ---------- |
| Mutable  | ✅             | ❌          |
| Syntax   | `[1,2]`       | `(1,2)`    |
| Use case | Changing data | Fixed data |

---

## ✅ 1️⃣3️⃣ Common gotchas

* Be careful with **references**:

  ```python
  a = [[0]*3]*3
  a[0][0] = 1
  print(a)  # All rows change!
  ```

  This happens because they share the *same inner list*.

  Proper way:

  ```python
  a = [[0]*3 for _ in range(3)]
  ```

---

## ✅ 1️⃣4️⃣ Memory & GC

* Lists live on the **heap**.
* When they have no references, GC frees them.
* If lists contain other objects, the GC handles that too.

---

## ✅ 1️⃣5️⃣ Useful methods

| Method           | What it does         |
| ---------------- | -------------------- |
| `.append(x)`     | Add one item         |
| `.extend([x,y])` | Add multiple         |
| `.insert(i,x)`   | Insert at index      |
| `.remove(x)`     | Remove by value      |
| `.pop()`         | Remove & return last |
| `.clear()`       | Empty the list       |
| `.index(x)`      | Find first index     |
| `.count(x)`      | Count occurrences    |
| `.sort()`        | Sort in place        |
| `.reverse()`     | Reverse in place     |
| `.copy()`        | Shallow copy         |

---

## ✅ 1️⃣6️⃣ Lists are objects

```python
type(a)   # <class 'list'>
dir(a)    # Shows all list methods
help(list)  # Read the docs
```

---


# **`lst = []` vs `lst.clear()`** when “clearing” a list:

---

## ✅ `lst = []`

**What it does:**

* Makes `lst` *refer to a brand new empty list*.
* The **old list** still exists in memory **if any other variable still refers to it**.

```python
lst = [1, 2, 3]
lst2 = lst

lst = []  # Only 'lst' now points to a new empty list.

print(lst)   # []
print(lst2)  # [1, 2, 3]  <-- the old list still exists here!
```

➡️ `lst = []` **does not clear the old list in memory** — it just points `lst` to a new one.

---

## ✅ `lst.clear()`

**What it does:**

* **Modifies the existing list object** in place.
* Removes all its elements.
* Any other variable that refers to this list sees the change.

```python
lst = [1, 2, 3]
lst2 = lst

lst.clear()  # Clears the *same* list object in memory.

print(lst)   # []
print(lst2)  # []  <-- same list, so also empty here
```

➡️ `lst.clear()` **mutates the list itself**, so **all references** see it emptied.

---

## ✅ When does this matter?

🔍 If you have **one reference**, both ways seem to do the same.

But when you have **multiple references** — for example, passing a list into functions — `clear()` is what you want if you need to empty the *original list*.

---

**So:**

✅ **Use `lst.clear()`** when you want to empty the *existing list*.
✅ **Use `lst = []`** when you want to drop the reference and start fresh with a new list (and you don’t care about other references).

---

![image](https://github.com/user-attachments/assets/58a00388-9c5d-4ecf-a9e2-a2eff4d536f4)


---
#  `.copy()` :

---

## 🔍 The problem: same reference

When you do:

```python
lst1 = [1, 2, 3]
lst2 = lst1
```

* `lst1` and `lst2` **point to the same list object** in memory.
* If you change one, the other sees the change.
* So, you *don’t* have two independent lists.

---

## ✅ The solution: `.copy()`

If you want a **new, independent list**, use:

```python
lst1 = [1, 2, 3]
lst2 = lst1.copy()
```

* `lst2` is a **shallow copy** — a new list with the same elements.
* Changing `lst2` does not affect `lst1`.

Example:

```python
lst1 = [1, 2, 3]
lst2 = lst1.copy()

lst2.append(4)

print(lst1)  # [1, 2, 3]
print(lst2)  # [1, 2, 3, 4]
```

Perfectly independent!

---

## ✅ How does this relate to GC?

* Using `.copy()` **makes a new list object in memory**.
* The old list keeps its references.
* So there’s no accidental aliasing.
* When no references remain for a list object, the **Python garbage collector** will clean it up.

So `.copy()` helps you *control when multiple names point to the same object or not* — which affects when objects can be garbage collected.

---

## ⚙️ Under the hood: `.copy()` vs `[:]`

`.copy()` is the same as:

```python
lst2 = lst1[:]
```

Or:

```python
lst2 = list(lst1)
```

All three do a **shallow copy**.

---

## ⚠️ Caveat: Nested structures

`.copy()` is **shallow** — it only copies the top-level list:

```python
lst1 = [[1, 2], [3, 4]]
lst2 = lst1.copy()

lst2[0].append(99)

print(lst1)  # [[1, 2, 99], [3, 4]]
print(lst2)  # [[1, 2, 99], [3, 4]]
```

See that? The *inner lists* are still shared.

✅ For **deep copies**:

```python
import copy

lst2 = copy.deepcopy(lst1)
```

---

## ✅ Summary

| Action               | Same object?    | GC effect                                    |
| -------------------- | --------------- | -------------------------------------------- |
| `lst2 = lst1`        | ✅ Same          | No new object                                |
| `lst2 = lst1.copy()` | ❌ New           | New object — old one GC’ed when unreferenced |
| `lst2 = lst1[:]`     | ❌ New           | Same as `.copy()`                            |
| `copy.deepcopy()`    | ❌ New deep copy | Recursively copies nested                    |

---

`.copy()` helps you **break shared references**, keep your data isolated, and control **when objects stay alive or get garbage collected**.

---
---
# **iteration through a list in Python**:

---

## ✅ Basic ways to iterate

### 1️⃣ **Using a simple `for` loop**

The most common:

```python
my_list = [10, 20, 30]

for item in my_list:
    print(item)
```

* `item` takes each element **in order**.
* Fast and Pythonic.

---

### 2️⃣ **Using `for` with `range(len())`**

When you need **indexes**:

```python
my_list = ['a', 'b', 'c']

for i in range(len(my_list)):
    print(i, my_list[i])
```

* `i` is the **index** (0, 1, 2...).
* Useful when you need to modify by index.

---

### 3️⃣ **Using `enumerate()`**

✅ More Pythonic than `range(len())`:

```python
my_list = ['apple', 'banana', 'cherry']

for idx, item in enumerate(my_list):
    print(idx, item)
```

* `enumerate()` gives you `(index, item)`.
* Faster and clearer than `range(len())`.

---

### 4️⃣ **Using `while` loop**

Rare but possible:

```python
my_list = [5, 6, 7]
i = 0

while i < len(my_list):
    print(my_list[i])
    i += 1
```

* Useful when index needs to change in non-linear ways.

---

### 5️⃣ **List comprehensions**

For transforming or filtering:

```python
my_list = [1, 2, 3]
squared = [x ** 2 for x in my_list]

print(squared)  # [1, 4, 9]
```

* One-liner for creating a new list.
* Faster than `for` + `append`.

---

## ✅ Common gotchas

### ❌ Modifying a list while iterating

Bad:

```python
lst = [1, 2, 3, 4]

for x in lst:
    if x == 2:
        lst.remove(x)  # Risky! Skips elements.
```

Better:

```python
# Use a copy to avoid messing up the iterator
for x in lst[:]:
    if x == 2:
        lst.remove(x)
```

Or use list comprehension to filter:

```python
lst = [x for x in lst if x != 2]
```

---

## ✅ Advanced: `zip()`

When iterating multiple lists in parallel:

```python
a = [1, 2, 3]
b = ['a', 'b', 'c']

for num, letter in zip(a, b):
    print(num, letter)
```

---

## ✅ Performance tips

* `for x in my_list` is fastest.
* `range(len(...))` is fine for index-only needs.
* `enumerate()` is more Pythonic than `range(len(...))`.

---

## ✅ Summary cheat sheet

| Pattern                      | Use case             |
| ---------------------------- | -------------------- |
| `for x in lst`               | Simple read          |
| `for i in range(len(lst))`   | Index-based          |
| `for i, x in enumerate(lst)` | Index + value        |
| `while i < len(lst)`         | Manual index control |
| `[x for x in lst]`           | New transformed list |
| `zip(list1, list2)`          | Multiple lists       |

---


