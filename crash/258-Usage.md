**TL;DR:**  
Lambda expressions have five components:

1. **Captures**: Variables from surrounding context, becoming member variables of the lambda object.
2. **Parameters**: Arguments passed when calling the lambda.
3. **Body**: Code executed by the lambda.
4. **Specifiers** *(optional)*: Such as `constexpr`, `mutable`, `noexcept`, or attributes like `[[noreturn]]`.
5. **Return Type** *(optional)*: Type returned by the lambda function.

Lambda syntax:

```cpp
[captures] (parameters) specifiers -> return_type { body }
```

Only **captures** and **body** are required; others are optional.

**Comparison with a function object:**

- Lambda captures ≈ class member variables set by constructor.
- Lambda parameters ≈ arguments of a class's function-call operator.
- Lambda body ≈ function-call operator's implementation.
- Lambda return type ≈ return type of the class's function-call operator.
- Lambda specifiers ≈ modifiers like `const` or `noexcept` on a function-call operator.