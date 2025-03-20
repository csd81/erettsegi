**TL;DR – Compound Statements (Blocks)**  

- **Compound statements** are groups of statements enclosed in `{}`.  
- They create a new **block scope**, meaning variables declared inside are only accessible there and get destroyed when the block ends.  
- Destruction of block-scope variables happens in **reverse order** of their creation.  

**Example (Listing 8-2):**  
- Tracer objects show construction/destruction order.  
- Entering a block: objects are created.  
- Exiting the block: objects are destroyed in reverse order.  

👉 **Takeaway:** Blocks let you group multiple statements and control scope and lifetime of temporary objects.