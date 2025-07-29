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

<img width="800" height="618" alt="image" src="https://github.com/user-attachments/assets/ad99c804-6ce3-41c5-877f-9544e06ca061" />

---
# how the Internet works

---

## 🌐 **What is the Internet?**

At its core, the Internet is a massive **network of networks**.
Millions of devices (computers, phones, servers) are connected together so they can **exchange data**.

It’s like:

* **Cables & Wi-Fi:** Physical connections.
* **Routers & Switches:** Direct traffic.
* **Protocols:** Define how devices talk.

---

## ✅ **How does it work?**

Let’s walk through a simple example:
**“You open your web browser and visit `www.example.com`.”**

---

### 1️⃣ **Your device gets an IP address**

* Your computer/phone joins a network (like your home Wi-Fi).
* Your router (or your ISP) gives it an **IP address** (like a street address).

---

### 2️⃣ **You type a website → DNS**

* You type `www.example.com`.
* Your device doesn’t know its IP address — it needs to find it.
* So it asks a **DNS server** (Domain Name System):
  “What is the IP of `www.example.com`?”
* The DNS server replies: `93.184.216.34` (for example).

---

### 3️⃣ **Your device builds a packet**

* Your browser creates an **HTTP request**:
  *“GET /”* (give me the homepage).
* This data is wrapped in:

  * **Application Layer:** HTTP
  * **Transport Layer:** TCP segments (reliable delivery)
  * **Network Layer:** IP packets (adds source & destination IP)
  * **Data Link Layer:** Ethernet frames (adds MAC addresses)
  * **Physical Layer:** Transmits as electrical signals or radio waves.

---

### 4️⃣ **Your request travels across networks**

* Your request leaves your device → goes to your **router**.
* The router checks the IP destination → sends it out to your ISP.
* The ISP routes it through **many routers**, until it reaches the web server that owns `www.example.com`.

---

### 5️⃣ **The server responds**

* The server receives your packet → sees the HTTP request → prepares a response.
* The response (e.g., an HTML file) is broken into packets and sent back to your IP.
* The packets travel back through routers → your ISP → your router → your device.

---

### 6️⃣ **Your browser displays the page**

* Your computer reassembles the TCP segments into a full web page.
* The browser renders the HTML, images, CSS, JavaScript — and you see the website.

---

## ✅ **Key pieces making this possible**

**💡 IP addresses** — Unique ID for every device.

**💡 Routers** — Direct traffic based on IP addresses.

**💡 DNS** — Like a phonebook for domain names.

**💡 Protocols** — Rules for how data moves (TCP, IP, HTTP).

**💡 Physical layer** — Cables, fiber optics, Wi-Fi, 4G/5G, etc.

---

## ⚙️ **The OSI Layers in action**

* Your request starts at **Application Layer** (HTTP).
* Goes down through **Presentation**, **Session**, **Transport (TCP)**, **Network (IP)**, **Data Link (Ethernet)**, **Physical (cables)**.
* Then up the layers again at the server.
* Same on the way back.

---

# IPC Example

<img width="1777" height="936" alt="image" src="https://github.com/user-attachments/assets/4051e7c9-3851-4f16-8b04-69a8415b09c5" />

---
# c++ and python IPC

### C++ Server Code:
```cpp
#include <iostream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <cstring>

int main() {
    int socketBox, newSocket, recvSize;
    struct sockaddr_in server, client;
    char message[2000] = {0};

    // Create socket
    socketBox = socket(AF_INET, SOCK_STREAM, 0);
    if (socketBox == -1) {
        std::cerr << "Could not create socket\n";
        return 1;
    }

    // Prepare the sockaddr_in structure
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;
    server.sin_port = htons(8888);

    // Bind
    if (bind(socketBox, reinterpret_cast<struct sockaddr*>(&server), sizeof(server)) < 0) {
        std::cerr << "Bind failed\n";
        return 1;
    }

    // Listen
    listen(socketBox, 3);
    std::cout << "Waiting for incoming connections...\n";

    // Accept incoming connection
    socklen_t clientLen = sizeof(client);
    newSocket = accept(socketBox, reinterpret_cast<struct sockaddr*>(&client), &clientLen);
    if (newSocket < 0) {
        std::cerr << "Accept failed\n";
        return 1;
    }

    // Receive and send messages
    while ((recvSize = recv(newSocket, message, sizeof(message), 0)) > 0) {
        std::cout << "Received: " << message << std::endl;
        send(newSocket, message, strlen(message), 0);
        memset(message, 0, sizeof(message));
    }

    if (recvSize == 0) {
        std::cout << "Client disconnected\n";
    } else if (recvSize == -1) {
        std::cerr << "Receive failed\n";
    }

    close(newSocket);
    close(socketBox);
    return 0;
}
```

### Python Client Code:
```python
import socket

def main():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Server address and port
    server_address = ('localhost', 8888)

    try:
        # Connect to the server
        client_socket.connect(server_address)

        # Send data to server
        message = "hello"
        client_socket.sendall(message.encode())

        # Receive response from server
        response = client_socket.recv(1024).decode()
        print(f"Received response from server: {response}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the socket
        client_socket.close()

if __name__ == "__main__":
    main()
```
