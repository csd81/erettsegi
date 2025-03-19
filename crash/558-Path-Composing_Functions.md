### ✅ TL;DR: Path-Composing Functions  

In addition to `std::filesystem::path` constructors, there are special functions to build and manipulate paths:  

| Function                                | Description                                                                          |
|-----------------------------------------|--------------------------------------------------------------------------------------|
| `absolute(p, [ec])`                    | Returns an absolute version of path `p`                                              |
| `canonical(p, [ec])`                   | Returns a fully resolved, canonical version of `p` (no symlinks, dots, or dot-dot)   |
| `current_path([ec])`                   | Gets the current working directory                                                   |
| `current_path(p, [ec])`                | Changes the current working directory to `p`                                         |
| `relative(p, [base], [ec])`            | Returns `p` relative to `base` (or current dir if base not given)                    |
| `temp_directory_path([ec])`            | Returns the system’s temporary files directory (always exists)                       |

---

### ✅ Example (from Listing 17-4):  

```cpp
#include <filesystem>
#include <iostream>
using namespace std;

int main() {
    try {
        const auto temp_path = filesystem::temp_directory_path();      // u
        const auto relative = filesystem::relative(temp_path);         // v
        cout << boolalpha
             << "Temporary directory path: " << temp_path              // w
             << "\nTemporary directory absolute: " << temp_path.is_absolute() // x
             << "\nCurrent path: " << filesystem::current_path()       // y
             << "\nTemporary directory's relative path: " << relative  // z
             << "\nRelative path absolute: " << relative.is_absolute() // {
             << "\nChanging current directory to temp.";
        filesystem::current_path(temp_path);                           // |
        cout << "\nCurrent directory: " << filesystem::current_path(); // }
    } catch(const exception& e) {
        cerr << "Error: " << e.what();                                 // ~
    }
}
```

---

### ✅ Key takeaways:  
- `absolute()`, `canonical()`, and `relative()` help transform paths.  
- `current_path()` can both get and change the current directory.  
- `temp_directory_path()` gives you a reliable place to store temporary files.  
- Works across platforms (unless certain environments don’t support it).  

---

👉 Want me to show what canonical paths look like with an example using `.` and `..`?

Here’s an example showing how `std::filesystem::canonical()` works by resolving `.` and `..` in paths:  

---

### ✅ Example: Using `canonical()` to resolve paths

```cpp
#include <iostream>
#include <filesystem>
using namespace std;
namespace fs = std::filesystem;

int main() {
    try {
        fs::path p = fs::current_path() / ".." / "." / "some_folder" / "..";
        cout << "Original path: " << p << endl;

        fs::path canonical_path = fs::canonical(p);
        cout << "Canonical path: " << canonical_path << endl;
    } catch (const fs::filesystem_error& e) {
        cerr << "Filesystem error: " << e.what() << endl;
    }
}
```

---

### ✅ Example output:
```
Original path: "/home/user/project/.././some_folder/.."
Canonical path: "/home/user"
```

---

### ✅ Key behavior of `canonical()`:
- Resolves `.` (current directory) and `..` (parent directory)  
- Follows symlinks and returns the *real* path  
- The given path **must exist**, or it will throw a `filesystem_error`  

---

👉 Want me to show `weakly_canonical()` too? It works similarly but doesn't require all path components to exist!