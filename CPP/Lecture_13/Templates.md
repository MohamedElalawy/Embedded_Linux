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

A **variadic template** in C++ is a type of template that can take a **variable number of template arguments**. This feature, introduced in **C++11**, allows you to write functions and classes that can accept any number of parameters — similar to how functions like `printf()` work in C.

---

### 🧩 Basic Idea

Normally, a class or function template has a fixed number of parameters:

```cpp
template<typename T1, typename T2>
void print(T1 a, T2 b) {
    std::cout << a << " " << b << std::endl;
}
```

But what if you want to print *any number* of arguments?
That’s where **variadic templates** come in.

---

### 🧠 Syntax

```cpp
template<typename... Args>
void print(Args... args) {
    // function body
}
```

* `typename... Args` → a **parameter pack**, which can hold zero or more types.
* `args...` → a **function parameter pack**, which holds the actual arguments.
* The `...` (ellipsis) is called the **pack expansion operator** — it “expands” the parameter pack.

---

### 🧾 Example

Here’s a recursive example to print all arguments:

```cpp
#include <iostream>

void print() {}  // base case (stops recursion)

template<typename T, typename... Args>
void print(T first, Args... rest) {
    std::cout << first << " ";
    print(rest...); // recursive expansion
}

int main() {
    print(1, 2.5, "hello", 'A');
}
```

**Output:**
<img width="905" height="682" alt="image" src="https://github.com/user-attachments/assets/5411c762-43a4-4f71-854f-6c36bbfc0d9f" />


<img width="1397" height="798" alt="image" src="https://github.com/user-attachments/assets/1327cff5-a2a2-4f7f-9add-e670a5673850" />

---

### 🧰 Modern Alternative (C++17 Fold Expressions)

Starting with **C++17**, you can use **fold expressions** to simplify variadic templates:

```cpp
template<typename... Args>
void print(Args... args) {
    ((std::cout << args << " "), ...);
}
```
<img width="877" height="628" alt="image" src="https://github.com/user-attachments/assets/f70dd74c-e308-4d43-828a-b4f1330543e2" />

This does the same thing, but without recursion — it “folds” the pack using the `<<` operator.

---

### ⚙️ Uses of Variadic Templates

* Writing **generic wrappers** (e.g., logging or forwarding functions)
* Implementing **tuple-like containers** (`std::tuple` uses them internally)
* Perfect forwarding in **variadic constructors**
* Custom printf-like functions

---
# Class example that uses a **variadic template**, similar to how `std::tuple` works internally:

---

## 🧱 1. Basic Concept — Variadic Class Template

A **variadic class template** can take a variable number of **type parameters**.
Here’s a minimal version:

```cpp
// Base case: empty tuple
template<typename... Types>
class MyTuple;  // forward declaration

// Specialization for an empty pack
template<>
class MyTuple<> {};

// Recursive definition
template<typename Head, typename... Tail>
class MyTuple<Head, Tail...> {
public:
    Head head;
    MyTuple<Tail...> tail;  // recursively contains the rest

    MyTuple(Head h, Tail... t) : head(h), tail(t...) {}
};
```

This defines a tuple-like structure that can hold any number of elements.

---

## 🧪 2. Example Usage

```cpp
#include <iostream>
#include <string>

int main() {
    MyTuple<int, double, std::string> t(42, 3.14, "Hello");

    std::cout << t.head << "\n";          // prints 42
    std::cout << t.tail.head << "\n";     // prints 3.14
    std::cout << t.tail.tail.head << "\n"; // prints Hello
}
```

This is **recursive composition**:

* `MyTuple<int, double, std::string>` contains
  → `int head` and a `MyTuple<double, std::string> tail`,
  which contains
  → `double head` and a `MyTuple<std::string> tail`, and so on.

---

## 🔍 3. Accessing Elements — Recursive Helper

We can add a helper to access the nth element, like `std::get<N>()`.

```cpp
// Base case for get<0>
template<std::size_t N, typename Head, typename... Tail>
auto& get(MyTuple<Head, Tail...>& tuple) {
    if constexpr (N == 0)
        return tuple.head;
    else
        return get<N - 1>(tuple.tail);
}
```

Now you can do:

```cpp
int main() {
    MyTuple<int, double, std::string> t(1, 2.5, "test");
    std::cout << get<0>(t) << ", " << get<1>(t) << ", " << get<2>(t) << "\n";
}
```

**Output:**

```
1, 2.5, test
```

---

## 🧠 4. Key Takeaways

| Concept            | Explanation                                                 |
| ------------------ | ----------------------------------------------------------- |
| `typename... Args` | A **template parameter pack** — holds multiple types        |
| `Args... args`     | A **function parameter pack** — holds multiple arguments    |
| `tail(t...)`       | **Pack expansion** — expands multiple arguments recursively |
| `if constexpr`     | Used to handle base cases at compile-time cleanly (C++17+)  |

---

## ⚙️ 5. Real-World Example

`std::tuple`, `std::pair`, and many parts of the STL (like `std::make_shared`) use **variadic templates** internally to support arbitrary numbers of types and arguments efficiently.

---

---

# Full Example: Compile-Time Factorial Using Templates

<img width="1457" height="916" alt="image" src="https://github.com/user-attachments/assets/a3ef2276-0837-4081-bf29-5ee172db7a96" />


---

### 🧠 **Explanation**

1. **Template Recursion**

   * Each instantiation of `Factorial<N>` references `Factorial<N-1>`.
   * The compiler recursively generates templates until it reaches a base case.

2. **Base Cases**

   * `Factorial<0>` and `Factorial<1>` are explicitly specialized to stop recursion.
   * Both return `1`.

3. **Compile-Time Evaluation**

   * The keyword `constexpr` means the compiler evaluates the result at **compile time**, not runtime.
   * So, no recursive calls are made when the program runs — only the final constants are printed.

---

### 💡 **Program Output**

```
Factorial of 0: 1
Factorial of 1: 1
Factorial of 5: 120
Factorial of 10: 3628800
```

---

### 🏗️ **Alternative (Cleaner C++14/17 Version)**

In modern C++, you can achieve the same compile-time result with a simple `constexpr` function:

```cpp
#include <iostream>

constexpr unsigned long long factorial(unsigned int n) {
    return (n <= 1) ? 1 : n * factorial(n - 1);
}

int main() {
    std::cout << "Factorial of 10: " << factorial(10) << std::endl;
}
```

✅ This is **easier to read**,
✅ Still computed **at compile time**,
✅ And avoids template recursion depth limits.

---

Would you like me to extend this example to show **SFINAE or `enable_if`** usage with templates (for example, restricting factorial to integral types only)?



---
<img width="1760" height="775" alt="image" src="https://github.com/user-attachments/assets/f8ee49ae-8c23-4916-a155-60cb40c9cecb" />

Great — the image you shared outlines several **C++ Standard Library topics and features** to review. Here’s a **brief, structured explanation** of each one grouped by their category (as in your slide).

---

## 🧮 Standard Library Algorithms

The “Standard Library – Part 1 & 2” sections cover core C++ STL algorithms and containers.

### 1. **Iterators**

* Provide a **general way to access elements** of containers (like pointers).
* Enable traversal of container elements without exposing internal structure.
* Types include `input`, `output`, `forward`, `bidirectional`, and `random_access`.

### 2. **Sequence Containers**

* Maintain elements in a **linear order**.
* Examples: `std::vector`, `std::deque`, `std::list`.
* Support operations like insertion, deletion, and traversal.

### 3. **Sequence Views (C++20)**

* Non-owning, lightweight **views** into sequences.
* Example: `std::span`, `std::string_view`.
* Useful for passing subranges efficiently without copying data.

### 4. **Associative Containers**

* Store elements in **key–value** or **sorted key** order.
* Examples: `std::set`, `std::map`, `std::multiset`, `std::multimap`.
* Usually implemented as balanced trees.

### 5. **Algorithms Introduction**

* Core set of **generic algorithms** in `<algorithm>` and `<numeric>`.
* Examples: `std::sort`, `std::find`, `std::count`, `std::accumulate`.

### 6. **Container Traversal**

* Ways to iterate through containers (via loops, iterators, or algorithms).
* Often combined with range-based `for` and lambda functions.

### 7. **Minimum / Maximum**

* Functions: `std::min`, `std::max`, `std::min_element`, `std::max_element`.
* Used for finding extreme values in a collection.

### 8. **Existence Queries / Finding Elements**

* Search operations like `std::find`, `std::find_if`, `std::binary_search`.
* Used to check if certain elements exist in a container.

### 9. **Comparing Ranges**

* Algorithms like `std::equal`, `std::lexicographical_compare`.
* Useful for comparing two sequences element-by-element.

### 10. **Copying and Reordering**

* Algorithms like `std::copy`, `std::swap_ranges`, `std::reverse`, `std::rotate`.
* Allow rearranging elements efficiently.

### 11. **Changing / Removing Elements**

* `std::replace`, `std::remove`, `std::unique`.
* Modify or eliminate certain elements based on a condition.

### 12. **Numeric Operations**

* Found in `<numeric>`: `std::accumulate`, `std::inner_product`, `std::partial_sum`.

### 13. **Sorted Sequence Operations**

* Functions that assume sorted data: `std::binary_search`, `std::merge`, `std::set_union`.

### 14. **Binary Heap Operations**

* Support for heap-based structures: `std::make_heap`, `std::push_heap`, `std::pop_heap`.

### 15. **Random Numbers**

* Use `<random>` header: `std::mt19937`, `std::uniform_int_distribution`, etc.
* Modern, type-safe way to generate random data.

---

## 🔍 “Searching for” Topics

### 1. **`final`**

* Keyword that prevents inheritance or method overriding.

```cpp
class Base final {};  // cannot be derived from
virtual void foo() final;  // cannot be overridden further
```

### 2. **`std::bind`**

* Creates a **callable object** by binding arguments to a function.

```cpp
auto f = std::bind(add, 2, 3);  // f() calls add(2,3)
```

* Often replaced by **lambdas** in modern C++.

### 3. **Template `.hpp`**

* `.hpp` is a **header file extension** used for C++ templates.
* Templates must be defined in headers so the compiler can instantiate them during compilation.

### 4. **`std::stringstream`**

* Used for **string-based input/output**.

```cpp
std::stringstream ss;
ss << "Value: " << 10;
std::string s = ss.str();
```

### 5. **`<chrono>` timers**

* Provides **time measurement** utilities.

```cpp
auto start = std::chrono::high_resolution_clock::now();
// ... code ...
auto end = std::chrono::high_resolution_clock::now();
std::chrono::duration<double> diff = end - start;
```

### 6. **Random Numbers**

* Uses the `<random>` header (already mentioned above).
* Replace old `rand()` with modern, seedable generators.

---

## ⚙️ C++17 Features

### 1. **`std::variant`**

* A **type-safe union** — can hold one of several types.

```cpp
std::variant<int, std::string> v = "Hello";
v = 10;
```

### 2. **`std::optional`**

* Represents an **optional value** (may or may not exist).

```cpp
std::optional<int> x = 42;
if (x) std::cout << *x;
```

### 3. **`std::any`**

* A **type-erased container** for any type (stores arbitrary objects safely).

```cpp
std::any a = 5;
a = std::string("Hi");
```

---

👉 **Substitution Failure Is Not An Error**

This is a *fundamental concept* in C++ **templates and metaprogramming**.
Let’s go step by step 👇

---

## 🧩 1. What Is SFINAE?

When the compiler tries to **instantiate** a template, it substitutes the provided template arguments into the template definition.
If this substitution causes an **error**, C++ normally would fail compilation — **but** with SFINAE, that particular template is **silently ignored** instead of producing a hard error.

In short:

> During template argument substitution, if a substitution fails, that template is discarded from overload resolution — it’s **not** a compile error.

This allows **function overloading and template specialization** based on *whether a certain expression or type is valid*.

---

## ⚙️ 2. Why It Exists

SFINAE enables **compile-time introspection** — letting you write templates that only participate in overload resolution if certain conditions are met.

It’s what makes things like:

* `std::enable_if`
* Type traits (`std::is_integral`, `std::is_class`, etc.)
* Generic libraries (e.g., STL algorithms, Boost)
  work smoothly.

---

## 🧠 3. Basic Example

Let’s say we want two different versions of a function — one for types that have a nested type `value_type`, and one for those that don’t.

### Without SFINAE:

This would cause a compilation error when the compiler tries to access `T::value_type` for types that don’t have it.

### With SFINAE:

We can safely choose the valid one.

```cpp
#include <iostream>
#include <type_traits>

template <typename T>
auto has_value_type(int) -> decltype(typename T::value_type(), std::true_type{}) {
    return std::true_type{};
}

template <typename T>
std::false_type has_value_type(...) {
    return std::false_type{};
}

struct WithValueType {
    using value_type = int;
};

struct WithoutValueType {};

int main() {
    std::cout << has_value_type<WithValueType>(0) << std::endl; // true
    std::cout << has_value_type<WithoutValueType>(0) << std::endl; // false
}
```

👉 The first overload uses `decltype(typename T::value_type(), std::true_type{})`.
If `T::value_type` doesn’t exist, that substitution fails — but **does not cause a compiler error** thanks to SFINAE — the compiler just uses the second overload.

---

## ⚙️ 4. Modern SFINAE with `std::enable_if`

SFINAE is often implemented using `std::enable_if` (in `<type_traits>`):

```cpp
#include <iostream>
#include <type_traits>

template <typename T>
typename std::enable_if<std::is_integral<T>::value>::type
print(T value) {
    std::cout << "Integral: " << value << std::endl;
}

template <typename T>
typename std::enable_if<std::is_floating_point<T>::value>::type
print(T value) {
    std::cout << "Floating-point: " << value << std::endl;
}

int main() {
    print(5);      // calls the integral version
    print(3.14);   // calls the floating-point version
}
```

Here:

* If `T` is integral, the first function is valid.
* If `T` is floating-point, the second one is valid.
* Substitution failure of `enable_if` removes the wrong overload.

---

## 🚀 5. Modern Alternative: Concepts and `requires`

Since **C++20**, SFINAE is often replaced by **concepts** and the `requires` clause — much cleaner and more readable:

```cpp
#include <iostream>
#include <concepts>

void print(std::integral auto value) {
    std::cout << "Integral: " << value << std::endl;
}

void print(std::floating_point auto value) {
    std::cout << "Floating-point: " << value << std::endl;
}

int main() {
    print(42);
    print(3.14);
}
```

✅ No messy `enable_if`,
✅ No manual `decltype`,
✅ Compiler diagnostics are clearer.

---

## 🧾 Summary

| Concept                | Meaning                                                  |
| ---------------------- | -------------------------------------------------------- |
| **SFINAE**             | Substitution Failure Is Not An Error                     |
| **When?**              | During template argument substitution                    |
| **Purpose**            | To enable selective overloads or template specialization |
| **Typical Tool**       | `std::enable_if`, `decltype`, `void_t`, etc.             |
| **Modern Replacement** | C++20 Concepts and `requires` clauses                    |

---

[PlaList 3zema](https://youtube.com/playlist?list=PL1_C6uWTeBDF4oRLtCP_NqFtzP1DrQC6f&si=GwH47JjEXITglZr8)

