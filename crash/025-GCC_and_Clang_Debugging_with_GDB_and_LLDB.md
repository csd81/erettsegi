Here’s a clear and concise summary of the section you shared on debugging with GDB and LLDB:  

---

## **GCC and Clang Debugging with GDB and LLDB — Summary**

### **1. Debugging Tools**
- **GDB (GNU Debugger):**  
  - Powerful debugger for GCC.  
  - Install via:  
    ```bash
    sudo apt install gdb
    ```  
- **LLDB (Low-Level Debugger):**  
  - Designed for Clang but compatible with GDB commands.  
  - Can debug programs compiled with both GCC and Clang.  
  - Download from: [https://lldb.llvm.org](https://lldb.llvm.org)  
- **Xcode users:** LLDB is used behind the scenes.

---

### **2. Basic Debugging Workflow with GDB**
#### Step-by-step example:
1. **Navigate to your project folder.**  
2. **Compile with debug symbols:**  
   ```bash
   g++ main.cpp -o program_name -g
   ```  
3. **Start GDB:**  
   ```bash
   gdb program_name
   ```  
4. **Set breakpoints:**  
   - By line:  
     ```
     (gdb) break main.cpp:5
     ```  
   - By function:  
     ```
     (gdb) break main
     ```  
5. **Run the program inside GDB:**  
   ```
   (gdb) run
   ```  
6. **Step into each line of code:**  
   ```
   (gdb) step
   ```  
7. **Press Enter** to repeat the last command (continue stepping).  
8. **Step out of a function:**  
   ```
   (gdb) finish
   ```  
9. **Step over functions (without entering):**  
   ```
   (gdb) next
   ```  
10. **Inspect current variables:**  
   ```
   (gdb) info locals
   ```  
11. **Continue execution until the next breakpoint or program end:**  
   ```
   (gdb) continue
   ```  
12. **Exit GDB:**  
   ```
   (gdb) quit
   ```  

---

### **3. Additional Resources**
- Full GDB documentation: [https://sourceware.org/gdb/current/onlinedocs/gdb/](https://sourceware.org/gdb/current/onlinedocs/gdb/)  

---

If you’d like, I can create a small example program and show how to debug it live in GDB — want me to set that up?