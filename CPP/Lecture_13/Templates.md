In **C++**, a **template** is a powerful feature that allows you to write **generic code**—code that works with any data type without rewriting it for each type.

Think of templates as **blueprints** for creating functions or classes that can operate on different types.

---

### 🔹 Types of Templates in C++

1. **Function Templates**

   * Allow functions to work with different data types.

   ```cpp
   #include <iostream>
   using namespace std;

   template <typename T>
   T add(T a, T b) {
       return a + b;
   }

   int main() {
       cout << add(3, 4) << endl;       // int
       cout << add(3.5, 2.1) << endl;  // double
   }
   ```

   ✅ The same function `add` works for both `int` and `double`.

---

2. **Class Templates**

   * Allow classes to handle multiple data types.

   ```cpp
   #include <iostream>
   using namespace std;

   template <typename T>
   class Box {
   private:
       T value;
   public:
       Box(T v) : value(v) {}
       T getValue() { return value; }
   };

   int main() {
       Box<int> intBox(123);
       Box<string> strBox("Hello");

       cout << intBox.getValue() << endl;
       cout << strBox.getValue() << endl;
   }
   ```

   ✅ The same class `Box` works for `int`, `string`, or any type.

---

3. **Template Specialization**

   * You can create a special version of a template for a specific type.

   ```cpp
   #include <iostream>
   using namespace std;

   template <typename T>
   class Printer {
   public:
       void print(T value) {
           cout << value << endl;
       }
   };

   // Specialization for char*
   template <>
   class Printer<char*> {
   public:
       void print(char* value) {
           cout << "String: " << value << endl;
       }
   };

   int main() {
       Printer<int> p1;
       Printer<char*> p2;

       p1.print(42);
       p2.print("Hello Templates");
   }
   ```

   ✅ Normal template handles `int`, but specialized template handles `char*`.

---

### 🔹 Why use Templates?

* **Code Reuse** → No need to write the same logic for `int`, `float`, `string`, etc.
* **Type Safety** → Unlike macros, templates are checked by the compiler.
* **Flexibility** → Functions and classes can be generalized.

---


## Is tempates the smart way instead of function overloading????

 **templates can often replace function overloading**, but it depends on the situation. Let’s break it down:

---

### 🔹 Function Overloading

With **function overloading**, you write multiple versions of the same function, one for each type you need:

```cpp
#include <iostream>
using namespace std;

int add(int a, int b) {
    return a + b;
}

double add(double a, double b) {
    return a + b;
}

string add(string a, string b) {
    return a + b;
}

int main() {
    cout << add(3, 4) << endl;          // int
    cout << add(2.5, 3.1) << endl;      // double
    cout << add("Hello ", "World") << endl; // string
}
```

⚠️ Problem: You must manually write each version → **code repetition**.

---

### 🔹 Function Templates

With **templates**, you write the function **once**, and the compiler generates the correct version when needed:

```cpp
#include <iostream>
using namespace std;

template <typename T>
T add(T a, T b) {
    return a + b;
}

int main() {
    cout << add(3, 4) << endl;          // int
    cout << add(2.5, 3.1) << endl;      // double
    cout << add(string("Hello "), string("World")) << endl; // string
}
```

✅ Advantage:

* Less code
* More scalable (works with any type that supports `+`)
* Type safe

---

### 🔹 When to Use Which?

* **Use Templates**

  * When the function logic is **identical** for all types.
  * Example: `max`, `min`, `swap`, `sort`, `vector` (STL).

* **Use Overloading**

  * When behavior is **different depending on the type**.
  * Example: Printing `int` vs printing `char*` vs printing `bool` → you might want special handling.

---

👉 So yes, **templates are a smarter, more general solution** than function overloading, but **overloading is still useful when types need unique behavior**.


---


---

## 🔹 1. Templates are *compile-time blueprints*

* A **template itself is not code**.
* It’s just a **pattern (blueprint)** that tells the compiler how to generate real functions or classes when you use them.

👉 This process is called **template instantiation**.

Example:

```cpp
template <typename T>
T square(T x) {
    return x * x;
}

int main() {
    square(5);       // instantiates square<int>
    square(2.5);     // instantiates square<double>
}
```

Here:

* `square(5)` → compiler generates a function: `int square(int x)`.
* `square(2.5)` → compiler generates: `double square(double x)`.

So the compiler **copies the template** and replaces `T` with the actual type.

---

## 🔹 2. Templates are resolved at **compile-time**

That means:

* The compiler checks the code inside the template only **when it’s instantiated**.
* If you never use the template with a certain type, no code is generated for it.

Example:

```cpp
template <typename T>
T divide(T a, T b) {
    return a / b;
}

int main() {
    cout << divide(10, 2) << endl; // OK, instantiates divide<int>
    // cout << divide("a", "b");   // ❌ Compile error only if used
}
```

* If you never call `divide("a", "b")`, the compiler won’t complain.
* If you do call it, the compiler checks if `"a" / "b"` makes sense (it doesn’t).

---

## 🔹 3. Function Template vs Class Template Instantiation

* **Function templates**: Each call with a *new type* generates a new function.
* **Class templates**: Each time you declare a class with a *new type parameter*, the compiler generates a new class.

```cpp
template <typename T>
class Box {
    T value;
public:
    Box(T v) : value(v) {}
    T get() { return value; }
};

int main() {
    Box<int> b1(42);       // generates a Box<int> class
    Box<double> b2(3.14);  // generates a Box<double> class
}
```

Here, the compiler literally creates **two different classes**:

* `class Box<int> { int value; ... };`
* `class Box<double> { double value; ... };`

---

## 🔹 4. Template Compilation Stages

1. **Definition** → You write the template.
2. **Declaration** → The compiler stores the blueprint.
3. **Instantiation** → When you use the template with a specific type, the compiler generates real code.
4. **Compilation** → The generated code is compiled like normal functions/classes.

---

## 🔹 5. Code Bloat (a side effect)

Since each type creates a new function/class, templates can cause **code bloat**.
Example:

```cpp
square(5);    // makes square<int>
square(2.5);  // makes square<double>
square(3.0f); // makes square<float>
```

The compiler generates **3 different functions**, even though they look the same.
(This is why STL uses a lot of **inline** and **small functions**.)

---

## 🔹 6. Advanced Concepts

* **Template Specialization** → customize for certain types.
* **Non-type template parameters** → templates can take numbers/constants.

  ```cpp
  template <int N>
  int fixedArray() {
      return N;
  }

  int main() {
      cout << fixedArray<5>() << endl;  // prints 5
  }
  ```
* **SFINAE (Substitution Failure Is Not An Error)** → lets you write templates that only compile for types that “make sense.”
* **Concepts (C++20)** → constraints on templates (like type requirements).

---

✅ **Summary**

* Templates = compile-time blueprints.
* Compiler generates real code when you use them → instantiation.
* Saves code duplication, but can increase binary size (code bloat).
* Very powerful → STL (`vector`, `map`, `sort`, etc.) is almost entirely templates.

---
<img width="798" height="255" alt="image" src="https://github.com/user-attachments/assets/1982c2ab-0cab-4a69-a69d-97a6c1e531c7" />

Let’s break this down — in the image, you have:

```cpp
template <typename T>
class Data {
public:
    explicit Data(T data) : data(std::move(data)) {
        std::cout << data << std::endl;
    }

    T data;
};
```

So, why use the **`explicit`** keyword here?

---

### 🔹 1. What `explicit` does

`explicit` prevents the compiler from using your constructor for **implicit type conversions**.

Normally, C++ allows a **single-argument constructor** to be used for *automatic conversions* like this:

```cpp
class Data {
public:
    Data(int x) { std::cout << x << std::endl; }
};

void print(Data d) { }

int main() {
    print(5); // ✅ Implicit conversion: 5 → Data(5)
}
```

Here, the compiler automatically converts the `int` value `5` into a `Data` object.

---

### 🔹 2. What happens **with `explicit`**

When you mark the constructor as `explicit`, **that automatic conversion is disallowed**:

```cpp
class Data {
public:
    explicit Data(int x) { std::cout << x << std::endl; }
};

void print(Data d) { }

int main() {
    // print(5); ❌ Error: no implicit conversion
    print(Data(5)); // ✅ OK, explicit construction
}
```

So now, the user must **explicitly** create a `Data` object.

---

### 🔹 3. Why it’s important in **templates**

When writing templates, you often don’t know what `T` will be.
If the constructor is *not explicit*, C++ might silently perform unintended conversions between unrelated types.

Example:

```cpp
Data<std::string> d = "hello"; // ✅ Implicit conversion from const char* → std::string → Data<std::string>
```

If your constructor wasn’t `explicit`, this kind of *chained implicit conversion* could happen even when you didn’t intend it.
By marking it **explicit**, you make it safer:

```cpp
Data<std::string> d("hello"); // ✅ Explicit
Data<std::string> d = "hello"; // ❌ Error — no implicit conversion
```

---

### ✅ Summary

| Without `explicit`                 | With `explicit`                       |
| ---------------------------------- | ------------------------------------- |
| Allows implicit type conversions   | Disables implicit conversions         |
| Can lead to unintended conversions | Forces clear, explicit construction   |
| Often OK for simple types          | Recommended for template constructors |

---

So in short:

> `explicit` is used here to **prevent automatic type conversions** when constructing `Data<T>` objects — a good practice for template classes where type safety and clarity matter.

---

## template method inside a template class?? when we need a generic function inside the template class:
<img width="1242" height="798" alt="image" src="https://github.com/user-attachments/assets/31c01aad-c7f7-40ca-b113-23977d94183e" />


```cpp
#include <bits/stdc++.h>


template <typename T> 
class Data {
public:
    explicit Data(T data) : data(std::move(data)) {
        std::cout << data << std::endl;
    }
    T data;

    // report→ generic
    template <typename U> 
    void report(U info) { 
        std::cout << info << std::endl; 
    }
};

int main() {

    std::cout << "\n=== Template Class Example ===" << std::endl;
    
    // Creating Data objects with different types
    Data<int> intData(100);
    Data<std::string> stringData("Template Class Data");
    
    std::cout << "\n=== Template Method Example ===" << std::endl;
    
    // Using the template method 'report' with different types
    intData.report("Reporting integer data:");
    intData.report(3.14159);
    
    stringData.report("Reporting string data:");
    stringData.report('X');
    
    return 0;
}
```

Template is metadata, and Metadata is data that describes another data.


---
---
# Template specialization:

**Template specialization** is one of the most powerful and interesting features in C++.
It lets you **customize the behavior** of a template for a *specific data type* (or set of types), while keeping the same general template for all others.

Let’s break it down clearly 👇

---

## 🔹 1. The Problem: One Size Doesn’t Always Fit All

A **template** is a general blueprint — it works for any type.

Example:

```cpp
#include <iostream>
using namespace std;

template <typename T>
class Printer {
public:
    void print(T value) {
        cout << "Value: " << value << endl;
    }
};
```

This works fine for `int`, `double`, etc.:

```cpp
Printer<int> p1;
p1.print(10);   // Value: 10
```

But what happens for something like `char*` (C-style string)?

```cpp
Printer<char*> p2;
p2.print("Hello");
```

✅ It prints `Value: Hello` — but that’s **only by chance**, since `cout` knows how to handle `char*`.
However, sometimes you’ll want **special behavior** — maybe to show:

```
String: Hello
```

That’s where **specialization** comes in.

---

## 🔹 2. What is Template Specialization?

Template specialization lets you **override** the generic version of a template for a **specific type**.

---

### ✅ Example: Class Template Specialization

```cpp
#include <iostream>
using namespace std;

template <typename T>
class Printer {
public:
    void print(T value) {
        cout << "General type: " << value << endl;
    }
};

// 👇 Specialization for const char*
template <>
class Printer<const char*> {
public:
    void print(const char* value) {
        cout << "String: " << value << endl;
    }
};

int main() {
    Printer<int> p1;
    p1.print(42);          // uses general template

    Printer<const char*> p2;
    p2.print("Hello");     // uses specialized version
}
```

🧠 What happens:

* For `int`, the compiler instantiates the **generic template**.
* For `const char*`, it finds the **specialized version** and uses that instead.

---

### ✅ Example: Function Template Specialization

You can do the same with **function templates**.

```cpp
#include <iostream>
using namespace std;

template <typename T>
void show(T value) {
    cout << "General: " << value << endl;
}

// Specialization for const char*
template <>
void show<const char*>(const char* value) {
    cout << "String: " << value << endl;
}

int main() {
    show(10);        // General: 10
    show("Hello");   // String: Hello
}
```

---

## 🔹 3. Types of Specialization

| Type                                          | Description                                                     |
| --------------------------------------------- | --------------------------------------------------------------- |
| **Full specialization**                       | You define the template for one exact type (e.g., `T = int`).   |
| **Partial specialization (for classes only)** | You define it for a subset of cases (e.g., pointer types `T*`). |
| **Function specialization**                   | Special handling for a specific type in a function template.    |

---

### ✅ Example: Partial Specialization (only for class templates)

You can’t partially specialize **functions**, only **classes**.

```cpp
#include <iostream>
using namespace std;

template <typename T>
class Data {
public:
    void show() { cout << "General type" << endl; }
};

// 👇 Partial specialization for pointers
template <typename T>
class Data<T*> {
public:
    void show() { cout << "Pointer type" << endl; }
};

int main() {
    Data<int> d1;
    Data<int*> d2;

    d1.show();  // General type
    d2.show();  // Pointer type
}
```

---

## 🔹 4. Why use Template Specialization?

✅ Advantages:

* Customize template behavior for specific types.
* Avoid code duplication while still handling special cases.
* Commonly used in **STL**, **type traits**, and **meta-programming**.

---

## 🔹 5. Real-World Example (from `<type_traits>`)

C++ standard library uses template specialization heavily.

Example (simplified version of `std::is_pointer`):

```cpp
template <typename T>
struct is_pointer {
    static constexpr bool value = false;
};

// Specialized for pointer types
template <typename T>
struct is_pointer<T*> {
    static constexpr bool value = true;
};

int main() {
    cout << is_pointer<int>::value << endl;   // 0
    cout << is_pointer<int*>::value << endl;  // 1
}
```

---

## ✅ Summary

| Concept                    | Meaning                                                              |
| -------------------------- | -------------------------------------------------------------------- |
| **General template**       | Works for all types                                                  |
| **Full specialization**    | Override for one exact type                                          |
| **Partial specialization** | Override for a pattern of types (e.g., pointers, arrays)             |
| **Why use it?**            | To give certain types custom behavior while keeping the rest generic |

---


#  Default Template Parameters:

Just like function parameters can have **default values**,
template parameters can also have **default types or values**.

That means if you **don’t specify** a type when using the template,
the compiler will **use the default one** automatically.

---

## 🧩 Example 1: Default Type in Class Template

```cpp
#include <iostream>
using namespace std;

template <typename T = int>
class Data {
public:
    T value;
    Data(T v) : value(v) {}
    void show() { cout << value << endl; }
};

int main() {
    Data<> d1(10);        // ✅ Uses default type int
    Data<double> d2(5.5); // ✅ Uses double explicitly

    d1.show(); // 10
    d2.show(); // 5.5
}
```

🧠 **Explanation:**

* If you write `Data<>`, it means `Data<int>` because `T` defaults to `int`.
* You can override it anytime: `Data<float>`, `Data<string>`, etc.

---

## 🔹 Example 2: Multiple Template Parameters (with defaults)

You can give defaults to **some or all** template parameters.

```cpp
template <typename T = int, typename U = double>
class Pair {
public:
    T first;
    U second;
    Pair(T a, U b) : first(a), second(b) {}
    void show() { cout << first << ", " << second << endl; }
};

int main() {
    Pair<> p1(1, 2.5);        // T=int, U=double
    Pair<int, char> p2(3, 'A'); // T=int, U=char

    p1.show(); // 1, 2.5
    p2.show(); // 3, A
}
```

⚠️ **Rule:**
Once you start giving default parameters, all following ones must also have defaults.

✅ This works:

```cpp
template <typename T = int, typename U = double>
```

❌ This does not:

```cpp
template <typename T = int, typename U>  // error: U must also have a default
```

---

## 🔹 Example 3: Default Non-Type Template Parameter

Templates can also take **non-type parameters**, such as constants, which can have defaults too:

```cpp
#include <iostream>
using namespace std;

template <typename T = int, int size = 5>
class Array {
public:
    T data[size];
    void fill(T value) {
        for (int i = 0; i < size; ++i)
            data[i] = value;
    }
    void print() {
        for (int i = 0; i < size; ++i)
            cout << data[i] << " ";
        cout << endl;
    }
};

int main() {
    Array<> a1;       // T=int, size=5
    Array<float, 3> a2; // T=float, size=3

    a1.fill(10);
    a2.fill(1.1f);

    a1.print(); // 10 10 10 10 10
    a2.print(); // 1.1 1.1 1.1
}
```

---

## 🔹 Example 4: Default Parameters in Function Templates

Default parameters can also be used in **function templates**:

```cpp
#include <iostream>
using namespace std;

template <typename T = double>
T add(T a, T b) {
    return a + b;
}

int main() {
    cout << add(1.5, 2.5) << endl; // Uses default type double
    cout << add<int>(1, 2) << endl; // Uses explicit int
}
```

---

## ✅ Summary

| Feature                            | Description                                               | Example                                            |
| ---------------------------------- | --------------------------------------------------------- | -------------------------------------------------- |
| **Default type**                   | Provide fallback for missing template argument            | `template <typename T = int>`                      |
| **Multiple defaults**              | All parameters after the first default must have defaults | `template <typename T = int, typename U = double>` |
| **Default non-type**               | Provide default constant value                            | `template <typename T = int, int N = 5>`           |
| **Works with classes & functions** | Supported in both                                         | ✅                                                  |

---

💡 **Pro tip:**
Default template parameters are widely used in the **STL**, e.g.:

```cpp
std::map<int, std::string, std::less<int>, std::allocator<std::pair<const int, std::string>>>
```

You usually just write:

```cpp
std::map<int, std::string>  // uses default comparator (std::less) and allocator
```

---


#  Variadic Template:

A **variadic template** is a template that can take **a variable number of template parameters or function arguments**.
Think of it as a way to write functions or classes that accept *any number of types or values*.

It was introduced in **C++11**.

---

## 🧩 Example 1: Variadic Function Template

```cpp
#include <iostream>
using namespace std;

// Base case: no arguments
void print() { 
    cout << "End of recursion" << endl; 
}

// Variadic template
template <typename T, typename... Args>
void print(T first, Args... rest) {
    cout << first << endl;
    print(rest...);  // Recursive unpack
}

int main() {
    print(1, 2.5, "Hello", 'A');
}
```

🔎 **Output:**

```
1
2.5
Hello
A
End of recursion
```

🧠 How it works:

* `Args...` → called a **parameter pack** (it holds zero or more template parameters).
* `rest...` → expands the pack (unpacks it).
* Recursion ends when no arguments remain.

---

## 🧩 Example 2: Fold Expressions (C++17)

Instead of recursion, **C++17** added **fold expressions** to simplify variadic templates.

```cpp
#include <iostream>
using namespace std;

template <typename... Args>
auto sum(Args... args) {
    return (args + ...);  // fold expression
}

int main() {
    cout << sum(1, 2, 3, 4, 5) << endl;  // 15
}
```

🧠 `(... + args)` → expands to `(((1 + 2) + 3) + 4) + 5`.

---

## 🧩 Example 3: Variadic Class Template

You can also define classes that take multiple types:

```cpp
#include <iostream>
#include <tuple>
using namespace std;

template <typename... Args>
class MyTuple {
public:
    tuple<Args...> data;
    MyTuple(Args... args) : data(args...) {}

    void print() {
        cout << "Tuple size = " << sizeof...(Args) << endl;
    }
};

int main() {
    MyTuple<int, double, string> t(1, 3.14, "Hello");
    t.print();  // Tuple size = 3
}
```

Here, `MyTuple<int, double, string>` automatically becomes `tuple<int, double, string>` internally.

---

## 🔹 Key Concepts

* **Parameter pack:**
  `typename... Args` → declares a pack of types.
  `Args... args` → declares a pack of variables.

* **Pack expansion:**
  `f(args...)` → expands to `f(arg1, arg2, arg3, ...)`.

* **sizeof...(Args):**
  Gives the number of arguments in the pack.

---

## 🔹 Real-World Use Cases

* **STL containers / utility classes** (`std::tuple`, `std::variant`, `std::apply`).
* **Perfect forwarding** (e.g., `std::make_unique`, `std::make_shared`).
* **Generic logging functions**.

---

✅ **Summary**

* Variadic templates = templates with **variable number of arguments**.
* Implemented with **parameter packs** (`Args...`).
* Handled by **recursion** (C++11/14) or **fold expressions** (C++17).
* Widely used in **STL, metaprogramming, and generic utilities**.

---


