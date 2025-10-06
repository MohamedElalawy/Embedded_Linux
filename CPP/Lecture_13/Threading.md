# threads in C++
---

## 🧩 1. What is a Thread?

A **thread** is a separate path of execution within a program.
You can run multiple threads **concurrently**, allowing your program to perform several tasks at once.

In C++, threading is provided by the **`<thread>`** header introduced in **C++11**.

---

## ⚙️ 2. Your First Thread

Here’s the simplest example of creating and running a thread:

```cpp
#include <iostream>
#include <thread>

void hello() {
    std::cout << "Hello from thread!\n";
}

int main() {
    std::thread t(hello);  // create and start a thread
    t.join();              // wait for the thread to finish
    std::cout << "Hello from main!\n";
    return 0;
}
```

### Output (order may vary)

```
Hello from thread!
Hello from main!
```

🧠 **Explanation:**

* `std::thread t(hello);` starts a new thread that runs `hello()`.
* `t.join();` waits for the thread to complete before continuing.

---

## 🧵 3. Passing Arguments to Threads

You can pass arguments to a thread function:

```cpp
#include <iostream>
#include <thread>

void printNumber(int n) {
    std::cout << "Number: " << n << "\n";
}

int main() {
    std::thread t(printNumber, 42);
    t.join();
    return 0;
}
```

Output:

```
Number: 42
```

---

## ⚡ 4. Running Multiple Threads

You can create several threads that work simultaneously.

```cpp
#include <iostream>
#include <thread>

void task(int id) {
    std::cout << "Task " << id << " is running\n";
}

int main() {
    std::thread t1(task, 1);
    std::thread t2(task, 2);
    std::thread t3(task, 3);

    t1.join();
    t2.join();
    t3.join();
    return 0;
}
```

Output (order not guaranteed):
<img width="1350" height="951" alt="image" src="https://github.com/user-attachments/assets/8dea44e5-3a35-400e-b49f-997c37c447d5" />

```
Task 2 is running
Task 1 is running
Task 3 is running
```

💡 Output order changes each run because threads execute concurrently.

---

## 🚀 5. Lambda Threads

You can use **lambda functions** instead of defining separate functions:

```cpp
#include <iostream>
#include <thread>

int main() {
    std::thread t([] {
        std::cout << "Hello from lambda thread!\n";
    });

    t.join();
    return 0;
}
```

---

## 🧹 6. Detaching Threads

If you don’t want to wait (`join()`), you can **detach** a thread:

```cpp
#include <iostream>
#include <thread>
#include <chrono>

void backgroundTask() {
    std::this_thread::sleep_for(std::chrono::seconds(2));
    std::cout << "Background task done!\n";
}

int main() {
    std::thread t(backgroundTask);
    t.detach();  // runs independently
    std::cout << "Main thread done!\n";
    std::this_thread::sleep_for(std::chrono::seconds(3));  // wait to see output
}
```

⚠️ Be careful — detached threads can cause issues if the main program ends before they do.

---

## synchronization:

When multiple threads access shared data at the same time, things can go wrong — that’s where **`std::mutex`** and friends come in.

---

## 🧠 1. The Problem: Race Conditions

Let’s look at a problem example first:

```cpp
#include <iostream>
#include <thread>

int counter = 0;

void increment() {
    for (int i = 0; i < 100000; ++i)
        ++counter;
}

int main() {
    std::thread t1(increment);
    std::thread t2(increment);

    t1.join();
    t2.join();

    std::cout << "Counter: " << counter << "\n";
    return 0;
}
```

Expected output:

```
Counter: 200000
```

But actual output may vary each run — e.g.,

<img width="1140" height="642" alt="image" src="https://github.com/user-attachments/assets/de0984d4-5cf9-4b70-a779-e49b851846fd" />


💥 This happens because both threads modify `counter` **at the same time**, causing a **race condition**.

---

## 🧩 2. Fixing It with `std::mutex`

A **mutex** (mutual exclusion) ensures only one thread can access a section of code at a time.

```cpp
#include <iostream>
#include <thread>
#include <mutex>

int counter = 0;
std::mutex mtx;

void increment() {
    for (int i = 0; i < 100000; ++i) {
        mtx.lock();    // lock before accessing shared data
        ++counter;
        mtx.unlock();  // unlock after done
    }
}

int main() {
    std::thread t1(increment);
    std::thread t2(increment);

    t1.join();
    t2.join();

    std::cout << "Counter: " << counter << "\n";
    return 0;
}
```

✅ Output will now **always** be:
<img width="1358" height="845" alt="image" src="https://github.com/user-attachments/assets/94423f37-e35e-45f7-965b-9c968d78c42a" />


---

## 🔒 3. Using `std::lock_guard`

Manually locking and unlocking is risky — what if your function throws an exception?
That could leave the mutex **locked forever** 😱.

Instead, use **`std::lock_guard`**, which automatically locks and unlocks when it goes out of scope.

<img width="1237" height="848" alt="image" src="https://github.com/user-attachments/assets/40de296c-c8a7-4edf-bfda-7e2a4722b8b9" />


🧹 The lock is automatically released when `lock` goes out of scope — clean and safe.

---

## ⚙️ 4. `std::unique_lock` — More Flexible

`std::unique_lock` is like `lock_guard`, but more powerful:

* You can manually lock/unlock it later.
* It supports **`std::condition_variable`** (used for communication).

Example:

```cpp
#include <iostream>
#include <thread>
#include <mutex>

std::mutex mtx;

void task() {
    std::unique_lock<std::mutex> lock(mtx);
    std::cout << "Thread has lock\n";
    lock.unlock();  // manually unlock
    std::cout << "Thread released lock\n";
}

int main() {
    std::thread t(task);
    t.join();
}
```

---

## 🕰️ 5. Timed Locks

Sometimes you want to try locking a mutex, but not wait forever.

```cpp
#include <iostream>
#include <thread>
#include <mutex>
#include <chrono>

std::mutex mtx;

void tryLockExample() {
    if (mtx.try_lock()) {
        std::cout << "Got the lock!\n";
        mtx.unlock();
    } else {
        std::cout << "Couldn't get the lock.\n";
    }
}

int main() {
    std::thread t1(tryLockExample);
    std::thread t2(tryLockExample);

    t1.join();
    t2.join();
}
```

---

## 🚦 6. Summary

| Tool               | Purpose                | Typical Use                             |
| ------------------ | ---------------------- | --------------------------------------- |
| `std::mutex`       | Basic mutual exclusion | Manual lock/unlock                      |
| `std::lock_guard`  | RAII wrapper           | Automatically lock/unlock safely        |
| `std::unique_lock` | More flexible lock     | For condition variables / manual unlock |
| `try_lock()`       | Non-blocking attempt   | Optional locking                        |

---

✅ You now understand **how to safely access shared data** in multi-threaded programs.

---
[Playlist 3zema](https://www.youtube.com/watch?v=TPVH_coGAQs&list=PLk6CEY9XxSIAeK-EAh3hB4fgNvYkYmghp)

