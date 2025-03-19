Here's a clear and concise summary of the provided detailed section on **Lambda Captures** in C++:

---

## **Lambda Captures in C++**

Lambda captures let you inject external variables into the body of a lambda, influencing its behavior. You declare captures within square brackets `[]` before the lambda’s parameter list.

### **Basic Capture Syntax**

```cpp
[capture-list](parameters){ body }
```

- **Capture by Value:** (default behavior)
  - Copies captured variable into lambda scope.
- **Capture by Reference:**
  - Prefix captured variable with `&` to reference the original variable.

---

### **Named Capture by Value (default):**

Example:

```cpp
char to_count = 's';
auto lambda = [to_count](const char* str) {
    // can use to_count here
};
```

---

### **Named Capture by Reference:**

Capturing a variable by reference allows a lambda to modify the original variable outside its scope.

Example:

```cpp
size_t tally = 0;
auto lambda = [&tally](const char* str) {
    tally += 1; // modifies tally outside the lambda
};
```

---

### **Default Capture**

You can capture all automatic variables implicitly:

| Capture | Meaning                                |
|---------|----------------------------------------|
| `[=]`   | Default capture all by value           |
| `[&]`   | Default capture all by reference       |

#### Example (default capture by reference):

```cpp
auto lambda = [&](const char* str) {
    // all variables from outer scope captured by reference
};
```

#### Example (default capture by value):

```cpp
auto lambda = [=](const char* str) mutable {
    // all variables captured by value; must use mutable if you modify
};
```

---

### **Mutable Lambdas**

If you capture by value and want to modify captured variables, you must use `mutable`:

```cpp
size_t tally = 0;
auto lambda = [=](const char* str) mutable {
    tally += 1; // modifies lambda’s own copy, not outer tally
};
```

Note: Modifications to the lambda's copy do not affect the original variable.

---

### **Initializer Expressions (Init Capture)**

Allows defining and initializing new variables directly in the capture list:

```cpp
char to_count = 's';
auto lambda = [my_char = to_count](const char* str) {
    // use my_char instead of to_count
};
```

---

### **Capturing `this`**

When a lambda expression is defined within a member function of a class, you can capture the enclosing object (`this`):

- Capture by reference: `[this]`
- Capture by value: `[*this]`

Example:

```cpp
struct MyClass {
    int data{};
    auto make_lambda() {
        return [this]() { return data; };    // capture this by reference
        // or
        // return [*this]() { return data; }; // capture this by value
    }
};
```

---

### **Clarifying Examples (Quick Reference)**

| Capture Syntax    | Meaning                                              |
|-------------------|------------------------------------------------------|
| `[&]`             | Default capture all variables by reference           |
| `[=]`             | Default capture all variables by value               |
| `[&, i]`          | Capture all by reference; `i` by value               |
| `[=, &i]`         | Capture all by value; `i` by reference               |
| `[i, &j]`         | Capture `i` by value; `j` by reference               |
| `[i=j, &k]`       | Capture variable `j` by value as `i`; `k` by reference |
| `[this]`          | Capture enclosing object by reference                |
| `[*this]`         | Capture enclosing object by value (copy)             |

---

Let me know if you have further questions or need additional clarifications!