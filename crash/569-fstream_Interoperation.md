This example illustrates how `fstream` can interoperate with `std::filesystem` in C++17 and later. Instead of using strings or C-style paths, you can directly pass a `std::filesystem::path` to an `ifstream`, `ofstream`, or `fstream` constructor.  

### Key highlights of the example (Listing 17-9):
- **Argument validation**:  
  The program expects exactly one argument — the path to search — and exits with an error code otherwise.  
- **PE file extensions**:  
  A predefined `unordered_set` of common Windows PE file extensions is used to filter relevant files.  
- **Recursive directory iteration**:  
  `recursive_directory_iterator` combined with `directory_options::skip_permission_denied` allows you to safely iterate through large directory trees without failing on permission issues.  
- **File stream construction**:  
  Each file entry that matches the extension filter is opened using `ifstream file{ entry.path() };`. Notice that you don't need to convert the `path` to a string; it works directly.  
- **PE check logic**:  
  It reads the first two characters from the file and checks if they are `'M'` and `'Z'` — the "magic bytes" for Windows PE executables.  
- **Error handling**:  
  Wrapped in a `try-catch` to catch and report any file read errors or unexpected exceptions.  

---

### Cleaned-up code sample from the text:
```cpp
#include <iostream>
#include <fstream>
#include <filesystem>
#include <unordered_set>

using namespace std;
using namespace std::filesystem;

int main(int argc, const char** argv) {
    if (argc != 2) {
        cerr << "Usage: pecheck PATH" << endl;
        return -1;
    }

    const unordered_set<string> pe_extensions{
        ".acm", ".ax", ".cpl", ".dll", ".drv",
        ".efi", ".exe", ".mui", ".ocx", ".scr",
        ".sys", ".tsp"
    };

    const path sys_path{ argv[1] };
    cout << "Searching " << sys_path << " recursively.\n";

    size_t n_searched{};
    auto iterator = recursive_directory_iterator{ sys_path, directory_options::skip_permission_denied };

    for (const auto& entry : iterator) {
        try {
            if (!entry.is_regular_file()) continue;

            const auto& extension = entry.path().extension().string();
            if (pe_extensions.find(extension) == pe_extensions.end()) continue;

            ifstream file{ entry.path() };
            char first{}, second{};
            file >> first >> second;

            if (first != 'M' || second != 'Z') {
                cout << "Invalid PE found: " << entry.path().string() << "\n";
            }
            ++n_searched;
        } catch (const exception& e) {
            cerr << "Error reading " << entry.path().string() << ": " << e.what() << endl;
        }
    }

    cout << "Searched " << n_searched << " PEs for magic bytes." << endl;
}
```

---

### Want me to help adapt it for Linux ELF headers, or add multithreading or progress display?  
Let me know!