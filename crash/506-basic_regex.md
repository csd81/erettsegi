### ✅ **Summary of `std::basic_regex` and Regex Algorithms in C++**

The **`std::basic_regex`** class template (from `<regex>`) represents a regular expression pattern.  
- Most often, you’ll use `std::regex` (alias for `std::basic_regex<char>`) or `std::wregex` (for `wchar_t`).
- Patterns are best passed as raw string literals (e.g., `R"(pattern)"`) to avoid escape character clutter.

---

### ✅ **Key `std::basic_regex` methods:**
| Method                  | Description                                                    |
|-------------------------|----------------------------------------------------------------|
| `assign(s)`             | Reassigns the pattern.                                         |
| `mark_count()`          | Returns the number of capture groups in the pattern.           |
| `flags()`               | Returns the syntax flags used at construction.                |

---

### ✅ **Example (Listing 15-23)**  
```cpp
std::regex zip_regex{ R"((\w{2})?(\d{5})(-\d{4})?)" };
REQUIRE(zip_regex.mark_count() == 3);
```
Creates a regex for ZIP codes with 3 possible groups.

---

## ✅ Regex Algorithms

### 1. **Matching** (`std::regex_match`)  
- Tries to match the **entire string** against the regex.
- Usage:
```cpp
regex_match(str, [match_results], regex, [flags]);
```
- The `match_results` object stores:
  - The entire match at `results[0]`
  - Subgroups in subsequent elements.
  - Use methods like `empty()`, `size()`, `length(i)`, `str(i)`, `prefix()`, and `suffix()` to access results.

> 🔎 Example (Listing 15-24):
```cpp
std::regex zip_regex{ R"((\w{2})(\d{5})(-\d{4})?)" };
std::smatch results;
regex_match("NJ07936-3173", results, zip_regex);
```
- Results hold the entire match and groups:
  - `[0]` = "NJ07936-3173"  
  - `[1]` = "NJ"  
  - `[2]` = "07936"  
  - `[3]` = "-3173"

---

### 2. **Searching** (`std::regex_search`)  
- Searches for a **partial match** within the string.
- Perfect for strings that contain a regex match somewhere inside.

> Example (Listing 15-25):
```cpp
std::regex zip_regex{ R"((\w{2})(\d{5})(-\d{4})?)" };
std::string sentence = "The string NJ07936-3173 is a ZIP Code.";
REQUIRE_FALSE(std::regex_match(sentence, zip_regex));   // entire string doesn't match
REQUIRE(std::regex_search(sentence, zip_regex));        // part of the string does match
```

---

### 3. **Replacing** (`std::regex_replace`)  
- Replaces occurrences of the regex with a specified replacement string.

> Example (Listing 15-26):
```cpp
std::regex vowels{ "[aeiou]" };
std::string phrase = "queueing and cooeeing in eutopia";
auto result = std::regex_replace(phrase, vowels, "_");
// Result: "q_____ng _nd c_____ng _n __t_p__"
```

---

### ✅ Helpful classes:
| Class            | Purpose                                                       |
|------------------|---------------------------------------------------------------|
| `std::smatch`    | `std::match_results` specialization for `std::string`.        |
| `std::sub_match` | Represents a single submatch; exposes `length()`, `str()`.    |

---

### ✅ Note:
- **Boost.Regex** (in `<boost/regex.hpp>`) mirrors STL regex support but with additional flexibility.
- **Boost.Xpressive** allows defining regexes directly in C++ expressions, offering compile-time checks but using a different syntax than standard regexes.

---

👉 Let me know if you’d like help writing custom regex patterns or tips on using `regex_replace` formatting options!