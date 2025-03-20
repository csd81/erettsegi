### ✅ **TL;DR: The Structure of a Basic C++ Program**

---

### **1. Writing Your First C++ Program**
- Create a source file (human-readable text) named **`main.cpp`**.
- Example:
```cpp
#include <cstdio>  // u: include the cstdio library

int main() {       // v: program entry point
  printf("Hello, world!");  // w: prints text to the console
  return 0;       // x: exit code (0 = success)
}
```
- Save this file as **`main.cpp`**.

---

### **2. What Happens**
- The program prints:
```
Hello, world!
```
- The file extension **`.cpp`** is used for C++ source files.

---

### **3. Program Entry Point**
- **`main()`** is the starting point of every C++ program.  
- Inside `main()`, functions like `printf()` are called to perform tasks.  
- Returning **`0`** from `main()` signals to the operating system that the program finished successfully.  
- If you omit `return 0;`, the compiler will automatically assume it for `main()`.

---

### **4. External Function: `printf`**
- The `printf` function is provided by the **`cstdio`** library, not defined in your code — that’s why you use `#include <cstdio>`.

---

> Want me to show how to compile and run this from the terminal on Linux, Windows, or Mac step-by-step? I can help with that if you’d like!