Here's a concise summary of the **`sort`** algorithm from the C++ Standard Library:

---

## 🔗 **`sort`** (`<algorithm>` header)

The `sort` algorithm **reorders elements** of a sequence **in-place**. It is **unstable**, meaning it **doesn't guarantee** the preservation of the original ordering for elements considered equal.

---

### 📌 **Function Signature**

```cpp
void sort([ep], rnd_begin, rnd_end, [comp]);
```

- **`ep` (optional)**: Execution policy (`std::execution::seq` by default).
- **`rnd_begin, rnd_end`**: Random-access iterators specifying the range.
- **`comp` (optional)**: Custom comparison operator (default is `<`).

---

### ⏳ **Complexity**

- **O(N log N)**, where N = `distance(rnd_begin, rnd_end)`.

---

### 🔑 **Requirements**

Elements must be:

- **Swappable**
- **Move-constructible**
- **Move-assignable**

---

### 🧪 **Example**

Sorting a string alphabetically:

```cpp
#include <algorithm>
#include <string>
#include <iostream>

int main() {
    std::string goat_grass{"spoilage"};

    std::sort(goat_grass.begin(), goat_grass.end());

    std::cout << goat_grass << '\n'; // Outputs: "aegilops"

    return 0;
}
```

**Explanation:**  
- `std::sort` rearranges the characters of `"spoilage"` alphabetically.
- Result: `"aegilops"`.

---

### ⚠️ **Note on Stability**

- **Unstable sorting**: Equal elements may not retain original relative ordering.  
  *(Use `stable_sort` if stability is required.)*

---

Would you like additional examples or further clarifications?