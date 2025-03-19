### ✅ TL;DR: Constructing `std::filesystem::directory_iterator`  

- **End iterator**:  
  - `directory_iterator{}` → Creates an end iterator (used to detect end of iteration).  

- **Typical construction**:  
  - `directory_iterator{ p }` — Start iterating over directory `p`.  
  - Optional flags (`directory_options`) can control behavior:  
    | Option                          | Meaning                                                          |
    |---------------------------------|------------------------------------------------------------------|
    | `none`                          | (default) Do not follow symlinks; throws on permission denied     |
    | `follow_directory_symlink`      | Follows directory symlinks                                       |
    | `skip_permission_denied`        | Skips directories you don't have permission to access            |

- **Error handling**:  
  - You can pass a `std::error_code` argument to handle errors without exceptions:  
    ```cpp
    std::error_code ec;
    std::filesystem::directory_iterator it{"some/dir", ec};
    if (ec) { std::cerr << "Error: " << ec.message(); }
    ```

- **Supports copy & move construction/assignment**.  

---

👉 Want me to show a quick example of using `directory_iterator` with `skip_permission_denied` to safely iterate directories?