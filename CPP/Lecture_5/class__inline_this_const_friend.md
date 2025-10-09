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
