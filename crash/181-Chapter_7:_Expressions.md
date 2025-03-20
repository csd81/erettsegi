## Chapter 7: Expressions (C++)

### Introduction to Expressions

Expressions form the heart of programming languages, and C++ is no exception. An **expression** in C++ is any valid combination of operators, variables, literals, and function calls that computes to a value. Expressions are critical, as they're fundamental building blocks that control logic, arithmetic operations, and decision-making processes within code.

---

### Categories of Expressions

In C++, expressions are broadly categorized as:

- **Arithmetic Expressions:** Handle numeric computations (`+`, `-`, `*`, `/`, `%`)
- **Relational Expressions:** Perform comparisons (`<`, `>`, `<=`, `>=`, `==`, `!=`)
- **Logical Expressions:** Deal with boolean logic (`&&`, `||`, `!`)
- **Assignment Expressions:** Assign values to variables (`=`, `+=`, `-=`, `*=`, `/=`, etc.)
- **Increment/Decrement Expressions:** Modify the value of variables (`++`, `--`)
- **Bitwise Expressions:** Manipulate individual bits (`&`, `|`, `^`, `~`, `<<`, `>>`)
- **Conditional Expressions:** Ternary conditional operator (`?:`)
- **Comma Expressions:** Allow multiple expressions in a sequence separated by commas (`,`)

---

### Arithmetic Expressions

Arithmetic expressions in C++ involve numeric computations:

```cpp
int result = (10 + 5) * 2; // Evaluates to 30
```

C++ follows a well-defined precedence and associativity order, where multiplication/division has higher precedence than addition/subtraction. Parentheses alter this order explicitly.

---

### Relational and Logical Expressions

These expressions evaluate to Boolean values (`true` or `false`):

```cpp
bool comparison = (a > b); // true if a is greater than b
bool logical = (x > 10) && (y < 20); // true if both conditions hold
```

Logical expressions are fundamental in controlling flow in conditionals (`if`, `while`, `for`) and decision-making logic.

---

### Assignment Expressions

Assignment expressions involve assigning computed values to variables:

```cpp
int a;
a = 5; // Assigns 5 to a

a += 10; // Equivalent to a = a + 10, result: a is now 15
```

Assignment operators like `+=`, `-=`, `*=`, `/=`, `%=` are concise ways to perform operations and assign results back to the same variable.

---

### Increment/Decrement Expressions

Increment (`++`) and decrement (`--`) expressions modify a variable's value by one:

```cpp
int counter = 5;
counter++; // counter is now 6
--counter; // counter is now back to 5
```

They can be **prefix** or **postfix**, affecting evaluation differently:

- **Prefix (`++x`, `--x`)**: The variable is incremented or decremented before being evaluated.
- **Postfix (`x++`, `x--`)**: The variable is evaluated first, then modified.

Example:

```cpp
int x = 10;
int y = x++; // y = 10, then x becomes 11
int z = ++x; // x becomes 12, then z = 12
```

---

### Bitwise Expressions

Bitwise expressions allow direct manipulation of individual bits within an integer type. Operators include:

- `&` (bitwise AND)
- `|` (bitwise OR)
- `^` (bitwise XOR)
- `~` (bitwise NOT, unary operator)
- `<<` (left shift)
- `>>` (right shift)

Example:

```cpp
int a = 6;   // 0110 in binary
int b = 12;  // 1100 in binary
int c = a & b; // 0100 (4 in decimal)
int d = a | b; // 1110 (14 in decimal)
```

These expressions are used extensively in low-level programming, including embedded systems, graphics, cryptography, and performance-critical applications.

---

### Conditional Expressions (Ternary Operator)

Conditional expressions use the ternary operator `?:`, providing a concise way to represent conditional logic:

```cpp
int max = (a > b) ? a : b; // Assigns a if a>b, else b
```

This simplifies basic if-else assignments into compact one-liners.

---

### Comma Expressions

Comma expressions combine multiple expressions into a single statement, evaluating from left to right. The value of the entire expression is the last one evaluated:

```cpp
int x;
int y = (x = 5, x + 2); // x is assigned 5, y becomes 7
```

Though less common, they are particularly helpful in `for` loops and certain initialization sequences.

---

### Operator Precedence and Associativity

Operator precedence and associativity determine the order in which expressions are evaluated. A simplified precedence hierarchy is:

1. Parentheses `()`
2. Unary operators (`++`, `--`, `!`, `~`)
3. Multiplicative operators (`*`, `/`, `%`)
4. Additive operators (`+`, `-`)
5. Shift operators (`<<`, `>>`)
6. Relational operators (`<`, `<=`, `>`, `>=`)
7. Equality operators (`==`, `!=`)
8. Bitwise AND (`&`)
9. Bitwise XOR (`^`)
10. Bitwise OR (`|`)
11. Logical AND (`&&`)
12. Logical OR (`||`)
13. Conditional (`?:`)
14. Assignment (`=`, `+=`, `-=`, etc.)
15. Comma (`,`)

Associativity determines evaluation when operators have equal precedence:

- **Left-to-right** associativity: most binary operators (e.g., `+`, `-`, `*`, `/`).
- **Right-to-left** associativity: assignment (`=`), unary (`!`, `~`, `++`, `--` prefix).

---

### Evaluation Order and Side Effects

Understanding evaluation order is crucial because some expressions have **side effects**, altering states beyond returning a value. For instance, assignments and increments affect state.

Example with side effects:

```cpp
int i = 0;
int result = (++i) + (i++); 
// Undefined behavior in older standards, defined explicitly in later standards
```

Avoid code relying on evaluation order where it's ambiguous, to maintain clarity and portability.

---

### Type Conversions in Expressions

Expressions can implicitly or explicitly convert data types:

- **Implicit conversions**: Automatically handled by C++:
```cpp
double x = 10; // 10 implicitly converts to 10.0
```

- **Explicit conversions (casts)**: Programmer-initiated:
```cpp
double y = 7.3;
int z = static_cast<int>(y); // z becomes 7
```

---

### Constant Expressions (`constexpr`)

C++ supports compile-time evaluated expressions through the keyword `constexpr`, improving efficiency and performance:

```cpp
constexpr int size = 10 * 5; // evaluated at compile time
```

---

### Conclusion

Expressions in C++ are foundational, representing how the program performs calculations, makes decisions, and manages control flow. Mastering expressions means understanding operator precedence, evaluation order, side effects, and data conversions—critical skills to writing robust, efficient, and clear code in C++.

