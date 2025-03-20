### ✅ **TL;DR: Setting Up C++ on Windows 10+ with Visual Studio**

---

### **1. Install Visual Studio with MSVC**
1. Download **Visual Studio 2017 Community Edition** from [https://ccc.codes/](https://ccc.codes/).  
2. Run the installer (allow it to update if needed).  
3. On the **Installing Visual Studio** screen, select:  
   - ✅ **Desktop Development with C++** workload.  
4. Click **Install** — this may take several hours (20GB–50GB typical).  
5. When finished, click **Launch**.

---

### **2. Set Up a New Project**
1. In Visual Studio, select **File → New → Project**.  
2. Under **Installed → Visual C++ → General**, select **Empty Project**.  
3. Name the project (e.g., `hello`) and click **OK**.

---

### **3. Add Your Source File**
1. In the **Solution Explorer** (left side), right-click **Source Files → Add → Existing Item**.  
2. Select your `main.cpp` file, or:  
   - Right-click **Source Files → Add → New Item** if you haven’t created one yet.  
   - Name it `main.cpp` and paste your code into the editor.

---

### **4. Build and Run**
1. Go to **Build → Build Solution** to compile the program.  
2. If errors appear, double-check your code and the error messages for hints.  
3. To run the program, select **Debug → Start Without Debugging** or press **Ctrl + F5**.  
4. You should see:
```
Hello, world!
Press any key to continue...
```

---

> Want me to help you make a portable Visual Studio project template so you can skip setup steps for future projects? I can guide you through that if you’d like!