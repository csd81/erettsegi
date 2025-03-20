**TL;DR – continue Statements**  

- The `continue` statement skips the rest of the current loop iteration and jumps to the next iteration.  
- Example:  
```cpp
if (i == 21) {
   printf("*** ");
   continue;
}
printf("%d ", i);
```
- When `i` is `21`, it prints `***` and skips printing `21` itself, but continues looping.  
- Unlike `break`, which stops the loop entirely, `continue` just moves on to the next loop cycle.