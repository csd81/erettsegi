Here’s a clean, focused **Boost.Asio + ProgramOptions C++ Cheatsheet** you can keep handy:  

---

## 🔗 **Boost.Asio Core Concepts**  

### ➡️ Synchronous reads:  
```cpp
boost::asio::read(socket, buffer);
boost::asio::read_until(socket, dynamic_buffer, delimiter);
```

### ➡️ Synchronous writes:  
```cpp
boost::asio::write(socket, buffer);
```

### ➡️ Asynchronous reads/writes:
```cpp
boost::asio::async_read(socket, buffer, handler);
boost::asio::async_write(socket, buffer, handler);
```
**Handlers look like:**
```cpp
[](const boost::system::error_code& ec, std::size_t bytes_transferred) { }
```

---

## 🌐 **Simple HTTP Request (sync)**  
```cpp
boost::asio::ip::tcp::resolver resolver(io_context);
auto endpoints = resolver.resolve("example.com", "http");
boost::asio::connect(socket, endpoints);
boost::asio::write(socket, boost::asio::buffer(request_string));
boost::asio::read(socket, boost::asio::dynamic_buffer(response));
```

---

## 🤖 **Async Server Structure**  
- Use `ip::tcp::acceptor.async_accept()`.
- Each connection handled by a `Session` object with:
```cpp
async_read_until(socket, dynamic_buffer, '\n', handler);
async_write(socket, buffer(message), handler);
```
- Capture `shared_from_this()` in handlers.

---

## 🧵 **Multithreaded io_context**  
```cpp
for (int i = 0; i < n_threads; ++i)
    futures.push_back(std::async(std::launch::async, [&]{ io_context.run(); }));
```

---

## 🏁 **Program Termination Handling**  
- `std::atexit(callback)` — call on exit.  
- `std::exit(code)` — clean exit (calls destructors for static/thread_local).  
- `std::abort()` — immediate stop, no cleanup.  
- Handle `SIGINT` with:
```cpp
std::signal(SIGINT, handler);
```

---

## ⚙️ **Boost.ProgramOptions Quick Reference**  
### Setup:
```cpp
boost::program_options::options_description desc("Usage:");
desc.add_options()
    ("help,h", "show help")
    ("threads,t", value<int>()->default_value(4), "thread count")
    ("pattern", value<std::string>(), "search pattern")
    ("path", value<std::vector<std::string>>(), "paths to search");
```
### Parse:
```cpp
auto parsed = command_line_parser(argc, argv).options(desc).positional(pos).run();
variables_map vm;
store(parsed, vm);
notify(vm);
```
### Access values:
```cpp
if (vm["help"].as<bool>()) { /* show help */ }
int threads = vm["threads"].as<int>();
std::string pattern = vm["pattern"].as<std::string>();
auto paths = vm["path"].as<std::vector<std::string>>();
```

---

## 🚀 **Compiler Flags**  
| Flag   | Meaning                               |
|--------|---------------------------------------|
| `-O0`  | No optimization (debug-friendly)      |
| `-O2`  | Good performance, good binary size    |
| `-O3`  | Aggressive optimization               |
| `-Os`  | Optimize for size                     |
| `-Ofast` | Optimize ignoring strict standards |

---

## ✅ **Header Best Practice**  
```cpp
#pragma once
```
(instead of `#ifndef` guards)

---

## ⚡ **Linking with C**  
```cpp
extern "C" {
    int sum(const int* x, int len);
}
```

---

> Want me to make this into a PDF or a markdown doc for download? 😊