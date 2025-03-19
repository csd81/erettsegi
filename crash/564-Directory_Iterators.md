### ✅ TL;DR: Directory Iterators  

- **`std::filesystem::directory_iterator`**  
  - Iterates over the immediate contents of a directory (no recursion).  
  - Great for listing files/folders in a single directory.  

- **`std::filesystem::recursive_directory_iterator`**  
  - Does the same but **recursively** explores subdirectories.  
  - Drop-in replacement for `directory_iterator` if you need to go deep.  

- **Usage**:  
```cpp
for (const auto& entry : std::filesystem::directory_iterator("path/to/dir")) {
    std::cout << entry.path() << '\n';
}
```
- Replace `directory_iterator` with `recursive_directory_iterator` to list all files in all subfolders too.

---

👉 Want me to show how to filter certain file types while iterating?