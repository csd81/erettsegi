Awesome! Here’s a simple example of a TCP client and server using Boost.Asio in C++11 so you can see how all these pieces come together.  

### ✅ TCP Server Example (listening on port 8080):
```cpp
#include <iostream>
#include <boost/asio.hpp>

using boost::asio::ip::tcp;

int main() {
    try {
        boost::asio::io_context io_context;
        tcp::acceptor acceptor(io_context, tcp::endpoint(tcp::v4(), 8080));

        std::cout << "Server listening on port 8080...\n";

        while (true) {
            tcp::socket socket(io_context);
            acceptor.accept(socket);

            std::string message = "Hello from server!\n";
            boost::asio::write(socket, boost::asio::buffer(message));

            std::cout << "Sent message to client.\n";
        }
    }
    catch (std::exception &e) {
        std::cerr << "Error: " << e.what() << "\n";
    }

    return 0;
}
```

---

### ✅ TCP Client Example (connecting to localhost:8080):
```cpp
#include <iostream>
#include <boost/asio.hpp>

using boost::asio::ip::tcp;

int main() {
    try {
        boost::asio::io_context io_context;
        tcp::resolver resolver(io_context);
        auto endpoints = resolver.resolve("127.0.0.1", "8080");

        tcp::socket socket(io_context);
        boost::asio::connect(socket, endpoints);

        std::cout << "Connected to server.\n";

        boost::asio::streambuf buffer;
        boost::asio::read_until(socket, buffer, "\n");

        std::istream input(&buffer);
        std::string line;
        std::getline(input, line);

        std::cout << "Received from server: " << line << "\n";
    }
    catch (std::exception &e) {
        std::cerr << "Error: " << e.what() << "\n";
    }

    return 0;
}
```

---

### ✅ How to run:  
1. Compile the server:  
```bash
g++ -std=c++11 tcp_server.cpp -o server -lboost_system
```
2. Compile the client:  
```bash
g++ -std=c++11 tcp_client.cpp -o client -lboost_system
```
3. Run the server first:  
```bash
./server
```
4. Then run the client:  
```bash
./client
```

---

If you’d like, I can help make an asynchronous version, or one that echoes back client input. Want to go deeper? 😎