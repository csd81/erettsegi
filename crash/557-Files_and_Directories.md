### ✅ TL;DR: Files and Directories in `<filesystem>`  

- **`std::filesystem::path`**:  
  - Just describes filesystem components (paths, filenames, etc.).  
  - Does **not** actually perform actions on files or directories.  

- **The `<filesystem>` header**:  
  - Contains non-member functions that **interact with the filesystem** (create, delete, copy, move, check existence, etc.).  
  - Provides friendly error handling and works cross-platform.  

- **Summary**:  
  - **`path`** = *"What you point to"*  
  - **`<filesystem>` functions** = *"What you do with it"*  

---

👉 Want me to list the most common filesystem functions like `exists()`, `create_directory()`, `remove()`, etc., in a quick table?