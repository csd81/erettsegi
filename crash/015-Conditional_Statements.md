Here’s a structured and clear summary of the **Conditional Statements** section you shared:

---

## **Conditional Statements in C++ — Summary**

### **1. What Are Conditional Statements?**
- Conditional statements let programs make decisions based on **Boolean expressions** (expressions that evaluate to `true` or `false`).
- Boolean expressions are often built using **comparison operators**.

---

### **2. Common Comparison Operators (Listing 1-2)**
| Operator  | Meaning                     |
|-----------|-----------------------------|
| `==`      | Equal to                    |
| `!=`      | Not equal to                |
| `>`       | Greater than                |
| `>=`      | Greater than or equal to    |
| `<`       | Less than                   |
| `<=`      | Less than or equal to       |

> Example (no output, just validation):
```cpp
int main() {
  int x = 0;
  42 == x; // equality check
  42 != x; // inequality check
  100 > x; // greater than check
  123 >= x; // greater than or equal to check
  -10 < x; // less than check
  -99 <= x; // less than or equal to check
}
```

---

### **3. Basic if Statement**
> Syntax:
```cpp
if (boolean-expression) statement;
```
- If the Boolean expression is `true`, the statement runs; otherwise, it’s skipped.

- You can execute multiple statements using braces `{}` to create a **compound statement**:
```cpp
if (boolean-expression) {
  statement1;
  statement2;
  // more statements
}
```

---

### **4. if-else and else if Statements (Listing 1-3)**
> Syntax:
```cpp
if (boolean-expression-1) statement-1
else if (boolean-expression-2) statement-2
else statement-3
```
- The program checks each Boolean expression in order:
  - If the first condition is true, it executes `statement-1` and stops checking.
  - If not, it checks the next `else if` condition, and so on.
  - If none of the conditions are true, the `else` block (if present) executes.
- Only one block will run — they are mutually exclusive.

---

### **5. Example Program (Listing 1-4)**
```cpp
#include <cstdio>

int main() {
  int x = 0;
  if (x > 0) printf("Positive.");
  else if (x < 0) printf("Negative.");
  else printf("Zero.");
}
```
> Output:
```
Zero.
```
- Try changing `x` to other values and observe how the program prints "Positive.", "Negative.", or "Zero." based on the conditions.

---

### **6. Note on main()**
> `main()` can omit a return statement — it will automatically return `0` by default.

---

If you’d like, I can create a short interactive quiz to help practice writing `if-else` statements — would you like to try that?