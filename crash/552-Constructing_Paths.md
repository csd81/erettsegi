### ✅ TL;DR: Constructing `std::filesystem::path`  

- **How to construct paths:**  
  - **Empty path:**  
    ```cpp
    std::filesystem::path empty_path;
    ```
  - **From string:**  
    ```cpp
    std::filesystem::path shadow_path{ "/etc/shadow" };
    ```

- **Checking if a path is empty:**  
  ```cpp
  empty_path.empty();  // returns true if empty
  ```

- **Comparing paths:**  
  You can compare paths with other paths or strings using `==`:  
  ```cpp
  shadow_path == std::string{ "/etc/shadow" }; // true
  ```

---

### ✅ Example from Listing 17-1:
```cpp
#include <string>
#include <filesystem>
TEST_CASE("std::filesystem::path supports == and .empty()") {
    std::filesystem::path empty_path;                          // u
    std::filesystem::path shadow_path{ "/etc/shadow" };        // v
    REQUIRE(empty_path.empty());                               // w
    REQUIRE(shadow_path == std::string{ "/etc/shadow" });      // x
}
```

---

👉 Want me to show common methods like `.filename()`, `.extension()`, `.parent_path()` next?