# Class:
<img width="1457" height="660" alt="image" src="https://github.com/user-attachments/assets/23f8e916-97b9-46f4-bf33-095dbb6a6647" />

---

##  **What is OOP in Python?**

**Object-Oriented Programming (OOP)** is a programming paradigm that organizes code using **objects** — reusable pieces that bundle **data** (attributes) and **behavior** (methods) together.

In Python, OOP is implemented mainly with **classes** and **objects**.

---

##  **What is a Class?**

A **class** is like a **blueprint** for creating **objects**.
An **object** is an **instance** of a class — a real piece of data built from that blueprint.

---

## ⚙️ **Key Parts of Classes**

| Part                  | Description                                                       |
| --------------------- | ----------------------------------------------------------------- |
| **`__init__` method** | The **constructor**; runs when you create an object.              |
| **`self` keyword**    | Refers to the **current object** itself.                          |
| **Attributes**        | Variables that store data for each object.                        |
| **Methods**           | Functions defined inside the class that act on the object’s data. |

---

## 🧵 **OOP Concepts in Python**

| Concept           | Meaning                                                                              |
| ----------------- | ------------------------------------------------------------------------------------ |
| **Encapsulation** | Bundling data (attributes) + behavior (methods) together.                            |
| **Inheritance**   | A class can **inherit** properties and methods from another class.                   |
| **Polymorphism**  | Different classes can have methods with the same name but different implementations. |
| **Abstraction**   | Hiding internal details and exposing only necessary parts.                           |

---

## ✅ **Inheritance Example**

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle started.")


# Car inherits from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Call parent constructor
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} car started.")


my_vehicle = Vehicle("Generic")
my_vehicle.start()  # Generic vehicle started.

my_car = Car("Honda", "Civic")
my_car.start()      # Honda Civic car started.
```

---

## ✅ **Polymorphism Example**

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())
# Woof!
# Meow!
```

---
# Constructor:


A **constructor** in Python is a special method that **runs automatically** when you **create an object** from a class.

Its job is to **initialize** the object’s **attributes**.

In Python, the constructor is always named:

```python
__init__(self, ...)
```

---

##  **Basic Example**

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # attribute
        self.age = age    # attribute

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# Create an object
p1 = Person("Alice", 30)

# Access attributes
print(p1.name)  # Alice
print(p1.age)   # 30

# Call method
p1.greet()      # Hello, my name is Alice and I am 30 years old.
```

---

##  **Key Points**

| Feature        | Description                                               |
| -------------- | --------------------------------------------------------- |
| **`__init__`** | The constructor method — runs when the object is created. |
| **`self`**     | Refers to the **current object** (instance).              |
| **Parameters** | You can pass arguments to initialize the object’s data.   |

---

##  **Default Values in Constructor**

You can set default values for parameters:

```python
class Person:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

p2 = Person()
print(p2.name)  # Unknown
print(p2.age)   # 0
```

---

# self

* `self` is **not a keyword** — it’s just a **convention**, but almost always used.
* It represents the **instance** (the specific object) **itself**.
* It must be the **first parameter** of **instance methods** (like `__init__` or other methods).
* Through `self`, each object keeps track of **its own data**.

---

##  **Why is `self` needed?**

Imagine you have a class `Car` and you create two cars: `car1` and `car2`.
Each should store **its own brand, model, speed, etc.**

`self` makes sure the **method or attribute** works on the **right object**.

---

##  **How it works**

When you do:

```python
car1 = Car()
car2 = Car()
```

and then call:

```python
car1.drive()
car2.drive()
```

Internally, Python does:

```python
Car.drive(car1)
Car.drive(car2)
```

So `self` is **automatically passed** as the first argument!

---

##  **Example to show `self` clearly**

```python
class Dog:
    def __init__(self, name):
        self.name = name   # attaches name to THIS object

    def bark(self):
        print(f"{self.name} says woof!")

dog1 = Dog("Max")
dog2 = Dog("Buddy")

dog1.bark()   # Max says woof!
dog2.bark()   # Buddy says woof!
```

➡️ Here:

* `self.name` is different for `dog1` and `dog2`.
* If you forget `self` → all objects would **share the same variable**, which breaks OOP.

---

##  **`self` is required for instance methods**

```python
class Example:
    def say_hello():  # ❌ wrong — missing self
        print("Hello!")

obj = Example()
# obj.say_hello()  # TypeError: missing 1 required positional argument: 'self'
```

➡️ The fix:

```python
class Example:
    def say_hello(self):  # ✅ correct
        print("Hello!")

obj = Example()
obj.say_hello()  # Hello!
```

---

##  **`self` vs class variables**

Sometimes, you see:

```python
class Example:
    count = 0  # class variable

    def __init__(self):
        self.value = 10  # instance variable
```

* `count` belongs to the **class** (shared by all instances).
* `self.value` belongs to the **object**.

---

##  **Can you use a different name instead of `self`?**

Yes, technically:

```python
class Test:
    def hello(this):
        print("Hi!")

t = Test()
t.hello()  # Hi!
```

…but don’t do this — `self` is the **standard** in Python.

---

##  **Where you see `self`**

| Where                              | Purpose                                                   |
| ---------------------------------- | --------------------------------------------------------- |
| **`__init__(self, …)`**            | Constructor: binds attributes to this object.             |
| **Methods: `def method(self, …)`** | Instance methods need to know *which* object called them. |
| **`self.attribute`**               | Create or access **object-specific** data.                |

---

##  **What about `@classmethod` and `@staticmethod`**

* **Instance methods** → `self`
* **Class methods** → `cls` (the class itself, not the object)
* **Static methods** → no `self` or `cls`

Example:

```python
class Example:
    def instance_method(self):
        print("I am an instance method")

    @classmethod
    def class_method(cls):
        print("I am a class method")

    @staticmethod
    def static_method():
        print("I am a static method")
```

---






















