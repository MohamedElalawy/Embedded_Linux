<img width="1233" height="652" alt="image" src="https://github.com/user-attachments/assets/e29a7f2a-c535-4687-9030-c0f5f94c1c1c" />

Excellent — this is a **very important distinction** in C++.
Let’s go through it carefully 👇

---

## 🧩 1. When a method is **defined inside** the class

Example:

```cpp
class Car {
public:
    void test() { std::cout << "Inside class definition\n"; }
};
```

✅ **This version is automatically `inline`.**

That’s because, according to the C++ standard:

> Any member function that is defined *inside the class definition* is implicitly declared as `inline`.

So, the compiler treats it as:

```cpp
class Car {
public:
    inline void test() { std::cout << "Inside class definition\n"; }
};
```

This allows you to place the class definition (and its functions) in a **header file** without causing “multiple definition” errors when included in multiple `.cpp` files.

---

## 🧩 2. When a method is **declared inside** but **defined outside** the class

<img width="1303" height="671" alt="image" src="https://github.com/user-attachments/assets/3ed82cc0-1a1b-4579-afd3-8711207fe84b" />


🚫 **This version is *not* automatically inline.**

Now, the compiler no longer assumes it’s `inline`, because:

* The definition is *separate* from the class body.
* Only functions defined *inside* the class body get that implicit `inline` behavior.

So here, `Car::test()` is a **normal function**, not an inline one.

---

## 🧠 3. If you still want it inline

You can explicitly mark it as `inline` yourself:

```cpp
class Car {
public:
    void test();
};

inline void Car::test() {
    std::cout << "Defined outside but marked inline\n";
}
```

Now the compiler treats it the same way as if it were defined inside the class — it can be inlined, and multiple definitions across translation units are allowed.

---

## 🧾 Summary Table

| Definition style                        | Example                                  | Implicitly inline? | Notes                                 |
| --------------------------------------- | ---------------------------------------- | ------------------ | ------------------------------------- |
| Defined **inside** class                | `void test(){...}`                       | ✅ Yes              | Automatic `inline`                    |
| Declared inside, defined **outside**    | `void test();` + `void Car::test(){...}` | ❌ No               | Must add `inline` manually            |
| Defined outside **with inline keyword** | `inline void Car::test(){...}`           | ✅ Yes              | Equivalent to inside-class definition |

---

### 💬 In short

> A member function is only **implicitly inline** if it’s **defined inside** the class body.
> If you define it **outside**, you must explicitly write `inline` if you want the same behavior.

---

<img width="1113" height="202" alt="image" src="https://github.com/user-attachments/assets/557ab16f-832e-4222-ac0f-60e957061d9d" />

### 🧠 What it means

#### 1. `constexpr` or `consteval` functions are **implicitly inline**

When you write:

```cpp
constexpr int square(int x) { return x * x; }
```

you don’t need to also write `inline`.
Because `constexpr` already **implies** `inline`.

So this:

```cpp
constexpr int square(int x) { return x * x; }
```

is **equivalent to**:

```cpp
inline constexpr int square(int x) { return x * x; }
```

---

#### 2. Why?

Because `constexpr` functions are often defined in **header files**, and the compiler must allow multiple identical definitions of them across translation units — the same reason we need `inline`.

If `constexpr` didn’t imply `inline`, you’d get “multiple definition” linker errors whenever you included the same header in several `.cpp` files.

---

#### 3. The same applies to `consteval` (since C++20)

`consteval` means the function **must** be evaluated at compile-time.
It also gets the same implicit `inline` behavior.

Example:

```cpp
consteval int add(int a, int b) { return a + b; }
```

This is treated as:

```cpp
inline consteval int add(int a, int b) { return a + b; }
```

---

#### 4. Deleted functions are also implicitly inline

Example:

```cpp
class Car {
public:
    Car(const Car&) = delete;
};
```

Even though `= delete;` means the function can’t be used,
the standard makes it **implicitly inline**, so that the “deleted” declaration can safely appear in multiple translation units (again, usually through header inclusion).

---

### ✅ Summary Table

| Function Type                                    | Implicitly `inline`? | Why                                              |
| ------------------------------------------------ | -------------------- | ------------------------------------------------ |
| Defined inside a class                           | ✅ Yes                | Class member rule                                |
| Declared `constexpr`                             | ✅ Yes                | Must be usable in headers & constant expressions |
| Declared `consteval` (C++20+)                    | ✅ Yes                | Compile-time only function                       |
| Declared `= delete`                              | ✅ Yes                | Safe to repeat across translation units          |
| Declared/defined outside class (normal function) | ❌ No                 | Needs `inline` explicitly                        |

---

### 🧠 In short:

> `constexpr`, `consteval`, and deleted functions are automatically treated as `inline` —
> so you can safely define them in headers without duplication errors.

---

## 🧩 What is a Constructor?

A **constructor** is a **special function** inside a class that’s automatically called when you **create an object** of that class.

Its main job is to **initialize** the object — that is, set up its data members and prepare it for use.

---

### 🧠 Key facts about constructors

* The constructor’s **name is the same as the class name**.
* It **has no return type** (not even `void`).
* It can be **overloaded** (you can have multiple constructors with different parameters).
* It’s called **automatically** when you create an object.

Example:

```cpp
class Car {
public:
    Car() { // Constructor
        std::cout << "Car object created!\n";
    }
};
```

When you write:

```cpp
Car myCar;
```

→ The constructor `Car()` is automatically called.

---

## ⚙️ Types of Constructors

There are **5 main types** of constructors in C++.

---

### 1️⃣ **Default Constructor**

* Takes **no parameters**.
* Automatically created by the compiler if you don’t define any constructor yourself.

Example:

```cpp
class Car {
public:
    Car() {
        std::cout << "Default constructor called\n";
    }
};
```

If you don’t define it, the compiler implicitly provides:

```cpp
Car() = default;
```

---

### 2️⃣ **Parameterized Constructor**

* Takes **arguments**.
* Used to initialize objects with specific values.

Example:

```cpp
class Car {
public:
    std::string brand;
    int year;

    Car(std::string b, int y) {
        brand = b;
        year = y;
    }
};
```

Usage:

```cpp
Car c1("Audi", 2024);
```

---

### 3️⃣ **Copy Constructor**

* Used when **creating a new object from an existing one** of the same type.
* The syntax is:

  ```cpp
  ClassName (const ClassName &obj)
  ```

Example:

```cpp
class Car {
public:
    std::string brand;

    Car(std::string b) : brand(b) {}
    Car(const Car &c) { // Copy constructor
        brand = c.brand;
    }
};
```

Usage:

```cpp
Car c1("BMW");
Car c2 = c1; // Calls copy constructor
```

---

### 4️⃣ **Move Constructor** (C++11 and later)

* Used to transfer (move) resources from one object to another **instead of copying**.
* Signature:

  ```cpp
  ClassName(ClassName &&obj)
  ```

Example:

```cpp
class Car {
public:
    std::string brand;

    Car(std::string b) : brand(std::move(b)) {}
    Car(Car &&c) noexcept { // Move constructor
        brand = std::move(c.brand);
    }
};
```

Usage:

```cpp
Car c1("Tesla");
Car c2 = std::move(c1); // Move constructor called
```

---

### 5️⃣ **Copy Elision / Compiler-Generated Constructor**

* The compiler may **omit** copy or move operations for optimization (called *copy elision*).
* You’ll often see this in return statements:

  ```cpp
  return Car("BMW"); // The temporary is constructed directly
  ```

---

### Bonus: **Destructor** (not a constructor but related)

When the object’s lifetime ends, the **destructor** is automatically called to clean up:

```cpp
~Car() {
    std::cout << "Car destroyed\n";
}
```

---

## 🧾 Summary Table

| Type                      | Syntax                 | Purpose                                   |
| ------------------------- | ---------------------- | ----------------------------------------- |
| Default Constructor       | `Car()`                | Initializes object with default values    |
| Parameterized Constructor | `Car(int a, string b)` | Initializes object with specific values   |
| Copy Constructor          | `Car(const Car &obj)`  | Creates copy of another object            |
| Move Constructor          | `Car(Car &&obj)`       | Transfers resources instead of copying    |
| Implicit / Defaulted      | `Car() = default;`     | Compiler-generated version if not defined |

---

## 🧩 What is `this`?

In C++, **`this`** is a **special pointer** that exists inside **all non-static member functions** of a class.

It **points to the object** that **called** the function.

---

### 🧠 Think of it like this:

When you have an object calling a method:

```cpp
Car audi;
audi.start();
```

Inside the `start()` function, the compiler secretly passes a hidden pointer — the **address of `audi`** — so that the function knows *which object’s data it’s working on*.

That pointer is named `this`.

---

### 🔹 Example

```cpp
#include <iostream>
using namespace std;

class Car {
public:
    string brand;
    int year;

    Car(string b, int y) {
        // "this" points to the object being constructed
        this->brand = b;
        this->year = y;
    }

    void show() {
        cout << "Brand: " << this->brand << ", Year: " << this->year << endl;
    }
};

int main() {
    Car c1("BMW", 2024);
    c1.show();
}
```

#### Output:

```
Brand: BMW, Year: 2024
```

Here:

* Inside the constructor, `this->brand` refers to the **brand member** of the current object (`c1`).
* `this` is a pointer to `c1`.

---

### 🧩 Why use `this`?

It’s especially useful when:

1. **Parameter names are the same as member names:**

   ```cpp
   class Car {
       string brand;
   public:
       Car(string brand) {
           this->brand = brand; // disambiguates between member and parameter
       }
   };
   ```

   Without `this->`, the compiler would think both refer to the parameter.

---

2. **Returning the current object**

   ```cpp
   class Car {
       int speed;
   public:
       Car(int s) : speed(s) {}
       Car& setSpeed(int s) {
           this->speed = s;
           return *this; // return the object itself
       }
   };
   ```

   Then you can chain calls:

   ```cpp
   Car c(100);
   c.setSpeed(120).setSpeed(150); // method chaining
   ```

---

3. **Passing the current object to another function**

   ```cpp
   void printCar(const Car* c);

   class Car {
   public:
       void show() {
           printCar(this); // pass pointer to current object
       }
   };
   ```

---

### ⚙️ Technical details

| Aspect           | Description                                                    |
| ---------------- | -------------------------------------------------------------- |
| Type             | `this` is a **pointer** (e.g., `Car* this` inside class `Car`) |
| Scope            | Available in **non-static member functions only**              |
| Static functions | ❌ Cannot use `this`, since they are not tied to any object     |
| Const functions  | The type becomes `const Car* this`                             |

Example:

```cpp
void show() const {
    // here, "this" is of type "const Car*"
}
```

---

### ✅ Summary

| Concept          | Meaning                                                            |
| ---------------- | ------------------------------------------------------------------ |
| `this`           | Pointer to the current object                                      |
| Type             | ClassName* (or const ClassName* for const methods)                 |
| Common uses      | Resolve name conflicts, return current object, pass current object |
| Not available in | Static member functions                                            |

---

# trivial vs non-trivial classes
## ⚙️ What Does “Trivial” Mean?

A **trivial class** is one that the compiler can manage **entirely without custom code** — meaning the compiler can safely:

* Copy it with `memcpy()`
* Initialize it with zeroes
* Destroy it by doing nothing

This makes it **very efficient** and **C-compatible**.

---

### ✅ Trivial Class — Definition

A class is **trivial** if **all** of the following are true:

1. It has **at least one default constructor** (either implicit or explicitly `= default`).
2. All **special member functions** (default constructor, copy/move constructor, copy/move assignment, destructor) are **trivial**.
3. It has **no virtual functions** or **virtual base classes**.
4. Its **base classes and members** are also **trivial**.

---

### 💡 Example of a Trivial Class

```cpp
struct Point {
    int x;
    int y;
};
```

* No user-defined constructors/destructors.
* No inheritance or virtual functions.
* All members are trivial types (`int`).

This class is **trivial** — the compiler can copy it by raw memory copy.

---

### ❌ Non-Trivial Class — Definition

A class becomes **non-trivial** when **any** of its special member functions is **user-defined** or **non-trivial** itself.

That includes:

* Defining your own constructor/destructor.
* Having virtual functions.
* Having base classes or members that are non-trivial.

---

### ⚠️ Example of a Non-Trivial Class

```cpp
struct Person {
    std::string name;  // std::string is non-trivial
    int age;

    Person() {}  // User-defined constructor makes it non-trivial
};
```

or

```cpp
struct A {
    virtual void f() {}  // virtual function → non-trivial
};
```

Even an empty user-defined constructor destroys triviality.

---

## 🧠 Why It Matters

| Feature                    | Trivial                    | Non-Trivial                             |
| -------------------------- | -------------------------- | --------------------------------------- |
| Memory copyable (`memcpy`) | ✅ Yes                      | ❌ No (could break invariants)           |
| Zero initialization        | ✅ Safe                     | ⚠️ Might skip important setup           |
| C compatibility            | ✅ Compatible               | ❌ Not compatible                        |
| Object lifetime management | Simple (no ctor/dtor code) | Complex (requires calls to ctors/dtors) |
| Performance                | Very fast                  | Slightly slower due to extra steps      |

---

### 🔍 Checking Triviality in Code

You can check if a type is trivial with the `<type_traits>` header:

```cpp
#include <type_traits>
#include <iostream>

struct A { int x; };
struct B { B() {} };

int main() {
    std::cout << std::is_trivial<A>::value << "\n";  // 1 (true)
    std::cout << std::is_trivial<B>::value << "\n";  // 0 (false)
}
```

---
# initializer lists
## 🧩 1. What Is an *Initializer List*?

In C++, an **initializer list** is a syntax used to **initialize class members** (especially in constructors) **before** the constructor body executes.

You use it after a colon (`:`) in a constructor definition.

---

### ✅ Example: Member Initializer List

```cpp
class Point {
    int x;
    int y;

public:
    Point(int a, int b) : x(a), y(b) {   // <— initializer list
        // constructor body
    }
};
```

**What happens:**

* `x` is initialized directly with `a`
* `y` is initialized directly with `b`
* Then the constructor body runs (if any extra logic is needed)

This is **not** assignment — it’s **direct initialization** that happens before the body.

---

## ⚙️ 2. Why Use an Initializer List?

It’s important for several reasons:

| Reason                             | Explanation                                                                 |
| ---------------------------------- | --------------------------------------------------------------------------- |
| **Performance**                    | Avoids double initialization (e.g., default constructor + assignment).      |
| **Const / Reference Members**      | You **must** initialize `const` and reference (`&`) members in the list.    |
| **Base Class Initialization**      | Used to call base class constructors before derived class constructor body. |
| **Uniform Initialization (C++11)** | Works cleanly with `{}` syntax for direct member initialization.            |

---

### ❌ Bad Example (Double Initialization)

```cpp
class Point {
    int x;
    int y;
public:
    Point(int a, int b) {
        x = a;   // first default-constructed, then assigned
        y = b;
    }
};
```

Here, `x` and `y` are first default-initialized, **then assigned**, which is slightly less efficient.

---

### ✅ Good Example (Direct Initialization)

```cpp
class Point {
    int x;
    int y;
public:
    Point(int a, int b) : x(a), y(b) {}
};
```

Here, `x` and `y` are **initialized once**, directly — better and necessary for const/reference members.

---

## 🧱 3. Order of Initialization

Even if you write them in any order in the list, **members are initialized in the order they’re declared in the class**, not the order in the list.

### Example:

```cpp
class Example {
    int a;
    int b;
public:
    Example() : b(2), a(1) {}  // initializes 'a' first, then 'b' (based on declaration order)
};
```

⚠️ This can cause **compiler warnings** if the order differs — so it’s good practice to match declaration order.

---

## 🧩 4. Initializer Lists for Inheritance

Used to call **base class constructors** from derived classes.

```cpp
class Base {
public:
    Base(int n) { }
};

class Derived : public Base {
    int x;
public:
    Derived(int val) : Base(val), x(val * 2) { }
};
```

Base class constructors **always run before** the derived class’s constructor body.

---

## 🧮 5. `std::initializer_list<T>` (C++11 Feature)

This is a **standard library template** that allows initialization from a list of values (usually with `{}`).

### Example:

```cpp
#include <initializer_list>
#include <iostream>

class MyList {
public:
    MyList(std::initializer_list<int> values) {
        for (int v : values)
            std::cout << v << " ";
    }
};

int main() {
    MyList obj = {1, 2, 3, 4, 5};  // passes {1,2,3,4,5} as initializer_list<int>
}
```

**Output:**

```
1 2 3 4 5
```

This feature underlies many modern C++ idioms, such as:

* Initializing `std::vector` or `std::map` with `{}`.
* Uniform initialization syntax (`T obj{args...}`).

---

# delegating constructors
This is a powerful feature that helps reduce code duplication between constructors in the **same class**.


## 🧩 1. What Is a Delegating Constructor?

A **delegating constructor** is a constructor that **calls another constructor** of the **same class** to perform some or all of the initialization work.

Introduced in **C++11**, it allows you to write **cleaner, DRY (Don’t Repeat Yourself)** constructor code.

---

### ✅ Example: Without Delegation (Old Way)

```cpp
class Box {
    int width;
    int height;
public:
    Box() {
        width = 0;
        height = 0;
    }

    Box(int w, int h) {
        width = w;
        height = h;
    }
};
```

Here, both constructors initialize members — **duplicate code**.

---

### ✅ Example: With Delegation (Modern Way)

```cpp
class Box {
    int width;
    int height;
public:
    Box() : Box(0, 0) {            // delegating to another constructor
        // nothing else needed
    }

    Box(int w, int h) : width(w), height(h) { }
};
```

✔ `Box()` **calls** `Box(int, int)`
✔ Only one constructor actually performs initialization
✔ No duplication, simpler maintenance

---

## ⚙️ 2. How It Works

* Delegating constructor uses the **member initializer list** syntax:

  ```cpp
  ClassName(arguments)
  ```
* You can **only delegate to one other constructor**.
* You cannot mix delegation with base-class constructor calls in the same initializer list.

---

### ❌ Invalid Example (Mixing)

```cpp
class Derived : public Base {
public:
    Derived() : Base(1), Derived(2) { } // ❌ not allowed — can’t call both
};
```

You must choose **either** a base constructor **or** a delegation target, not both.

---

## 🧱 3. Realistic Example

```cpp
#include <string>

class Person {
    std::string name;
    int age;
public:
    Person(std::string n, int a) : name(n), age(a) {}
    Person(std::string n) : Person(n, 0) {}     // delegate to main constructor
    Person() : Person("Unknown", 0) {}          // delegate again
};
```

All constructors delegate to the most detailed one.
This is often called a **constructor chain**.

---

## 🧠 4. Why Use Delegating Constructors?

| Benefit         | Description                                                   |
| --------------- | ------------------------------------------------------------- |
| **Code reuse**  | Avoid repeating common initialization logic.                  |
| **Consistency** | All constructors behave uniformly.                            |
| **Maintenance** | Only one place to update when adding new members or defaults. |
| **Readability** | Makes the constructor flow explicit and organized.            |

---

## ⚡ 5. Delegation vs Inheritance Initialization

* **Delegation:** calls another constructor in the *same* class.
* **Inheritance:** calls a constructor from the *base* class.

You can use both — but not in the same initializer list.

Example:

```cpp
class Base {
public:
    Base(int id) {}
};

class Derived : public Base {
    int value;
public:
    Derived() : Base(0), value(0) {}     //base constructor
    Derived(int v) : Derived() { value = v; } //delegation
};
```

This is valid: the delegating constructor (`Derived(int)`) calls another constructor (`Derived()`), which in turn calls the base constructor.


---
# Enforcing Parameterized Construction

```cpp
class MyData {
public:
    MyData() = delete;                     // disallow empty construction
    MyData(int a, int b) : x(a), y(b) {}   // only this is valid
private:
    int x, y;
};

MyData m1;         // ❌ error
MyData m2(10, 20); // ✅ ok
```

## 🧱 1. What `= delete` Means

In your code:

```cpp
MyData() = delete;
```

This line **tells the compiler not to generate** a default constructor for `MyData`.
If someone tries to create an object with:

```cpp
MyData data;   // ❌ error: call to deleted constructor
```

the compiler **explicitly forbids it** — hence the error in your IDE:

> “Call to deleted constructor of 'MyData'”.

This is often used to **prevent invalid or undesired object creation**, for example:

* To enforce initialization with parameters.
* To disable copy or move operations.
* To prevent heap allocation or stack allocation, depending on design.


---

## ⚙️ 2. Why Delete Instead of Just Private?

Before C++11, people made constructors **private** to prevent access:

```cpp
private:
    MyData();  // declared but not defined
```

But this led to **linker errors** instead of **compiler errors**.

With `= delete`, you get a **clear compile-time error**.
It’s safer, cleaner, and explicit.

---

## 🧩 3. Rule of 0, 3, and 5 (C++ Object Lifetime Rules)

These rules describe when and how you should define or omit special member functions (like constructors, destructors, and assignment operators).

---

### 🧠 The Rule of 0 (C++11+)

> **If your class doesn’t manage resources manually (like dynamic memory, files, etc.), don’t define any special member functions.**

Let the compiler handle:

* Default constructor
* Copy constructor
* Copy assignment operator
* Move constructor
* Move assignment operator
* Destructor

**Rationale:** The compiler-generated ones are safe and efficient for simple data members (like `int`, `std::string`, etc.).

**Example:**

```cpp
struct Point {
    int x, y;    // POD-like
}; // compiler generates all special functions safely
```

---

### ⚙️ The Rule of 3 (Pre-C++11)

> **If you define one of the “big three”, you probably need all three:**

1. Copy constructor
2. Copy assignment operator
3. Destructor

Because defining one usually implies resource ownership — and the others must handle it too.

**Example:**

```cpp
class MyClass {
    int* data;
public:
    MyClass(int val) { data = new int(val); }
    ~MyClass() { delete data; }                     // 1. destructor
    MyClass(const MyClass& other) {                 // 2. copy constructor
        data = new int(*other.data);
    }
    MyClass& operator=(const MyClass& other) {      // 3. copy assignment
        if (this != &other) {
            *data = *other.data;
        }
        return *this;
    }
};
```

---

### ⚡ The Rule of 5 (C++11+)

> **If you define any of the “big five”, you likely need to define all of them:**

1. Destructor
2. Copy constructor
3. Copy assignment operator
4. Move constructor
5. Move assignment operator

Because move semantics introduced in C++11 add new ways to manage resource ownership efficiently.

**Example:**

```cpp
class Resource {
    int* ptr;
public:
    Resource(int v) : ptr(new int(v)) {}
    ~Resource() { delete ptr; }

    // copy
    Resource(const Resource& other) : ptr(new int(*other.ptr)) {}
    Resource& operator=(const Resource& other) {
        if (this != &other) *ptr = *other.ptr;
        return *this;
    }

    // move
    Resource(Resource&& other) noexcept : ptr(other.ptr) { other.ptr = nullptr; }
    Resource& operator=(Resource&& other) noexcept {
        if (this != &other) {
            delete ptr;
            ptr = other.ptr;
            other.ptr = nullptr;
        }
        return *this;
    }
};
```

---

## 📘 Summary Table

| Rule           | Era    | When to Apply                          | Key Idea                                      |
| -------------- | ------ | -------------------------------------- | --------------------------------------------- |
| **Rule of 0**  | C++11+ | If you don’t manage resources manually | Let compiler generate everything              |
| **Rule of 3**  | C++98  | If you manage copyable resources       | Define copy ctor, copy assignment, destructor |
| **Rule of 5**  | C++11+ | If you manage moveable resources       | Also define move ctor and move assignment     |
| **`= delete`** | C++11+ | To explicitly forbid a function        | Causes compile-time error if called           |

---

#  1. The “Sanitizing Rule” 

In modern C++ discussions, when someone mentions the **“sanitizing rule”**, they’re usually referring to a **design guideline** or **pattern hygiene rule** for special member functions and constructors — i.e. **to keep your class “clean” or “sanitized”** in how it manages resources and follows the “Rule of 0 / 3 / 5.”

It’s **not an official ISO C++ term**, but rather an **informal convention** meaning:

> *“A class should be sanitized — i.e., designed cleanly — so that it either requires no special member functions at all, or explicitly manages all of them correctly.”*

So the **sanitizing rule** in this sense is:

> Ensure your class is “sanitized” in its ownership semantics — no half-defined, inconsistent, or unsafe constructors/destructors.

---

### ✅ A “Sanitized” Class Example

```cpp
class MyData {
    int a, b;
public:
    MyData(int x, int y) : a(x), b(y) {}
    // no destructor, no copy/move — compiler-generated ones are fine
};
```

This class is **sanitized** under the **Rule of 0**:

* No raw pointers or manual resource management
* Compiler handles all copying and destruction safely

---

### ❌ An “Unsanitized” Class Example

```cpp
class MyData {
    int* data;
public:
    MyData(int val) { data = new int(val); }   // allocates
    // forgot destructor
};
```

Here, you have a **resource leak** — the destructor is missing.
The class is **unsanitized** — it violates Rule of 3 / Rule of 5.

So the *sanitizing rule* would tell you to either:

* Manage ownership fully (define destructor, copy, move properly), **or**
* Use RAII (like `std::unique_ptr<int>`) to **sanitize automatically**.

---

## 🧠 2. The “Sanitizers” (Compiler Tools)

There’s another, **formal and widely used** meaning of “sanitizing” in C++ — **runtime sanitizers** — tools that detect undefined or unsafe behavior.

These are compiler options that *instrument* your code to catch bugs at runtime.

### 🧰 Common Sanitizers

| Sanitizer                              | Purpose                                                               |
| -------------------------------------- | --------------------------------------------------------------------- |
| **AddressSanitizer (ASan)**            | Detects memory errors — buffer overflows, use-after-free, etc.        |
| **UndefinedBehaviorSanitizer (UBSan)** | Detects undefined C++ behaviors — invalid casts, divide by zero, etc. |
| **ThreadSanitizer (TSan)**             | Detects race conditions in multithreaded programs.                    |
| **MemorySanitizer (MSan)**             | Detects use of uninitialized memory.                                  |
| **LeakSanitizer (LSan)**               | Detects memory leaks.                                                 |

### Example usage:

```bash
g++ -fsanitize=address,undefined -g main.cpp -o main
./main
```

If your program mismanages memory or violates C++ rules, the sanitizer prints detailed runtime diagnostics.

---

## 🧮 3. Relationship Between the Two Meanings

| Aspect     | “Sanitizing Rule” (Design Hygiene)      | “Sanitizer” (Tool)                      |
| ---------- | --------------------------------------- | --------------------------------------- |
| Type       | Design principle                        | Compiler/runtime tool                   |
| Purpose    | Make classes safe by design             | Detect unsafe behavior during execution |
| Applies to | Code structure and object lifetime      | Runtime memory and logic                |
| Examples   | Rule of 0 / 3 / 5, deleted constructors | ASan, UBSan, TSan                       |

They complement each other:

* The **sanitizing rule** prevents bad code patterns.
* **Sanitizers** detect violations that slipped through.

---

## ✅ Summary

| Term                           | Meaning                                                                                                        |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------- |
| **Sanitizing Rule (informal)** | Design principle to keep classes “clean” — no partial ownership or inconsistent special members.               |
| **Goal**                       | Either rely entirely on compiler defaults (Rule of 0) or implement all relevant special members (Rule of 3/5). |
| **Formal Sanitizers**          | Runtime tools (ASan, UBSan, etc.) that detect bugs like memory leaks or undefined behavior.                    |
| **Key takeaway**               | “Sanitize” your code either by *correct design* or *runtime validation*.                                       |

---

