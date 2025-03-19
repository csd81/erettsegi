This passage describes three primary algorithms in C++'s `<regex>` library for working with regular expressions:

### 1. **Matching (`std::regex_match`)**
- Attempts to match the **entire** input string exactly against the given regular expression.
- Returns a boolean (`true` if the entire string matches, otherwise `false`).
- Can optionally fill a `std::match_results` object with detailed information about matches and submatches.
- Useful when you expect your entire string to conform exactly to a given regex pattern.

#### Syntax:
```cpp
bool matched = std::regex_match(str, results, regex, flags);
```

- `str`: Input string (or iterators for a half-open range).
- `results`: Optional `match_results` object containing the matched data.
- `regex`: Regular expression to match against.
- `flags`: Optional match flags (advanced usage).

#### Example:
```cpp
std::regex zip_regex{R"((\w{2})(\d{5})(-\d{4})?)"};
std::smatch results;

std::string zip = "NJ07936-3173";
bool matched = std::regex_match(zip, results, zip_regex);

// results[0] == "NJ07936-3173"
// results[1] == "NJ"
// results[2] == "07936"
// results[3] == "-3173"
```

### 2. **Searching (`std::regex_search`)**
- Attempts to find a match within a **portion** (or subset) of a string.
- Returns `true` if **any** portion of the string matches the regex, otherwise `false`.
- Useful for checking if a substring matching your regex pattern exists somewhere within a larger text.

#### Syntax:
```cpp
bool found = std::regex_search(str, results, regex, flags);
```

#### Example:
```cpp
std::regex zip_regex{R"((\w{2})(\d{5})(-\d{4})?)"};
std::string sentence = "The ZIP code is NJ07936-3173.";

bool matched = std::regex_match(sentence, zip_regex); // false
bool found = std::regex_search(sentence, zip_regex);  // true
```

### 3. **Replacing (`std::regex_replace`)**
- Replaces parts of the string that match the regular expression with a replacement string.
- Returns a new string with replacements applied.
- Can perform global replacements (all matches replaced).

#### Syntax:
```cpp
std::string result = std::regex_replace(str, regex, replacement);
```

#### Example:
```cpp
std::regex vowels_regex{"[aeiou]"};
std::string phrase = "queueing and cooeeing in eutopia";

std::string result = std::regex_replace(phrase, vowels_regex, "_");

// result == "q_____ng _nd c_____ng _n __t_p__"
```

### **Submatches & `match_results` Details:**
- Submatches correspond to parenthesized groups (`(group)`) in your regex.
- `match_results` stores the full match (at index 0), then each subsequent subgroup:
  - `results[0]`: Entire matched string.
  - `results[1]`: First captured subgroup.
  - `results[2]`: Second captured subgroup, and so forth.

#### Common methods of `match_results` (`std::smatch`):
| Operation             | Description                                 |
|-----------------------|---------------------------------------------|
| `empty()`             | Returns `true` if no match found.            |
| `size()`              | Number of submatches (including full match). |
| `length(i)`           | Length of submatch at index `i`.             |
| `position(i)`         | Starting position of submatch `i`.           |
| `str(i)`              | Returns matched substring at index `i`.      |
| `prefix()`            | Text before the match.                       |
| `suffix()`            | Text after the match.                        |

---

### Summary:
- Use **`regex_match`** when checking if the **entire** string matches a regex pattern.
- Use **`regex_search`** when you need to find a matching substring within a larger text.
- Use **`regex_replace`** when you need to substitute matches with another string.

These three functions provide powerful capabilities for manipulating text using regular expressions in C++.