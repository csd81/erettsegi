### ✅ **Summary of Regular Expression Patterns in C++**

Regular expressions (regex) are built from **patterns**, which define sets of strings that match a certain structure. The default grammar used by the STL is a modified **ECMAScript** regular expression grammar.

---

### ✅ **Key Elements of Regex Patterns**

---

### 1. **Character Classes**
These represent sets of characters:
| **Class** | **Matches**                       |
|-----------|-----------------------------------|
| `\d`      | Any digit                         |
| `\s`      | Any whitespace                    |
| `\w`      | Any alphanumeric (word) character |
| `\D`      | Any non-digit                     |
| `\S`      | Any non-whitespace                |
| `\W`      | Any non-word character            |

✅ **Custom Character Classes:**  
- Example: `[02468]` matches even digits.  
- Ranges like `[0-9a-fA-F]` match any hexadecimal digit.  
- Inversion using `[^...]` matches anything *not* in the set.  
  Example: `[^aeiou]` matches non-vowel characters.

---

### 2. **Examples of Regex Patterns (Table 15-8)**  
| **Regex**               | **Matches**                                                   |
|-------------------------|---------------------------------------------------------------|
| `\d\d\d-\d\d\d-\d\d\d\d`| An American phone number (e.g., `202-456-1414`)               |
| `\d\d:\d\d \wM`         | A time in `HH:MM AM/PM` format (e.g., `08:49 PM`)             |
| `\w\w\d\d\d\d\d\d`      | ZIP code with state prefix (e.g., `NJ07932`)                 |
| `\w\d-\w\d`             | Astromech droid ID (e.g., `R2-D2`)                            |
| `c\wt`                  | Three-letter words starting with c and ending with t (`cat`)  |

---

### 3. **Quantifiers (Table 15-9)**  
| **Quantifier** | **Meaning**                               |
|----------------|-------------------------------------------|
| `*`            | 0 or more occurrences                     |
| `+`            | 1 or more occurrences                     |
| `?`            | 0 or 1 occurrence (optional)              |
| `{n}`          | Exactly `n` occurrences                   |
| `{n,m}`        | Between `n` and `m` occurrences (inclusive)|
| `{n,}`         | At least `n` occurrences                  |

> Example: `c\w*t` matches words that start with `c` and end with `t`, with any number of word characters in between.

---

### 4. **Groups**
- Groups are created using parentheses `(...)`.  
- Groups are useful for extracting parts of a match and for applying quantifiers.  

> Example for a ZIP code:
```
(\w{2})?(\d{5})(-\d{4})?
```
- Group 1: Optional state code (`(\w{2})?`)  
- Group 2: ZIP code (`(\d{5})`)  
- Group 3: Optional four-digit suffix (`(-\d{4})?`)

---

### 5. **Other Special Characters (Table 15-10)**  
| **Character** | **Meaning**                                                     |
|---------------|-----------------------------------------------------------------|
| `X\|Y`        | Matches either `X` or `Y`                                       |
| `\Y`          | Escapes special character `Y` to use it literally               |
| `\n`          | Newline                                                         |
| `\r`          | Carriage return                                                 |
| `\t`          | Tab                                                             |
| `\0`          | Null character                                                  |
| `\xYY`        | The character represented by hexadecimal value `YY`             |

---

### 👉 **In short:**
Regex patterns combine **literal characters, character classes, quantifiers, groups, and special characters** to match and extract structured text.  
Let me know if you'd like a cheat sheet or real-world examples of regex patterns for common use cases!