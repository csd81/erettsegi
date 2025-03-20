**TL;DR – Range-Based for Loops**  

- A **range-based for loop** lets you iterate over arrays or range objects without manual indexing.  
- Syntax:  
```cpp
for (auto element : range_expression) {
   // use element
}
```
- It simplifies looping compared to traditional loops.  
- Custom ranges need:  
  - A `begin()` and `end()` method.  
  - An iterator with `operator!=`, `operator++`, and `operator*`.  

**Example:**  
- `FibonacciRange` with `FibonacciIterator` lets you iterate over Fibonacci numbers up to a limit.  
- Under the hood, the compiler turns the range-based for loop into a traditional loop with `begin()`, `end()`, and iterator comparisons.  

👉 **Bottom line:** Cleaner and more readable for loops, especially useful for reusable libraries or consuming complex ranges.