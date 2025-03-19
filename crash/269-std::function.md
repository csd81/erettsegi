Here's a concise summary of the provided section on **`std::function`**:

---

## `std::function` Overview:

The `std::function` class template (from `<functional>`) is a versatile, polymorphic wrapper for storing **callable objects** uniformly. Essentially, it acts as a general-purpose, type-safe **function pointer** capable of storing:

- Static functions
- Lambdas
- Function objects (functors)

### Key Features of `std::function`:

- **Polymorphic invocation:**  
  Call functions uniformly without knowing their implementation.

- **Assignable, movable, and copyable:**  
  Easily copy or move function wrappers around.

- **Empty state:**  
  Can represent a "no-function" state, similar to a pointer set to `nullptr`. Invoking an empty function throws a `std::bad_function_call`.

### Example usage:

```cpp
#include <functional>
#include <cstdio>

void static_function() { printf("Static function.\n"); }

int main() {
    std::function<void()> func;          // Empty std::function
    func = static_function;              // Assign static function
    func();                              // Invoke function without knowing implementation

    func = [] { printf("Lambda.\n"); };  // Assign lambda
    func();                              // Polymorphic call
}
```

---

Let me know if you'd like further explanation or examples!