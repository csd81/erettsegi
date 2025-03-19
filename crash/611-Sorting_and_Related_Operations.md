Here's a concise TL;DR of **Sorting and Related Operations** in C++'s Standard Library:

---

## 📝 **Sorting Algorithms Overview (`<algorithm>` header)**

Sorting algorithms reorder elements of a container based on a **comparison operator** (`operator<` by default). A valid comparison operator `comp(a,b)` returns `true` if `a` comes before `b`.

- **Note**: Comparison operators must be **transitive** (`if comp(a,b) and comp(b,c)` → `comp(a,c)`).

---

## 🔑 **Primary Sorting Algorithms**

| Algorithm          | Description                                                 | Complexity                 | Stable? |
|--------------------|-------------------------------------------------------------|----------------------------|---------|
| **`sort`**         | Sorts a sequence **in-place** (unstable)                    | **O(N log N)**             | ❌       |
| **`stable_sort`**  | Sorts a sequence **in-place** (stable)                      | **O(N log² N)** *(Can become O(N log N) with extra memory)* | ✅       |
| **`partial_sort`** | Sorts only the first **K** elements of a sequence           | **O(N log K)**             | ❌       |
| **`nth_element`**  | Places the nth element as if the sequence were sorted       | **O(N)**                   | ❌       |

---

## ⚡ **Sorting-Related Utilities**

| Algorithm             | Description                                              | Complexity   |
|-----------------------|----------------------------------------------------------|--------------|
| **`is_sorted`**       | Checks if a sequence is sorted                           | **O(N)**     |
| **`is_sorted_until`** | Returns iterator to the first unsorted element           | **O(N)**     |

---

## 🚩 **Examples**

### ✅ **`sort` Example:**

```cpp
#include <algorithm>
#include <string>

std::string goat_grass{ "spoilage" };
std::sort(goat_grass.begin(), goat_grass.end());
// goat_grass is now "aegilops"
```

### ✅ **`stable_sort` Example (custom order):**

Sort letters by ascenders and descenders (typography):

```cpp
#include <algorithm>
#include <string>

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

auto ascension_compare = [](char a, char b) {
    return categorize(a) < categorize(b);
};

std::string word{ "outgrin" };
std::stable_sort(word.begin(), word.end(), ascension_compare);
// word is now "touring"
```

### ✅ **`partial_sort` Example:**

```cpp
#include <algorithm>
#include <string>

std::string word{ "nectarous" };
std::partial_sort(word.begin(), word.begin() + 4, word.end());
// word is now "acentrous"
```

### ✅ **`nth_element` Example:**

```cpp
#include <algorithm>
#include <vector>

std::vector<int> numbers{1, 9, 2, 8, 3, 7, 4, 6, 5};
std::nth_element(numbers.begin(), numbers.begin() + 5, numbers.end());

// Now numbers[5] == 6,
// and elements [0,4] are all less than numbers[5]
```

---

## 🚧 **Important Notes**

- Sorting requires **random-access iterators**.
- Sorted elements must be **swappable, move-constructible, and move-assignable**.
- Stability guarantees the original relative order of equal elements.

---

Would you like more detail or another example on any specific algorithm?