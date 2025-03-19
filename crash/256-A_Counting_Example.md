**TL;DR:**  
`CountIf` is a function object type that counts occurrences of a character in a string. It demonstrates how to implement and use function objects by defining a class with a custom function-call operator. Lambdas simplify this concept significantly.

- **Function Object Example** (`CountIf`):

```cpp
struct CountIf {
    CountIf(char x) : x{x} {}
    
    size_t operator()(const char* str) const {
        size_t index{}, result{};
        while (str[index]) {
            if (str[index] == x) result++;
            index++;
        }
        return result;
    }
private:
    const char x;
};

// Usage:
CountIf count_s{'s'};
size_t result = count_s("Sally sells seashells.");
```

- **Equivalent Free Function** (`count_if`):

```cpp
size_t count_if(char x, const char* str) {
    size_t index{}, result{};
    while (str[index]) {
        if (str[index] == x) result++;
        index++;
    }
    return result;
}

// Usage:
size_t result = count_if('s', "Sally sells seashells.");
```

**Key points:**

- Function objects allow partial application (fixing one argument's value).
- Lambdas offer a shorter, more concise alternative to writing function objects.