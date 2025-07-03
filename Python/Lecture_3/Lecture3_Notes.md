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















