### ✅ TL;DR: Recursive Directory Iteration  

- **`recursive_directory_iterator`** works like `directory_iterator`, but it goes through all subdirectories.  
- Useful for building directory tree summaries: total size, number of files, and number of directories.  

---

### ✅ Key steps in recursive directory iteration:
| Step                               | What happens                                                               |
|-----------------------------------|----------------------------------------------------------------------------|
| Use `recursive_directory_iterator` | Iterates through all files and subdirectories                              |
| Check `entry.is_directory()`       | If directory, increment directory count                                    |
| If regular file, add `entry.file_size()` | Add file size and increment file count                                      |
| Accumulate attributes for each directory and print them                   |

---

### ✅ Example (from Listing 17-8): `treedir` — Directory Size Summary Tool

```cpp
#include <iostream>
#include <filesystem>
#include <iomanip>
using namespace std;
using namespace std::filesystem;
struct Attributes {
    Attributes& operator+=(const Attributes& other) {
        size_bytes += other.size_bytes;
        n_directories += other.n_directories;
        n_files += other.n_files;
        return *this;
    }
    size_t size_bytes = 0;
    size_t n_directories = 0;
    size_t n_files = 0;
};

void print_line(const Attributes& attr, string_view path) {
    cout << setw(14) << attr.size_bytes
         << setw(7) << attr.n_files
         << setw(7) << attr.n_directories
         << " " << path << "\n";
}

Attributes explore(const directory_entry& directory) {
    Attributes attr{};
    for (const auto& entry : recursive_directory_iterator{ directory.path() }) {
        if (entry.is_directory()) {
            attr.n_directories++;
        } else {
            attr.n_files++;
            attr.size_bytes += entry.file_size();
        }
    }
    return attr;
}

int main(int argc, const char** argv) {
    if (argc != 2) {
        cerr << "Usage: treedir PATH";
        return -1;
    }

    const path sys_path{ argv[1] };
    cout << "Size          Files  Dirs   Name\n";
    cout << "-------------- ------ ------ ------------\n";

    Attributes total{};
    for (const auto& entry : directory_iterator{ sys_path }) {
        try {
            if (entry.is_directory()) {
                const auto attr = explore(entry);
                total += attr;
                print_line(attr, entry.path().string());
                total.n_directories++;
            } else {
                total.n_files++;
                error_code ec;
                total.size_bytes += entry.file_size(ec);
                if (ec) cerr << "Error reading size of: " << entry.path() << endl;
            }
        } catch (const exception&) {}
    }
    print_line(total, argv[1]);
}
```

---

### ✅ Example Output:
```
Size          Files  Dirs   Name
-------------- ------ ------ ------------
      802          1      0 C:\Windows\addins
   8267330          9      5 C:\Windows\apppatch
11396916465     73383  20480 C:\Windows\WinSxS
21038460348    110950  26513 C:\Windows
```

---

👉 Want me to show how to make it print results sorted by directory size?