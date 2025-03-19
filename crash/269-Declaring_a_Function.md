Here's a clear, concise summary of this section on **declaring and using `std::function` in C++**:

---

## Declaring a `std::function`

`std::function` is a **class template** in C++ that can wrap any callable type (functions, lambdas, function objects) matching a specified signature.

### Declaration Syntax:
```cpp
std::function<return-type(arg-type-1, arg-type-2, ...)>
```

- **Example:**
```cpp
std::function<int(int, int)> func; // function taking two ints, returning int
```

---

## Empty Functions and `std::bad_function_call`

When a `std::function` is default-constructed (i.e., no callable object provided), it's in an **empty state**:

```cpp
std::function<void()> func; // empty function
```

If invoked without a valid callable, `std::function` throws a `std::bad_function_call` exception.

### Example of empty function behavior:
```cpp
#include <cstdio>
#include <functional>

int main() {
    std::function<void()> func; // empty function
    try {
        func(); // Invoking empty function throws exception
    } catch(const std::bad_function_call& e) {
        printf("Exception: %s", e.what()); // prints "Exception: bad function call"
    }
}
```

---

## Assigning Callable Objects to `std::function`

You can assign a callable object either at initialization or afterward:

### Example using initialization and assignment:
```cpp
#include <cstdio>
#include <functional>

void static_func() {
    printf("A static function.\n");
}

int main() {
    std::function<void()> func { [] { printf("A lambda.\n"); } }; // Initialize with lambda
    func(); // prints "A lambda."

    func = static_func; // Assign a static function
    func(); // prints "A static function."
}
```

- Initially assigned a lambda; later replaced by a static function.
- `std::function` can store and invoke different callable types seamlessly.

---

Let me know if you need any additional clarification or examples!