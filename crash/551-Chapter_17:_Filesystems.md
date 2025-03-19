## Chapter 17: C++ Filesystems

### Introduction
This chapter teaches you how to use the C++ standard library's Filesystem library to perform operations on filesystems, including manipulating and inspecting files, enumerating directories, and interoperating with file streams. The Filesystem library provides a consistent, cross-platform interface to interact with hierarchical filesystems, making it an invaluable tool for system programming and application development.

### 1. Filesystem Concepts
At the heart of a filesystem are files and directories. A file is a data container that supports input and output, while directories are containers that organize files and other directories. Paths are strings representing the location of files or directories. They can be absolute (fully qualified) or relative (based on the current directory). The special elements `.` and `..` represent the current and parent directories, respectively. Hard links are alternate names for an existing file, and symbolic links (symlinks) point to other paths.

### 2. The `std::filesystem::path` Class
The `path` class is central to the Filesystem library, representing filesystem paths in an OS-independent way. You can construct paths using default constructors (for empty paths), from strings, or by copying and moving. Important methods include:
- `empty()`: Checks if the path is empty.
- `root_name()`, `root_directory()`, `root_path()`: Extract different root parts of a path.
- `relative_path()`, `parent_path()`, `filename()`, `stem()`, and `extension()`: Extract components of a path.
- `make_preferred()`: Converts separators to the system-preferred format.
- Modifiers like `replace_filename()`, `replace_extension()`, `remove_filename()`, and `clear()` allow dynamic path manipulation.

### 3. Path-Composing Functions
Instead of constructing paths manually, you can use helper functions:
- `absolute()`: Returns an absolute path.
- `canonical()`: Returns a fully resolved, symlink-free path.
- `relative()`: Makes a path relative to another.
- `temp_directory_path()`: Returns the system’s temporary directory.
- `current_path()`: Gets or sets the current working directory.

### 4. Error Handling
Filesystem operations can fail due to permission errors or missing files. Most functions have two forms: one that throws exceptions (`std::filesystem::filesystem_error`) and one that sets an `std::error_code` for error handling without exceptions.

### 5. Inspecting Files and Directories
The library provides numerous functions to inspect filesystem attributes:
- `exists()`, `is_regular_file()`, `is_directory()`, `is_symlink()`, and more check file types.
- `file_size()`: Returns the size of a file.
- `last_write_time()`: Retrieves or sets modification times.
- `permissions()`: Adjusts file permissions.
- `hard_link_count()`: Returns the number of hard links.
- `space()`: Provides available and used disk space information.

### 6. Manipulating Files and Directories
Filesystem functions allow creation, modification, and removal of files and directories:
- `copy()` and `copy_file()`: Copy files or directories with customizable options.
- `create_directory()` and `create_directories()`: Create single or nested directories.
- `create_symlink()` and `create_directory_symlink()`: Create symbolic links.
- `remove()` and `remove_all()`: Delete files or directories.
- `resize_file()`: Truncate or expand file size.
- `rename()`: Rename or move files and directories.

### 7. Directory Iterators
Two iterators help enumerate directories:
- `directory_iterator`: Iterates through a directory’s immediate contents.
- `recursive_directory_iterator`: Iterates through all subdirectories.
These iterators yield `std::filesystem::directory_entry` objects, which provide attributes like file type, size, and modification time.

### 8. Using `directory_entry`
Each `directory_entry` object allows:
- Access to the associated path with `path()`.
- Checking attributes with methods like `is_directory()`, `is_regular_file()`, `is_symlink()`, and `file_size()`.
- Retrieving status information with `status()` and `symlink_status()`.

### 9. Example: Directory Listing
A common application of directory iterators is building listing utilities. For instance, using `directory_iterator` to print file sizes, modification times, and names of entries in a given directory. You can also handle exceptions gracefully if permissions are denied.

### 10. Recursive Directory Iteration
`recursive_directory_iterator` can be used to compute total sizes and counts of files and directories. A typical pattern involves:
- Iterating over subdirectories.
- Accumulating total file sizes and counts.
- Printing summaries for each directory.
This pattern allows creating utilities similar to Unix’s `du` command.

### 11. Building a Recursive Summary Tool
By combining `recursive_directory_iterator` with attributes tracking, you can build a program that:
- Recursively scans each directory.
- Tracks total file sizes, file counts, and directory counts.
- Prints the results, sorted by size if desired.

### Conclusion
The Filesystem library provides a robust, platform-independent toolkit for working with files, directories, and paths. Its clean API and extensive functionality make it a key part of modern C++ programming. Whether you need to inspect files, iterate through directories, or manipulate filesystem elements, `std::filesystem` provides a safe, efficient, and flexible solution.

------

### **Chapter 17: C++ Filesystems**  

The **C++ Filesystem library** (`<filesystem>`) provides a standardized way to **interact with files and directories**, making it easier to write **cross-platform** code. This chapter covers how to **manipulate, inspect, and enumerate files and directories** using the standard library.  

---

## **1. Filesystem Basics**  

The core element of the **Filesystem library** is `std::filesystem::path`, which models file and directory paths. However, the library does not directly manipulate files using `path`; instead, the `<filesystem>` header provides functions to perform operations.  

- **`std::filesystem::path`**:
  - Represents file/directory paths in an OS-independent way.
  - Allows **string operations** like joining paths and extracting components.
  - Does **not** perform operations on actual files; functions in `<filesystem>` do.  

### **Constructing Paths**  

```cpp
#include <filesystem>
#include <iostream>
namespace fs = std::filesystem;

int main() {
    fs::path p1{"/home/user/documents"};
    fs::path p2{"C:\\Windows\\System32"};

    std::cout << "Path: " << p1 << "\n";
    return 0;
}
```

- Use `fs::path` to **construct file paths**.
- On Windows, use **double backslashes (`\\`)** or **raw strings (`R"()"`)**.

---

## **2. Inspecting Files and Directories**  

The library provides functions to **check file attributes**, such as existence, size, and type.  

### **Checking Existence**  
```cpp
if (fs::exists("file.txt")) {
    std::cout << "File exists\n";
}
```

### **File Type Checks**  
| **Function**              | **Checks if the path is...** |
|---------------------------|----------------------------|
| `fs::is_directory(p)`      | a directory |
| `fs::is_regular_file(p)`   | a normal file |
| `fs::is_symlink(p)`        | a symbolic link |
| `fs::is_empty(p)`          | empty (file or folder) |

### **Getting File Size**  
```cpp
std::cout << "File size: " << fs::file_size("file.txt") << " bytes\n";
```

### **Getting Last Modification Time**  
```cpp
auto time = fs::last_write_time("file.txt");
std::cout << "Last modified: " << time.time_since_epoch().count() << "\n";
```

---

## **3. Enumerating Directories**  

### **Listing Files in a Directory**  
```cpp
for (const auto& entry : fs::directory_iterator("path/to/directory")) {
    std::cout << entry.path() << "\n";
}
```

### **Recursive Directory Iteration**  
To list all files **including subdirectories**, use `recursive_directory_iterator`:  
```cpp
for (const auto& entry : fs::recursive_directory_iterator("path/to/directory")) {
    std::cout << entry.path() << "\n";
}
```

---

## **4. Manipulating Files and Directories**  

### **Creating Directories**  
```cpp
fs::create_directory("new_folder");
fs::create_directories("nested/folder/structure");
```

### **Copying Files**  
```cpp
fs::copy_file("source.txt", "destination.txt", fs::copy_options::overwrite_existing);
```

### **Moving/Renaming Files**  
```cpp
fs::rename("old_name.txt", "new_name.txt");
```

### **Deleting Files and Directories**  
```cpp
fs::remove("file.txt");             // Deletes a file
fs::remove_all("directory");        // Deletes a directory and all its contents
```

---

## **5. File Permissions**  

The library also allows **modifying file permissions**, following the POSIX model:  
```cpp
fs::permissions("file.txt", fs::perms::owner_all, fs::perm_options::add);
```

| **Permission Constant** | **Meaning** |
|-------------------------|-------------|
| `owner_read`           | Owner can read |
| `owner_write`          | Owner can write |
| `owner_exec`           | Owner can execute |
| `group_read`           | Group can read |
| `others_write`         | Others can write |

---

## **6. Handling Errors**  

### **Exceptions vs. Error Codes**  
Most functions **throw exceptions** by default, but you can **catch errors manually** using `std::error_code`:  

```cpp
std::error_code ec;
fs::remove("non_existent.txt", ec);
if (ec) {
    std::cout << "Error: " << ec.message() << "\n";
}
```

---

## **7. Practical Example: Directory Size Summary**  

This example **calculates the total size** of all files in a directory, including subdirectories.  

```cpp
#include <iostream>
#include <filesystem>
using namespace std;
namespace fs = std::filesystem;

uintmax_t calculate_directory_size(const fs::path& dir) {
    uintmax_t total_size = 0;
    for (const auto& entry : fs::recursive_directory_iterator(dir)) {
        if (fs::is_regular_file(entry)) {
            total_size += fs::file_size(entry);
        }
    }
    return total_size;
}

int main() {
    fs::path dir{"path/to/directory"};
    std::cout << "Total size: " << calculate_directory_size(dir) << " bytes\n";
}
```

---

## **8. Summary**  

| **Category**          | **Functions** |
|----------------------|--------------|
| **Path Operations** | `fs::path()`, `.filename()`, `.extension()` |
| **Inspection** | `fs::exists()`, `fs::is_directory()`, `fs::file_size()` |
| **Iteration** | `fs::directory_iterator()`, `fs::recursive_directory_iterator()` |
| **Manipulation** | `fs::copy()`, `fs::rename()`, `fs::remove_all()` |
| **Permissions** | `fs::permissions()` |
| **Error Handling** | Uses exceptions by default, or `std::error_code` |

The **Filesystem library** makes it easy to **write portable file and directory management code** in C++. Whether you're **listing files**, **checking attributes**, or **manipulating directories**, the `<filesystem>` API provides a unified and modern approach.