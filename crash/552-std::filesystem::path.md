**TL;DR: `std::filesystem::path`**  

- **What it is:**  
  A C++ class from `<filesystem>` that models file and directory paths.  

- **Common ways to create:**  
  - `std::filesystem::path p;` → empty path  
  - `std::filesystem::path p("some/file.txt");` → from a string  

- **What you can do with it:**  
  - Break a path into parts (filename, extension, parent path, etc.)  
  - Modify paths (append directories, replace filenames)  
  - Write OS-independent file path code  

- **Why it’s useful:**  
  - Filesystem structures differ across OSes  
  - `std::filesystem::path` helps write clean, portable code for file manipulation  

---

👉 Want me to show common examples like decomposition, concatenation, and iteration over paths?