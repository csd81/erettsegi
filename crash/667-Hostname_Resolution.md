**TL;DR: Hostname Resolution in Boost Asio**  

- To convert a hostname (like `www.example.com`) to an IP address, use `boost::asio::ip::tcp::resolver`.  
- **Blocking example:**  
  - Create `io_context` and `resolver`.  
  - Call `resolver.resolve(hostname, service)`; iterate results to get `host_name`, `service_name`, and `endpoint`.  
  - Handle errors via `boost::system::error_code`.  

- **Asynchronous example:**  
  - Use `async_resolve(host, service, callback)`.  
  - In the callback, check for errors and iterate through results.  
  - Call `io_context.run()` to process the async operation.  

👉 In short: `resolve()` is blocking; `async_resolve()` is non-blocking and requires a callback + `io_context.run()`.