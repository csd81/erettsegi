### ✅ TL;DR: Inspecting Files and Directories with `<filesystem>`  

You can check detailed information about files, directories, and the filesystem using these functions:  

---

| **Function**                        | **What It Does**                                                                                      |
|-------------------------------------|-------------------------------------------------------------------------------------------------------|
| `current_path([p], [ec])`           | Gets or sets the current working directory.                                                           |
| `exists(p, [ec])`                   | Checks if a file or directory exists at path `p`.                                                     |
| `equivalent(p1, p2, [ec])`          | Checks if `p1` and `p2` point to the same file or directory (like hard links to the same inode).     |
| `file_size(p, [ec])`                | Returns the size of a regular file in bytes.                                                          |
| `hard_link_count(p, [ec])`          | Returns how many hard links point to the file.                                                        |
| `last_write_time(p, [t], [ec])`     | Gets or sets the last modified time (using `std::chrono::time_point`).                                |
| `permissions(p, prm, [ec])`         | Sets the permissions on `p`. Permissions are specified using `std::filesystem::perms`.                |
| `read_symlink(p, [ec])`             | Returns the target path that a symlink points to.                                                     |
| `space(p, [ec])`                    | Returns filesystem space info: `capacity`, `free`, and `available`.                                   |
| `status(p, [ec])`                   | Returns a `file_status` object describing the type and permissions of `p` (follows symlinks).         |
| `symlink_status(p, [ec])`           | Like `status()`, but doesn’t follow symlinks (inspects the link itself).                              |

---

### ✅ Example: Checking existence and file size  
```cpp
#include <iostream>
#include <filesystem>
using namespace std;
namespace fs = std::filesystem;

int main() {
    fs::path p = "example.txt";
    if (fs::exists(p)) {
        cout << "File exists.\n";
        if (fs::is_regular_file(p)) {
            cout << "Size: " << fs::file_size(p) << " bytes\n";
        }
    } else {
        cout << "File does not exist.\n";
    }
}
```

---

### ✅ Fun fact:
- `space_info` structure returned by `space(p)` contains:
  - `capacity`: total space on that filesystem.
  - `free`: free space (even if reserved for root/admin).
  - `available`: free space accessible to non-privileged users.

---

👉 Want me to show how to build a simple `ls`-like program using these inspection tools?

Awesome! Here’s a simple **`ls`-like program** using `<filesystem>` that lists files and directories along with their types and sizes:  

---

### ✅ Minimal `ls`-like Program Example:

```cpp
#include <iostream>
#include <filesystem>
#include <iomanip>
namespace fs = std::filesystem;

void list_directory(const fs::path& dir) {
    try {
        for (const auto& entry : fs::directory_iterator(dir)) {
            const auto& p = entry.path();
            std::cout << std::left << std::setw(30) << p.filename().string();

            if (fs::is_directory(p)) {
                std::cout << " <DIR>";
            } else if (fs::is_symlink(p)) {
                std::cout << " <SYMLINK>";
            } else if (fs::is_regular_file(p)) {
                std::cout << " " << fs::file_size(p) << " bytes";
            } else {
                std::cout << " <OTHER>";
            }
            std::cout << "\n";
        }
    } catch (const std::exception& e) {
        std::cerr << "Error reading directory: " << e.what() << std::endl;
    }
}

int main() {
    fs::path current = fs::current_path();
    std::cout << "Listing contents of: " << current << "\n\n";
    list_directory(current);
}
```

---

### ✅ Example Output:
```
Listing contents of: "/home/user/projects"

file1.txt                    1024 bytes
my_folder                    <DIR>
link_to_something            <SYMLINK>
image.png                    20345 bytes
unknown                      <OTHER>
```

---

👉 Want me to enhance this with recursion (`ls -R` style) or add permission and timestamp info (`ls -l` style)?