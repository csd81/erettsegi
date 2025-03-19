### ✅ TL;DR: Filesystem Error Handling  

- **Filesystem operations can fail** (file not found, permission denied, etc.).  
- Each filesystem function has **two ways to report errors**:  
  1. **Throw exception** (default behavior)  
     - Throws `std::filesystem::filesystem_error` (inherits from `std::system_error`).  
  2. **Use error codes**  
     - If you pass an `std::error_code` reference, the function won’t throw; it will set the error code instead.  

---

| ✅ Error Handling Style        | How it works                                              |
|--------------------------------|------------------------------------------------------------|
| **Without `error_code` param** | Throws `filesystem_error` exception on failure            |
| **With `error_code` param**    | Doesn’t throw; sets error_code value that you can check   |

---

### 👉 In short:  
- No error code param → exception.  
- With error code param → error info in variable, no exception.  

Want a quick example of both styles in code?