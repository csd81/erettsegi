**TL;DR – break Statements**  

- The `break` statement immediately exits the closest enclosing loop or `switch`.  
- In loops, it stops execution and jumps to the code after the loop.  
- Example from Listing 8-29:  
```cpp
if (i == 21) {
   printf("*** ");
   break;
}
```
- When `i` is `21`, the program prints `***` and stops the loop entirely — no further values are printed.  
- Unlike `continue`, which skips to the next iteration, `break` halts the loop completely.