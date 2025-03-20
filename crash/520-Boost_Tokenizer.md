Here’s a clear summary of the provided text:

The **Boost Tokenizer** (`boost::tokenizer`) is a class template that allows you to iterate over tokens in a string without allocating extra memory. It accepts three optional template parameters: a tokenizer function (to define delimiters), an iterator type, and a string type (defaulting to `std::string` and its const iterator).

- The tokenizer function determines delimiters. You can use `boost::char_separator<char>` to specify custom delimiters, for example:  
  ```cpp
  boost::char_separator<char>(";|,")
  ```
  will split on semicolons, pipes, and commas.
  
- Since `boost::tokenizer` doesn't allocate memory, it’s more efficient than `boost::algorithm::split` when you only need one pass over the tokens.

- A tokenizer works like a range with `begin()` and `end()`, returning input iterators that can be used in loops or manually iterated.

**Example (Listing 15-36)**:  
A tokenizer is used to split the string *"A man, a plan, a canal, Panama!"* by commas.  
Key steps:
- Define the string (`palindrome`), a `char_separator` for commas, and create a tokenizer from them.
- Iterate over the tokens with `begin()`.
- Dereference and compare each token to the expected string, then increment to move to the next token.

This demonstrates how easily Boost Tokenizer can handle custom delimiters and token iteration in a memory-efficient way.