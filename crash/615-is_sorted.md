Here's a concise summary of the **`is_sorted`** and **`is_sorted_until`** algorithms from the C++ Standard Library:

---

## 🔎 **`is_sorted` and `is_sorted_until` (`<algorithm>` header)**

These algorithms check if a given sequence is sorted based on either the default operator `<` or a custom comparison operator (`comp`).

- **`is_sorted`** returns a boolean indicating whether the entire sequence is sorted.
- **`is_sorted_until`** returns an iterator pointing to the **first element that breaks the sorted order**. If the entire sequence is sorted, it returns the end iterator.

---

### 📌 **Function Signatures**

```cpp
bool is_sorted([ep], rnd_begin, rnd_end, [comp]);

ForwardIterator is_sorted_until([ep], rnd_begin, rnd_end, [comp]);
```

- **`ep` (optional)**: Execution policy (`std::execution::seq` by default).
- **`rnd_begin, rnd_end`**: Random-access iterators defining the sequence.
- **`comp` (optional)**: Custom comparison operator.

---

### ⏳ **Complexity**

- **Linear Complexity** (**O(N)**), where N = `distance(rnd_begin, rnd_end)`.

---

### ✅ **Example Usage**

```cpp
#include <algorithm>
#include <iostream>
#include <string>

int main() {
    std::string word1{"billowy"};
    bool sorted1 = std::is_sorted(word1.begin(), word1.end());
    std::cout << "Is 'billowy' sorted? " << std::boolalpha << sorted1 << '\n';
    // Output: true (billowy is sorted alphabetically)

    std::string word2{"floppy"};
    auto sorted_until = std::is_sorted_until(word2.begin(), word2.end());

    if (sorted_until == word2.end()) {
        std::cout << "'floppy' is fully sorted\n";
    } else {
        std::cout << "'floppy' is sorted until character: " << *sorted_until << '\n';
    }
    // Output: 'floppy' is fully sorted

    return 0;
}
```

---

### 📝 **Key Points**

- Use `is_sorted` when you simply want to check if the whole sequence is sorted.
- Use `is_sorted_until` to detect precisely **where** the sorted property breaks.

---

Would you like additional examples or further explanations on this topic?