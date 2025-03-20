**TL;DR – Expression Statements**  

- An **expression statement** is simply an expression followed by a semicolon.  
- Used when you want to evaluate an expression for its side effect (like changing a value or printing), not for its return value.  
- Example:  
```cpp
int x{};
++x;            // expression statement with a side effect (increments x)
42;             // expression statement with no side effect (pointless)
printf("%d", x); // expression statement (calls a function)
```
👉 Most of your program’s actions (assignments, increments, function calls) are expression statements.