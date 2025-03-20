### ✅ **Summary of String Search Methods in C++**

C++'s `std::string` class provides several search functions to locate substrings and characters, each with specific use cases. Depending on whether you need to search forward, backward, or for specific characters, you can choose the appropriate method.

---

### ✅ **Basic Search Methods**

#### 1. **`find`**:
- Finds the **first occurrence** of a substring or character.
- Returns `std::string::npos` if not found.
- Can accept a **position** argument to specify where to start searching.

> **Example (Listing 15-13):**
```cpp
std::string word("pizzazz");
REQUIRE(word.find("zz") == 2);      // "zz" found at index 2
REQUIRE(word.find("zz", 3) == 5);   // "zz" found at index 5 starting from position 3
REQUIRE(word.find("zaz") == 3);     // "zaz" found at index 3
REQUIRE(word.find('x') == std::string::npos); // 'x' not found
```

#### 2. **`rfind`**:
- Similar to `find`, but searches in **reverse** (from the end to the beginning).
  
> **Example (Listing 15-14):**
```cpp
REQUIRE(word.rfind("zz") == 5);     // "zz" found at index 5 (second-to-last "z")
REQUIRE(word.rfind("zz", 3) == 2);  // "zz" found at index 2 (searching from position 3)
REQUIRE(word.rfind("zaz") == 3);    // "zaz" found at index 3
REQUIRE(word.rfind('x') == std::string::npos); // 'x' not found
```

#### 3. **`find_first_of`**:
- Finds the **first character** that appears in the provided set (a string or a C-style string).
  
> **Example (Listing 15-15):**
```cpp
std::string sentence("I am a Zizzer-Zazzer-Zuzz");
REQUIRE(sentence.find_first_of("Zz") == 7);   // Finds 'Z' at index 7
REQUIRE(sentence.find_first_of("Zz", 11) == 14); // Finds 'Z' starting from position 11
REQUIRE(sentence.find_first_of("Xx") == std::string::npos); // 'X' and 'x' not found
```

---

### ✅ **Variants of `find_first_of`**
There are additional variations of `find_first_of` that let you customize the search further:

#### 4. **`find_first_not_of`**:
- Finds the **first character** that is **not** in the provided set.

#### 5. **`find_last_of`**:
- Similar to `find_first_of`, but searches **in reverse**.

#### 6. **`find_last_not_of`**:
- Similar to `find_first_not_of`, but searches **in reverse**.

---

### ✅ **Summary Table of Search Methods (Table 15-6)**

| **Method**                             | **Description**                                                                        |
|----------------------------------------|----------------------------------------------------------------------------------------|
| `find(s2, [p])`                        | Finds the first substring equal to `s2` starting from position `p` (defaults to 0).    |
| `rfind(s2, [p])`                       | Finds the last substring equal to `s2`, starting from position `p` (defaults to `npos`).|
| `find_first_of(s2, [p])`               | Finds the first character in `s2` in the string `s` from position `p`.                 |
| `find_first_not_of(s2, [p])`           | Finds the first character not in `s2` in the string `s` from position `p`.             |
| `find_last_of(s2, [p])`                | Finds the last character in `s2` in the string `s` starting from position `p`.         |
| `find_last_not_of(s2, [p])`            | Finds the last character not in `s2` in the string `s` starting from position `p`.     |

---

### 👉 **Key Takeaway:**
The choice between `find`, `rfind`, and the `find_first_of` family depends on:
- Whether you need to search **forward** or **reverse**.
- Whether you're looking for **exact matches** or characters from a set.
- The **position** from where to start searching.

These methods provide flexible ways to efficiently search through strings based on the application’s needs.