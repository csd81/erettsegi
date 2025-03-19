Here's a concise summary of the **`partial_sort`** and **`partial_sort_copy`** algorithms in the C++ Standard Library:

---

## 🎯 **`partial_sort` (`<algorithm>` header)**

The `partial_sort` algorithm sorts only the **first portion** of a sequence:

- It sorts the elements in the range `[rnd_begin, rnd_middle)` as if the whole range `[rnd_begin, rnd_end)` were fully sorted.
- Elements in the first group `[rnd_begin, rnd_middle)` are guaranteed to be sorted and less than or equal to elements in `[rnd_middle, rnd_end)`.
- Elements in `[rnd_middle, rnd_end)` remain unsorted.

---

### 📌 **Function Signatures**

```cpp
// Partial sorting in-place
void partial_sort([ep], rnd_begin, rnd_middle, rnd_end, [comp]);

// Partial sorting into a separate destination sequence
RandomAccessIterator partial_sort_copy(
    [ep],
    ipt_begin, ipt_end,
    rnd_begin, rnd_end,
    [comp]
);
```

- **`ep` (optional)**: Execution policy (`std::execution::seq` by default).
- **Iterators**:
  - **Modifying**: `[rnd_begin, rnd_middle, rnd_end)` for the target range.
  - **Copying**: `[ipt_begin, ipt_end)` source range and `[rnd_begin, rnd_end)` destination range.
- **`comp` (optional)**: Custom comparison operator (defaults to `<`).

---

### ⏳ **Complexity**

- Quasilinear: **O(N log K)**  
  where **N** = `distance(rnd_begin, rnd_end)` and **K** = `distance(rnd_begin, rnd_middle)`

---

### 🔑 **Requirements**

Elements must be:

- **Swappable**
- **Move-constructible**
- **Move-assignable**

---

### 🧪 **Examples**

### ✅ **`partial_sort` In-Place Example:**

```cpp
#include <algorithm>
#include <string>
#include <iostream>

int main() {
    std::string word{"nectarous"};

    std::partial_sort(word.begin(), word.begin() + 4, word.end());
    std::cout << word << '\n'; // "acentrous"
    
    return 0;
}
```

**Explanation:**  
First four letters ("acen") are sorted correctly, smaller than any remaining letters.

### ✅ **`partial_sort` with Custom Comparison Example:**

```cpp
#include <algorithm>
#include <string>
#include <iostream>

enum class CharCategory { Ascender, Normal, Descender };

CharCategory categorize(char c) {
    switch(c) {
        case 'g': case 'j': case 'p': case 'q': case 'y':
            return CharCategory::Descender;
        case 'b': case 'd': case 'f': case 'h': case 'k':
        case 'l': case 't':
            return CharCategory::Ascender;
        default:
            return CharCategory::Normal;
    }
}

bool ascension_compare(char x, char y) {
    return categorize(x) < categorize(y);
}

int main() {
    std::string word{"pretanning"};

    std::partial_sort(word.begin(), word.begin() + 3, word.end(), ascension_compare);
    std::cout << word << '\n'; // "trepanning"

    return 0;
}
```

**Explanation:**  
The first three characters ("tre") are sorted according to typography categories (ascender first).

---

### ⚠️ **Important Note**

- `partial_sort` is **not stable**; the relative ordering of equivalent elements isn't guaranteed.

---

Would you like more clarification or additional examples?