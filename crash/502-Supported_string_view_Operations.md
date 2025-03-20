### ✅ **Summary of Supported `std::string_view` Operations**

The `std::string_view` class provides many of the same operations as a `const std::string&`, making it a flexible and efficient way to work with immutable character sequences.

---

### ✅ **Shared Methods Between `std::string` and `std::string_view`:**

| **Category**    | **Methods**                                                                                          |
|-----------------|------------------------------------------------------------------------------------------------------|
| **Iterators**   | `begin`, `end`, `rbegin`, `rend`, `cbegin`, `cend`, `crbegin`, `crend`                              |
| **Element Access** | `operator[]`, `at()`, `front()`, `back()`, `data()`                                               |
| **Capacity**    | `size()`, `length()`, `max_size()`, `empty()`                                                        |
| **Search**      | `find()`, `rfind()`, `find_first_of()`, `find_last_of()`, `find_first_not_of()`, `find_last_not_of()`|
| **Extraction**  | `copy()`, `substr()`                                                                                 |
| **Comparison**  | `compare()`, `operator==`, `operator!=`, `operator<`, `operator>`, `operator<=`, `operator>=`        |

---

### ✅ **Unique `string_view`-specific methods:**
- `remove_prefix(n)`: Removes the first `n` characters from the view.
- `remove_suffix(n)`: Removes the last `n` characters from the view.

---

### 📜 **Example (Listing 15-20)**:
```cpp
std::string_view view("previewing");

view.remove_prefix(3);   // view now points to "viewing"
view.remove_suffix(3);   // view now points to "preview"
```
- `remove_prefix(3)` makes the view start from the fourth character.
- `remove_suffix(3)` shortens the view by trimming characters from the end.

---

### 👉 **Key takeaway:**
`std::string_view` offers efficient string-like operations without copying or allocating memory, and it allows easy modification of what part of the string is being viewed using `remove_prefix` and `remove_suffix`.

Let me know if you’d like to see a quick reference card or real-life use cases for `string_view`!