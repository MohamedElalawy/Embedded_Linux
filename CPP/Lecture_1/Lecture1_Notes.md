
# Static Linking vs Dynamic Linking 
---

### 🔧 Static Linking

* **Definition**: All code, including external libraries, is compiled and **linked into a single executable** at **compile time**.

* **Example**:

  ```cpp
  g++ main.cpp -o my_app -lstaticlib
  ```

* **Characteristics**:

  * All required code is bundled into the executable.
  * No need for external `.so` (Linux) or `.dll` (Windows) files at runtime.
  * Executable file is **larger**.
  * Runs **independently** of the development environment.

* **Pros**:

  * Simpler deployment (only one file).
  * Slightly faster at runtime (no need to resolve symbols).
  * No dependency issues at runtime.

* **Cons**:

  * Larger file size.
  * Updating a library requires **rebuilding** the executable.

---

### ⚙️ Dynamic Linking

* **Definition**: The program is compiled, but **external libraries are linked at runtime**, not during compilation.

* **Example**:

  ```cpp
  g++ main.cpp -o my_app -ldynamiclib
  ```

* **Also requires**:

  * The shared library (`.so` on Linux, `.dll` on Windows) to be **present during runtime**.

* **Characteristics**:

  * Executable is **smaller**.
  * Code for external libraries is **loaded into memory when needed**.

* **Pros**:

  * Smaller executable size.
  * Easy to **update or patch** libraries without recompiling the app.

* **Cons**:

  * Extra care needed for **library versions**.
  * Risk of **runtime errors** if the required library isn't found or is incompatible.

---

### Summary Table

| Feature             | Static Linking         | Dynamic Linking            |
| ------------------- | ---------------------- | -------------------------- |
| Linking Time        | Compile Time           | Run Time                   |
| Executable Size     | Larger                 | Smaller                    |
| Speed               | Slightly Faster        | Slightly Slower            |
| Dependency Handling | No runtime dependency  | Needs external libraries   |
| Library Update      | Requires recompilation | Update without recompiling |

---

### When to Use Each

* Use **static linking** when:

  * You want a **portable, self-contained executable**.
  * You want to **avoid versioning issues**.

* Use **dynamic linking** when:

  * You're managing **many apps using the same libraries**.
  * You want **flexibility to update libraries** independently.

---

