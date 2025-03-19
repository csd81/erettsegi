### ✅ TL;DR: **Summary of `std::filesystem::path` Methods**  

---

### ✅ **Construction & Assignment**  
| Operation                        | Description                                                |
|----------------------------------|------------------------------------------------------------|
| `path{}`                         | Constructs an empty path                                   |
| `path{s}`                        | Constructs from a string                                   |
| `path{p}` / `p1 = p2`            | Copy construction/assignment                               |
| `path{move(p)}` / `p1 = move(p2)`| Move construction/assignment                               |
| `p.assign(s)`                    | Assigns new content from string `s`                        |

---

### ✅ **Modification**  
| Operation                         | Description                                                     |
|-----------------------------------|-----------------------------------------------------------------|
| `p.append(s)` or `p / s`          | Appends `s` with appropriate separator                           |
| `p.concat(s)` or `p + s`          | Appends `s` without adding separator                              |
| `p.clear()`                       | Erases the path                                                 |
| `p.make_preferred()`              | Converts separators to system-preferred ones                     |
| `p.remove_filename()`             | Removes filename portion                                         |
| `p.replace_filename(p2)`          | Replaces filename with that of `p2`                              |
| `p.replace_extension(p2)`         | Replaces extension with that of `p2`                             |

---

### ✅ **Decomposition**  
| Method               | Returns                                                     |
|----------------------|-------------------------------------------------------------|
| `p.root_name()`      | Root name (e.g., `C:` on Windows)                           |
| `p.root_directory()` | Root directory (e.g., `/` or `\`)                           |
| `p.root_path()`      | Combined root name and directory                            |
| `p.relative_path()`  | Portion after root                                          |
| `p.parent_path()`    | Path without filename                                       |
| `p.filename()`       | Filename part                                               |
| `p.stem()`           | Filename without extension                                  |
| `p.extension()`      | Extension part                                              |

---

### ✅ **Existence Checks**  
| Method                      | Description                                        |
|-----------------------------|----------------------------------------------------|
| `p.empty()`                 | True if path is empty                             |
| `p.has_root_name()`         | True if root name exists                          |
| `p.has_root_directory()`    | True if root directory exists                     |
| `p.has_root_path()`         | True if root path exists                          |
| `p.has_relative_path()`     | True if relative path exists                      |
| `p.has_parent_path()`       | True if parent path exists                        |
| `p.has_filename()`          | True if filename exists                           |
| `p.has_stem()`              | True if stem exists                               |
| `p.has_extension()`         | True if extension exists                          |

---

### ✅ **String Access & Iteration**  
| Method                    | Description                                                      |
|---------------------------|------------------------------------------------------------------|
| `p.c_str()` / `p.native()`| Returns native string representation                              |
| `p.begin()` / `p.end()`   | Iteration support over path elements                              |

---

### ✅ **Comparison & Swap**  
| Operation                  | Description                                      |
|----------------------------|--------------------------------------------------|
| `p1.swap(p2)` / `swap(p1, p2)` | Exchanges contents of two paths                |
| `==, !=, >, >=, <, <=`     | Lexicographic comparisons between two paths      |

---

### ✅ **Stream I/O**  
| Operation     | Description                            |
|---------------|----------------------------------------|
| `s << p`      | Writes path to stream                  |
| `s >> p`      | Reads path from stream                 |

---

👉 Want me to make a printable reference sheet PDF for this?