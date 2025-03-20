### ✅ **Summary: Ownership, Usage, and Efficiency of `std::string_view`**

- **`std::string_view`** is a lightweight, non-owning view of a character sequence.  
- Since it **does not own** the data, you must ensure that the lifetime of the string it refers to **outlives the string_view**.

---

### ✅ **Common Use Case**
- `std::string_view` is commonly used as a **function parameter** when working with immutable character sequences.
- It allows efficient handling of input without copying or allocating memory.

> **Example (Listing 15-21):**
```cpp
size_t count_vees(std::string_view my_view) {
    size_t result{};
    for (auto letter : my_view)
        if (letter == 'v') result++;
    return result;
}
```
- Takes a `string_view`, iterates over its characters, and counts the occurrences of `'v'`.

---

### ✅ Comparison with `const std::string&`
> While `std::string_view` can often be replaced by `const std::string&`, there are key differences:
- If you pass a **`std::string`** object, both `const std::string&` and `string_view` behave similarly.
- If you pass a **string literal**:
  - `const std::string&` requires constructing a temporary `std::string` (copying and potentially allocating).
  - `std::string_view` just points to the literal (cheap and efficient — no copy, no allocation).

---

### 👉 **In short:**
Use `std::string_view` when you need a read-only view of character data, especially in function parameters — it reduces unnecessary copies and allocations, particularly for string literals or substrings.