Here's a concise summary of the **`nth_element` algorithm** from the C++ Standard Library:

---

## 🚩 **nth_element (`<algorithm>` header)**

The `nth_element` algorithm partially sorts a sequence so that:

- The element at position `rnd_nth` is placed exactly where it would appear if the entire sequence was sorted.
- All elements **before** `rnd_nth` are **less than or equal** to the element at `rnd_nth`.
- All elements **after** `rnd_nth` are **greater than or equal**.

However, neither the elements before nor after `rnd_nth` are guaranteed to be sorted.

---

### 📌 **Function Signature**

```cpp
void nth_element([ep], rnd_begin, rnd_nth, rnd_end, [comp]);
```

- **`ep` (optional)**: Execution policy (`std::execution::seq` by default).
- **`rnd_begin, rnd_nth, rnd_end`**: Random-access iterators defining the range.
- **`comp` (optional)**: Custom comparison operator (defaults to `<`).

---

### ⏳ **Complexity**

- **Linear complexity (O(N))** on average, where N = `distance(rnd_begin, rnd_end)`.

---

### 🔑 **Requirements**

Elements must be:

- Swappable
- Move-constructible
- Move-assignable

---

### 🧪 **Example**

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main() {
    std::vector<int> numbers{1, 9, 2, 8, 3, 7, 4, 6, 5};

    // Move the element at position 5 (6th element) to its sorted position
    std::nth_element(numbers.begin(), numbers.begin() + 5, numbers.end());

    // Verify elements before the nth (6th) element are smaller or equal
    auto less_than_nth = [&numbers](int x) {
        return x < numbers[5];
    };

    bool correct_partition = std::all_of(numbers.begin(), numbers.begin() + 5, less_than_nth);

    std::cout << "Correct partition: " << std::boolalpha << correct_partition << '\n';
    std::cout << "nth_element at index 5: " << numbers[5] << '\n';

    // Possible output:
    // Correct partition: true
    // nth_element at index 5: 6

    return 0;
}
```

This code rearranges the vector such that the 6th smallest element (`6`) is in the correct sorted position, with smaller elements to its left.

---

Would you like more details or additional examples?