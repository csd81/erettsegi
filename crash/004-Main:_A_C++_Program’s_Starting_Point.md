### ✅ **TL;DR: Main — A C++ Program’s Starting Point**

---

### **1. The `main` Function**
- Every C++ program begins execution in the **`main`** function (the **entry point**).
- When the program runs, the code inside `main()` is executed.

---

### **2. What Happens Inside `main()`**
- Example:
```cpp
int main() {
  printf("Hello, world!");  // Prints to console (function from cstdio)
  return 0;                // Exit code sent to the operating system
}
```
- The call to `printf()` prints `"Hello, world!"` to the console.
- The program then **returns 0** to signal successful completion.

---

### **3. Exit Codes**
- **0** = Success  
- Any other integer = an error or special exit condition.  
- The `return 0;` line is optional; if omitted, it defaults to 0 in `main()`.

---

### **4. `printf` Comes From a Library**
- The `printf` function is not part of your program — it comes from the **`cstdio`** library, which you include with:
```cpp
#include <cstdio>
```

---

> Want me to explain the difference between `main()` returning `int` and the significance of non-zero exit codes for scripting and automation? I can show real examples if you’d like!