**TL;DR – goto Statements**  

- **`goto`** is an unconditional jump to a **label** (a named point in code).  
- Labels are simple identifiers ending with a colon and do nothing by themselves.  

**Example (Listing 8-31)**:  
```cpp
luke:
printf("I'm not afraid.\n");
yoda:
printf("You will be.");
```
Labels `luke` and `yoda` just name those lines; they don't affect execution.  

**Example (Listing 8-32)**:  
Uses `goto` to create messy "spaghetti" control flow.  
Execution jumps between `silent_bob`, `luke`, and `yoda` in a confusing way.  

**Modern C++ advice**:  
- Don’t use `goto`.  
- It makes code harder to read and maintain.  
- In C, `goto` was sometimes used for error-handling, but in C++ RAII makes that unnecessary.