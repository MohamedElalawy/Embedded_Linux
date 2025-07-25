# Threads | Socket | System | Gui
---


### *thread* in general

A **thread** is the smallest unit of execution in a process.
It’s like a lightweight subprocess: multiple threads share the same memory space but can run *apparently* in parallel.

For example:

* A web server might use threads to handle multiple connections at the same time.
* A GUI app might use a background thread to download data while the main thread keeps the interface responsive.

---

### `Thread` in Python

In Python, `Thread` (uppercase **T**) usually refers to the **`Thread` class** from the **`threading`** module.

Basic usage:

```python
import threading
import time

print("Main Thread:")
print(f"  Python thread ID: {threading.get_ident()}")
print(f"  Native thread ID: {threading.get_native_id()}")

def worker():
    print("Thread 1:")
    print(f"  Python thread ID: {threading.get_ident()}")
    print(f"  Native thread ID: {threading.get_native_id()}")
    time.sleep(1000)

def worker2():
    print("Thread 2:")
    print(f"  Python thread ID: {threading.get_ident()}")
    print(f"  Native thread ID: {threading.get_native_id()}")
    time.sleep(1000)

t = threading.Thread(target=worker)
t2 = threading.Thread(target=worker2)

t.start()
t2.start()

t.join()
t2.join()


```

* `threading.Thread` creates a new thread.
* `.start()` begins running it.
* `.join()` waits for it to finish.

---

<img width="1007" height="330" alt="image" src="https://github.com/user-attachments/assets/bd5f238b-3a86-4885-b99f-37c2cff9679d" />

---

#  What is a **process**?

A **process** is an **independent instance of a running program**.

* It has its own **memory space** (code, data, open files).
* Processes do not share memory by default.
* Each process can have one or more **threads** inside it.

Example:

* When you run Python, the interpreter runs as a **process**.
* Inside that Python process, you can have multiple **threads**.

---

##  Key difference: **process vs thread**

| Aspect            | Process                                        | Thread                                               |
| ----------------- | ---------------------------------------------- | ---------------------------------------------------- |
| **Definition**    | Independent running program                    | Smallest unit of execution inside a process          |
| **Memory**        | Has its own memory space                       | Shares memory with other threads in the same process |
| **Communication** | Needs inter-process communication (IPC)        | Threads communicate easily via shared data           |
| **Crash impact**  | One process crash usually doesn’t crash others | A bad thread can crash the whole process             |
| **Example**       | Python interpreter, browser tabs, VSCode       | Worker threads in a web server, GUI background task  |

---

## ✅ Processes in Python

Python’s **`multiprocessing`** module lets you create multiple **processes**.
It’s different from `threading`:

* `threading` → runs threads in the same process, sharing memory.
* `multiprocessing` → runs multiple processes, each with its own Python interpreter and memory space.

Example:

```python
from multiprocessing import Process

def worker():
    print("Hello from a separate process")

p = Process(target=worker)
p.start()
p.join()
```

---

##  Why use processes in Python?

The **GIL** (Global Interpreter Lock) limits Python threads: only one thread runs Python bytecode at a time.
So for **CPU-bound** tasks (like heavy calculations), multiple processes work better — they can run truly in parallel on multiple cores.

For **I/O-bound** tasks (networking, file I/O), `threading` is fine — because threads can switch while waiting for I/O.

---

<img width="750" height="375" alt="image" src="https://github.com/user-attachments/assets/a2f536cd-24e9-4338-a2ee-ed290a6ce20b" />

---

# `socket`

##  **What is a *socket* in general?**

A **socket** is an **endpoint for communication** between two machines or processes — like a virtual plug.

* At the OS level, it’s an abstraction for a network connection.
* A socket can be **TCP** (connection-oriented) or **UDP** (connectionless).
* Example: a web server listens on a TCP socket at port 80.

---

##  **What is `socket` in Python?**

In Python, `socket` (lowercase) is the name of the **standard library module**:

```py
import socket
```

Inside the `socket` module you have:

* The **`socket()`** function/class → to create a new socket object.
* Constants (e.g., `socket.AF_INET`, `socket.SOCK_STREAM`).
* Exceptions like `socket.error`.

So when people say **`socket`** in Python code, they usually mean:

1. The **module** → `socket`
2. A **socket object** → created by calling `socket.socket()`.

---

##  **Example: using the `socket` module**

Here’s a tiny TCP client example:

```python
import socket

# Create a socket object (AF_INET = IPv4, SOCK_STREAM = TCP)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a server (e.g., google.com on port 80)
s.connect(('www.google.com', 80))

# Send HTTP request
s.sendall(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")

# Receive response
response = s.recv(4096)
print(response)

s.close()
```
---



