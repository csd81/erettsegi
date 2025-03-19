**TL;DR:**  
Lambda expressions are concise, unnamed function objects defined directly where you need them. They don't add new functionality beyond traditional function objects but make creating short, one-time-use functions convenient.

Example:

```cpp
auto square = [](int x) { return x * x; };
square(5); // returns 25
```