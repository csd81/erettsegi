Here's a concise summary of the **`stable_sort`** algorithm from the C++ Standard Library:

---

## 🔗 **`stable_sort` (`<algorithm>` header)**

The `stable_sort` algorithm sorts a sequence **stably**, meaning that equal elements retain their original relative ordering after sorting.

---

### 📌 **Function Signature**

```cpp
void stable_sort([ep], rnd_begin, rnd_end, [comp]);
```

- **`ep` (optional)**: Execution policy (`std::execution::seq` by default).
- **`rnd_begin, rnd_end`**: Random-access iterators representing the range to sort.
- **`comp` (optional)**: Custom comparison operator (defaults to `<`).

---

### ⏳ **Complexity**

- Typically **O(N log² N)**.
- Improves to **O(N log N)** if extra memory is available.

---

### 🔑 **Requirements**

Elements must be:

- **Swappable**
- **Move-constructible**
- **Move-assignable**

---

### 🚩 **Example: Stable Sort Using Typography (Ascenders/Descenders)**

This example sorts a word so that letters with **ascenders** come first, then normal letters, and finally letters with **descenders**—all while maintaining their original relative order within groups.

```cpp
#include <algorithm>
#include <string>
#include <iostream>

enum class CharCategory {
    Ascender,
    Normal,
    Descender
};

CharCategory categorize(char x) {
    switch (x) {
        case 'g': case 'j': case 'p': case 'q': case 'y':
            return CharCategory::Descender;
        case 'b': case 'd': case 'f': case 'h':
        case 'k': case 'l': case 't':
            return CharCategory::Ascender;
        default:
            return CharCategory::Normal;
    }
}

bool ascension_compare(char x, char y) {
    return categorize(x) < categorize(y);
}

int main() {
    std::string word{"outgrin"};

    std::stable_sort(word.begin(), word.end(), ascension_compare);

    std::cout << word << '\n'; // Outputs: "touring"
    return 0;
}
```

**Explanation:**  
- `t` (ascender) is moved first.
- Remaining normal characters (`o,u,r,i,n`) follow, preserving their original relative order.
- Finally, the descender `g` appears last.

---

### ⚠️ **Note on Stability**

The primary benefit of `stable_sort` is that elements considered equal by the sorting criteria **retain their original ordering**.

---

Would you like more details or additional examples on this algorithm?