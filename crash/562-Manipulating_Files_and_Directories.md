### ✅ TL;DR: Manipulating Files and Directories with `<filesystem>`  

The filesystem library lets you perform actual file and directory operations, not just inspection.  

---

### ✅ Common Manipulation Functions:

| Function                                  | What It Does                                                                          |
|-------------------------------------------|---------------------------------------------------------------------------------------|
| `copy(p1, p2, [opt], [ec])`              | Copies files/directories; `opt` can skip, overwrite, or update existing targets       |
| `copy_file(p1, p2, [opt], [ec])`         | Copies a file only (errors if not a regular file)                                     |
| `create_directory(p, [ec])`              | Creates a single directory                                                            |
| `create_directories(p, [ec])`            | Recursively creates directories if parents are missing                                |
| `create_hard_link(tgt, lnk, [ec])`       | Creates a hard link                                                                  |
| `create_symlink(tgt, lnk, [ec])`         | Creates a symlink to `tgt`                                                            |
| `create_directory_symlink(tgt, lnk, [ec])` | Creates a directory symlink                                                          |
| `remove(p, [ec])`                        | Deletes a file or empty directory                                                    |
| `remove_all(p, [ec])`                    | Deletes a file or directory and everything inside recursively                        |
| `rename(p1, p2, [ec])`                   | Renames or moves a file/directory                                                    |
| `resize_file(p, new_size, [ec])`         | Changes file size (truncate or extend with zeros)                                    |

---

### ✅ Example (from Listing 17-6):  
This program:  
- Inspects an existing file  
- Copies it  
- Resizes it  
- Deletes it  

```cpp
#include <iostream>
#include <filesystem>
using namespace std;
using namespace std::filesystem;
using namespace std::chrono;

void write_info(const path& p) {
    if (!exists(p)) {
        cout << p << " does not exist." << endl;
        return;
    }
    const auto last_write = last_write_time(p).time_since_epoch();
    const auto in_hours = duration_cast<hours>(last_write).count();
    cout << p << "\t" << in_hours << "\t" << file_size(p) << " bytes\n";
}

int main() {
    const path source_file{ R"(C:/Windows/System32/kernel32.dll)" };
    const auto target_file = temp_directory_path() / "REAMDE";

    try {
        write_info(source_file);
        write_info(target_file);

        cout << "Copying " << source_file.filename() << " to " << target_file.filename() << "\n";
        copy_file(source_file, target_file);
        write_info(target_file);

        cout << "Resizing " << target_file.filename() << " to 1024 bytes\n";
        resize_file(target_file, 1024);
        write_info(target_file);

        cout << "Removing " << target_file.filename() << "\n";
        remove(target_file);
        write_info(target_file);

    } catch (const exception& e) {
        cerr << "Exception: " << e.what() << endl;
    }
}
```

---

### ✅ Key steps shown:
- **Copy** a file from one location to another  
- **Resize** a file (truncate or pad)  
- **Remove** a file and verify existence  

---

👉 Want me to show an example of using `create_directories()`, `remove_all()`, and directory cleanup in a small script?

Here’s a clean, practical example that shows how to:  
- Create nested directories  
- Add dummy files  
- Remove everything with `remove_all()`  

---

### ✅ Example: Creating and Cleaning Up Directories  
```cpp
#include <iostream>
#include <filesystem>
#include <fstream>
using namespace std;
namespace fs = std::filesystem;

int main() {
    // Create a nested directory path
    fs::path nested_dir = fs::temp_directory_path() / "test_dir" / "subdir1" / "subdir2";
    cout << "Creating directories: " << nested_dir << endl;
    fs::create_directories(nested_dir);

    // Create a dummy file inside the deepest directory
    fs::path dummy_file = nested_dir / "example.txt";
    cout << "Creating file: " << dummy_file << endl;
    ofstream(dummy_file) << "Hello from dummy file!";

    // Verify existence
    if (fs::exists(dummy_file)) {
        cout << "File created successfully at: " << dummy_file << endl;
    }

    // Remove all
    fs::path top_dir = fs::temp_directory_path() / "test_dir";
    cout << "Removing everything under: " << top_dir << endl;
    fs::remove_all(top_dir);

    // Confirm removal
    if (!fs::exists(top_dir)) {
        cout << "Cleanup successful. Directory no longer exists.\n";
    } else {
        cout << "Cleanup failed.\n";
    }
}
```

---

### ✅ Output Example:
```
Creating directories: "/tmp/test_dir/subdir1/subdir2"
Creating file: "/tmp/test_dir/subdir1/subdir2/example.txt"
File created successfully at: "/tmp/test_dir/subdir1/subdir2/example.txt"
Removing everything under: "/tmp/test_dir"
Cleanup successful. Directory no longer exists.
```

---

👉 Want me to show how to wrap this into a reusable cleanup utility function?

Here’s how you can wrap that logic into a **reusable cleanup utility function**:  

---

### ✅ Reusable Directory Cleanup Utility  

```cpp
#include <iostream>
#include <filesystem>
#include <fstream>
namespace fs = std::filesystem;

void create_test_structure(const fs::path& base) {
    fs::create_directories(base / "subdir1" / "subdir2");
    std::ofstream(base / "subdir1" / "subdir2" / "example.txt") << "Test content.";
    std::cout << "Test structure created at: " << base << "\n";
}

void cleanup_path(const fs::path& target) {
    if (fs::exists(target)) {
        std::cout << "Cleaning up: " << target << "\n";
        fs::remove_all(target);
        std::cout << "Removed: " << target << "\n";
    } else {
        std::cout << "Path does not exist, nothing to clean: " << target << "\n";
    }
}

int main() {
    fs::path test_dir = fs::temp_directory_path() / "cleanup_demo";
    
    create_test_structure(test_dir);
    // Do something with test_dir here if needed...

    // Call cleanup utility
    cleanup_path(test_dir);
}
```

---

### ✅ Benefits:
- **`create_test_structure()`**: Sets up a nested test environment for experimentation.  
- **`cleanup_path()`**: Handles safe cleanup and checks for existence before deleting.  
- Can be reused anywhere by passing any path to `cleanup_path()`.

---

👉 Want me to turn this into a small CLI tool (take path from command line and clean it up)?