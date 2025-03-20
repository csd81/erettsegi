### ✅ **Summary: Numeric Conversions in the STL**

The STL provides a set of functions for converting **between strings (or wstrings) and numeric types**, and vice versa. These conversions are handled by functions like `std::to_string`, `std::to_wstring`, `std::stoi`, `std::stod`, and others.

---

### ✅ **Converting Numbers to Strings**
- Use `std::to_string()` or `std::to_wstring()`.
- Overloads are available for all numeric types.

> **Example (Listing 15-17):**
```cpp
REQUIRE("8675309"s == std::to_string(8675309));
REQUIRE(L"109951.1627776"s == std::to_wstring(109951.1627776)); 
```

---

### ✅ **Converting Strings to Numbers**
- Use functions like:
  - `stoi()`, `stol()`, `stoll()` — convert to int, long, long long
  - `stoul()`, `stoull()` — convert to unsigned long, unsigned long long
  - `stof()`, `stod()`, `stold()` — convert to float, double, long double
- Optional parameters:
  - `p` — a `size_t*` to capture the position of the first unconverted character.
  - `b` — an integer representing the base (defaults to base 10, but can be set to 2, 8, 16, etc.).
- Throws:
  - `std::invalid_argument` if conversion isn’t possible.
  - `std::out_of_range` if the value is too large for the type.

---

### ✅ **Example (Listing 15-18):**
| **Test**                                           | **Example**                                                                                          |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Convert `"8675309"` to int                         | `std::stoi("8675309"s) == 8675309;`  ✅                                                               |
| Out-of-range conversion throws exception           | `std::stoi("1099511627776"s)` throws `std::out_of_range`                                             |
| Convert hexadecimal number with `stoul`            | `std::stoul("0xD3C34C3D"s, &last_character, 16)` returns `0xD3C34C3D` and sets `last_character = 10` |
| Partial string conversion                          | `std::stoul("42six"s, &last_character)` returns `42`; `last_character = 2`                           |
| Convert string to double                           | `std::stod("2.7182818"s)` returns `2.7182818`                                                       |

---

### ✅ **Quick Reference (Table 15-7)**:

| **Function**            | **Converts string `s` to**      |
|-------------------------|---------------------------------|
| `stoi(s, [p], [b])`     | `int`                           |
| `stol(s, [p], [b])`     | `long`                          |
| `stoll(s, [p], [b])`    | `long long`                     |
| `stoul(s, [p], [b])`    | `unsigned long`                 |
| `stoull(s, [p], [b])`   | `unsigned long long`            |
| `stof(s, [p])`          | `float`                         |
| `stod(s, [p])`          | `double`                        |
| `stold(s, [p])`         | `long double`                   |
| `to_string(n)`          | `std::string`                   |
| `to_wstring(n)`         | `std::wstring`                  |

---

### ✅ **Tip:**
> Boost also offers an alternative approach with `boost::lexical_cast` for type conversions, which can be more flexible and template-based.

---

👉 If you’d like, I can help write examples of using `boost::lexical_cast` or show error handling patterns for numeric conversions!