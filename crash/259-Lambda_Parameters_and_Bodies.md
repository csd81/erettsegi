**TL;DR:**  
Lambda functions are callable objects with parameters and a body, similar to regular functions. You declare parameters and the body in lambdas using familiar syntax:

```cpp
[](int x) { return x * x; } // Squares x
```

Example usage:

```cpp
// 'transform' applies a lambda function to elements in an array
template <typename Fn>
void transform(Fn fn, const int* in, int* out, size_t length) {
    for (size_t i{}; i < length; i++) {
        out[i] = fn(in[i]);
    }
}

int main() {
    const size_t len{3};
    int base[]{1, 2, 3}, a[len], b[len], c[len];

    transform([](int x) { return 1; }, base, a, len);          // fills 'a' with 1
    transform([](int x) { return x; }, base, b, len);          // copies 'base' to 'b'
    transform([](int x) { return 10 * x + 5; }, base, c, len); // applies expression

    // Resulting arrays:
    // a: [1, 1, 1]
    // b: [1, 2, 3]
    // c: [15, 25, 35]
}
```

Lambdas can be passed as arguments to template functions, making your code concise, reusable, and expressive.