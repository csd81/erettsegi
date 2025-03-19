### ✅ TL;DR: `std::filesystem::directory_entry`  

- **What it is:**  
  The objects returned by `directory_iterator` or `recursive_directory_iterator`.  
  Each `directory_entry` represents a single item (file or directory) and provides methods to inspect its properties.

---

### ✅ Key `directory_entry` methods:

| Method                        | Description                                                            |
|--------------------------------|------------------------------------------------------------------------|
| `de.path()`                   | Get the full path of the entry                                         |
| `de.exists()`                 | Check if the entry still exists                                        |
| `de.is_directory()`           | True if it’s a directory                                               |
| `de.is_regular_file()`        | True if it’s a regular file                                            |
| `de.is_symlink()`             | True if it’s a symlink                                                 |
| `de.is_block_file()`          | True if it’s a block device (Linux)                                    |
| `de.is_character_file()`      | True if it’s a character device                                        |
| `de.is_fifo()`                | True if it’s a FIFO (pipe)                                             |
| `de.is_socket()`              | True if it’s a socket                                                  |
| `de.is_other()`               | True if it’s something else special                                     |
| `de.file_size()`              | Get file size in bytes (only for regular files)                        |
| `de.hard_link_count()`        | Get the number of hard links                                           |
| `de.last_write_time([t])`     | Get or set the last modification time                                  |
| `de.status()` / `de.symlink_status()` | Get status information (file type, permissions, etc.)               |

---

### ✅ Example (from Listing 17-7): Directory listing tool

```cpp
#include <iostream>
#include <filesystem>
#include <iomanip>
using namespace std;
using namespace std::filesystem;
using namespace std::chrono;

void describe(const directory_entry& entry) {
    try {
        if (entry.is_directory()) {
            cout << " *";
        } else {
            cout << setw(12) << entry.file_size();
        }

        auto lw_time = duration_cast<seconds>(entry.last_write_time().time_since_epoch());
        cout << setw(12) << lw_time.count()
             << " " << entry.path().filename().string()
             << "\n";
    } catch (const exception& e) {
        cout << "Error accessing " << entry.path() << ": " << e.what() << endl;
    }
}

int main(int argc, const char** argv) {
    if (argc != 2) {
        cerr << "Usage: listdir PATH";
        return -1;
    }

    const path sys_path{ argv[1] };
    cout << "Size          Last Write   Name\n";
    cout << "------------  ------------ ------------\n";
    for (const auto& entry : directory_iterator{ sys_path })
        describe(entry);
}
```

---

### ✅ Example Output:
```
Size          Last Write   Name
------------  ------------ ------------
 *            13177963504 addins
 *            13171360979 appcompat
316640        13167963236 WMSysPr9.prx
11264         13167963259 write.exe
```

---

👉 Want me to help extend this into a `recursive_directory_iterator` version to show all subdirectories too?