### ✅ **Summary of Predicates in Boost String Algorithms**

Boost String Algorithms provides a rich set of **predicates** in `<boost/algorithm/string/predicate.hpp>`. These predicates allow you to check relationships between strings or ranges (like starts with, ends with, contains, equality, etc.).  

Most predicates accept two ranges (`r1` and `r2`) and an optional element-comparison predicate (`p`). There are also **case-insensitive variants** (prefixed with `i`), like `istarts_with`.

---

### **Examples:**

#### 📜 **Example: starts_with & istarts_with (Listing 15-27)**
```cpp
std::string word("cymotrichous");
REQUIRE(starts_with(word, "cymo"));   // returns true
REQUIRE(istarts_with(word, "cYmO"));  // also true (case-insensitive)
```

---

#### 📜 **Example: all predicate (Listing 15-28)**
```cpp
std::string word("juju");
REQUIRE(all(word, [](auto c) { return c == 'j' || c == 'u'; }));
```
- `all` checks whether *every character* in the range satisfies the predicate.

---

### ✅ **Table of Available Predicates (Table 15-12)**

| **Predicate**                               | **Returns true if...**                                                                 |
|---------------------------------------------|----------------------------------------------------------------------------------------|
| `starts_with(r1, r2, [p])`                  | `r1` starts with `r2` (optional custom character comparison with `p`)                 |
| `istarts_with(r1, r2)`                      | `r1` starts with `r2` (case-insensitive)                                              |
| `ends_with(r1, r2, [p])`                    | `r1` ends with `r2`                                                                   |
| `iends_with(r1, r2)`                        | `r1` ends with `r2` (case-insensitive)                                                |
| `contains(r1, r2, [p])`                     | `r1` contains `r2`                                                                    |
| `icontains(r1, r2)`                         | `r1` contains `r2` (case-insensitive)                                                 |
| `equals(r1, r2, [p])`                       | `r1` is equal to `r2`                                                                 |
| `iequals(r1, r2)`                           | `r1` is equal to `r2` (case-insensitive)                                              |
| `lexicographical_compare(r1, r2, [p])`      | `r1` is lexicographically less than `r2`                                              |
| `ilexicographical_compare(r1, r2)`          | Lexicographic comparison ignoring case                                                |
| `all(r, [p])`                               | All elements of `r` satisfy predicate `p`                                             |

---

### 👉 **Key takeaway:**
Boost predicates let you easily test string relationships, with both case-sensitive and case-insensitive support, and can be combined with custom predicates (like lambdas) for maximum flexibility.

Let me know if you’d like help with practical use cases or writing templates that combine these predicates!