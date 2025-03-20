**TL;DR – for Loops**  

- A **for loop** has three parts:  
  1. **Initialization** (runs once before the loop starts)  
  2. **Conditional** (checked before each iteration; loop continues if `true`)  
  3. **Iteration** (runs after each loop body execution)  

- Execution order:  
   1. Initialization  
   2. Conditional check  
   3. Loop body  
   4. Iteration expression  
   5. Repeat from step 2 until condition is `false`  

**Classic usage:**  
- Great for indexing arrays:  
```cpp
for (int i = 0; i < size; i++) {
   printf("%d: %d\n", i, array[i]);
}
```
- Example (Listing 8-23) prints each element of a Fibonacci array with its index.  

👉 **Takeaway:** The traditional `for` loop is powerful but can be verbose; range-based for loops are the modern, cleaner alternative.