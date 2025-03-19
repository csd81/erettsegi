### ✅ TL;DR: Inspecting File Types with `<filesystem>`  

You can check what kind of file a given path refers to using these inspection functions:  

| Function                       | What it checks for                                                        |
|--------------------------------|----------------------------------------------------------------------------|
| `is_block_file(p, [ec])`       | If `p` is a block device (special file; common in Linux)                   |
| `is_character_file(p, [ec])`   | If `p` is a character device (like `/dev/tty`)                             |
| `is_regular_file(p, [ec])`     | If `p` is a regular file                                                   |
| `is_symlink(p, [ec])`          | If `p` is a symbolic link                                                  |
| `is_empty(p, [ec])`            | If `p` is an empty file or an empty directory                              |
| `is_directory(p, [ec])`        | If `p` is a directory                                                      |
| `is_fifo(p, [ec])`             | If `p` is a named pipe (FIFO)                                              |
| `is_socket(p, [ec])`           | If `p` is a socket                                                         |
| `is_other(p, [ec])`            | If `p` is a file that’s none of the above                                  |

---

### ✅ Example (from Listing 17-5):

```cpp
#include <iostream>
#include <filesystem>
using namespace std;

void describe(const filesystem::path& p) {
    cout << boolalpha << "Path: " << p << endl;
    try {
        cout << "Is directory: " << filesystem::is_directory(p) << endl;
        cout << "Is regular file: " << filesystem::is_regular_file(p) << endl;
    } catch (const exception& e) {
        cerr << "Exception: " << e.what() << endl;
    }
}

int main() {
    filesystem::path win_path{ R"(C:/Windows/System32/kernel32.dll)" };
    describe(win_path);
    win_path.remove_filename();
    describe(win_path);

    filesystem::path nix_path{ R"(/bin/bash)" };
    describe(nix_path);
    nix_path.remove_filename();
    describe(nix_path);
}
```

---

### ✅ Key Point:
- Output differs by OS. For example, `/bin/bash` is a regular file on Linux, but not on Windows.
- Use these checks when writing cross-platform filesystem utilities.

---

👉 Want me to give a cheat sheet with real-world use examples for each file type check?

### ✅ Filesystem File Type Inspection — Cheat Sheet  

| Function                      | ✅ What It Checks For                                                   | 💡 Example Use Case                                                      |
|--------------------------------|-------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `is_block_file(p)`             | Block device file (like `/dev/sda`)                                      | Detect disk devices on Linux-based systems                               |
| `is_character_file(p)`        | Character device file (like `/dev/tty`)                                  | Detect terminal or input devices                                         |
| `is_regular_file(p)`          | Normal file (text, binaries, documents)                                  | Confirm you're about to read/write to a standard file                    |
| `is_symlink(p)`                | Symbolic link                                                           | Follow or display link targets                                           |
| `is_empty(p)`                  | Empty file or empty directory                                            | Clean-up tasks, ignore empty folders/files                               |
| `is_directory(p)`              | Directory                                                               | Check before listing contents or recursively processing                  |
| `is_fifo(p)`                   | Named pipe (FIFO)                                                       | Monitor or interact with IPC (inter-process communication) mechanisms    |
| `is_socket(p)`                 | Socket file                                                              | Useful for checking Unix socket endpoints                                |
| `is_other(p)`                  | Special file type (none of the above categories)                         | Handle edge cases for unusual filesystem objects                         |

---

### ✅ Example:
```cpp
if (std::filesystem::is_regular_file(p)) {
    std::cout << p << " is a regular file.\n";
} else if (std::filesystem::is_directory(p)) {
    std::cout << p << " is a directory.\n";
} else if (std::filesystem::is_symlink(p)) {
    std::cout << p << " is a symlink.\n";
} else {
    std::cout << p << " is another special type of file.\n";
}
```

---

👉 Want me to generate a quick PDF or markdown reference card for all of these?