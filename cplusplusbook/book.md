 
---

## PREFACE

I primarily recommend this book to students preparing for the advanced-level high school graduation exam in computer science, as the knowledge and tasks primarily align with those requirements. However, with the supplementary topics (fundamentals of object-oriented programming, basics of Windows applications), it can also be useful for vocational training foundation subjects and for self-study.

I chose C++ and C# as the programming languages so that the acquired knowledge can also be used after graduation.  
I rewrote the programming exercises to be closer to the C language. Array indexing starts from zero, and I supplemented them with variations not found in standard collections of algorithms but that have appeared in final exams (e.g., custom sorting).  

The development of Windows applications is explained step by step with a simple example, guiding the reader through the process. I recommend it to everyone who wants to try software development in an entertaining way.  

Due to space constraints, the book contains only a few complete program codes. Additional programs related to the book can be downloaded as supplementary material from the publisher's website:  
 
---

## 1. INTRODUCTION  

### GENERAL STRUCTURE OF A PROGRAM  

A computer program consists of the following parts: data structure, business logic, and user interface. Of course, in a short program with only a few lines, these parts are not very distinct. But with software consisting of a million lines, the situation is quite different.  

#### Data Structure  
The program needs to store the data it uses (whether permanent or temporary). To do this, we use various data structures (variables, files, databases). We choose the appropriate data structures according to the task. The foundation of every program is a well-chosen data structure, and special attention should be given to its design and consideration.  

#### Business Logic  
Sometimes business logic consists of only a few simple lines, while other times it is a complex, lengthy set of lines. This is also called the application logic. The business logic makes up the "soul" of the program. It defines what the program does. (This has nothing to do with commerce.)  

#### User Interface  
The program user interacts with the user interface. This is where the program’s messages, results, and questions are displayed. It can be a typical Windows-style interface, a web interface, or even just a text-only display. In all cases, it is important to ensure clarity and simplicity.  

---

### CONSOLE APPLICATIONS  

Programs that display only text are called **console applications**.  
At the graduation exam, it is expected that all requested and displayed data be accompanied by textual explanations. One must be able to write console applications for the exam.  

The significance of console applications is that they are the simplest way to practice and learn new software techniques. Sometimes, for technical or financial reasons, a graphical interface is not feasible or necessary.  

In web development, the appearance is especially important, and developing a user interface requires significant human resources, often involving web designers.  

---

## ALGORITHMS  

### The Concept of an Algorithm  

When given a task, solving it involves a series of steps. Whether it’s cooking a dish or adding two numbers (by hand or with a calculator), the solution consists of steps that follow each other.  

**We call an algorithm the sequence of steps suitable for solving a task.**  

Examples of algorithms include cooking recipes, step-by-step assembly instructions, descriptions of chemical experiments, and methods for prime factorization.  

The steps are often expressed as instructions (e.g., “Break three eggs!”). While we may soften our language for politeness in conversation, algorithms use clear, direct commands.  

---

### Tools for Describing Algorithms  

Algorithms are typically described in ways that are independent of programming languages. This has two advantages:  
1. The description is shorter and clearer.  
2. Everyone can understand it, even without knowing programming languages.  

- **The most commonly used format is the sentence-based description**, similar to how recipes are written.  
- **Flowcharts** can also be used to visually present shorter algorithms. The steps are represented by different shapes, and arrows indicate their sequence. This is a clear and easily understandable method. However, for large algorithms, such graphical representation becomes problematic.  
- Another method is **pseudo-code**, where the building blocks are predetermined and standardized.  

---

### Providing an Algorithm with a Flowchart  

Let’s take a simple task: ask the user for two numbers, add them, and display the result.  
- **Parallelograms** indicate input/output,  
- **Rectangles** indicate execution steps,  
- Flowcharts always begin with **START** and end with **STOP**.  

---

### Providing an Algorithm with Sentence-Based Description  

The steps are written down in sequence.  
Example for an addition program:  
```
Input: a  
Input: b  
c := a + b  
Output: c
```  
There are other agreed-upon sentence-based descriptions, which will be introduced later under control structures.  

---

## ALGORITHMIZATION  

Creating the algorithm is called algorithmization.  
Sometimes, the necessary steps are immediately clear. Other times, we have to think long and apply various techniques. It may also happen that the problem has no solution.  

A task can be easily algorithmized if it can be related to previously known formulas, types of algorithms, or methods.  

---

## PROGRAMMING LANGUAGES  

### Machine Code  

Initially, computers were programmed directly in machine code. The bytes of the program were entered into the computer one by one.  

The attached image shows a machine code program in the memory of a Commodore Plus 4 computer, starting at memory location **2000**.  

Each two-digit hexadecimal number (e.g., A9) represents one byte.  
The image shows the Neumann principle: instructions and data are stored together in memory. For example, A9 is an instruction, 02 is data (in this case, the code for the color dark red), and so on.  

Writing programs in machine code was tedious and required great expertise. One had to understand how the computer’s internals worked, down to how the processor “thinks.”  

Today, computers only execute machine code programs. Under Windows, we encounter them with the **exe** extension. Such programs are commonly called **binaries**.  

---

Here’s the full English translation of the provided pages:

---

### **Page 13**

**Assembly**

The appearance of assembly made things somewhat easier, where the still short machine code instructions were replaced by characteristic names. In the image, next to the machine code, the assembly instruction also appears: for example, the A9 instruction corresponds to LDA (Load Accumulator), and 8D corresponds to STA (Store the Accumulator).

Originally, programs developed in machine code or assembly occupy little space and run very fast. However, developing them is difficult, requires great expertise, and is extremely slow and expensive. In the era of fast computers, machine code is only used for special purposes. This includes illegal modifications and hacking.

**High-level programming languages**

Assembly also turned out to not be an efficient enough tool. There was a need to express thoughts in a way closer to human thinking. This led to the creation of the predecessors of today’s programming languages, such as C, Pascal, and Basic. Programming in these languages is much easier than in machine code and requires a more human-like approach. The developer writes the program in C, which is called **source code**. The source code is then converted into machine code (binary) by a **C compiler**.

Programs compiled into binary code will never be as small and fast as those written directly in machine code because compilers add unnecessary overhead. Over time, compilers have become increasingly advanced, but perfection has never been achieved. The choice remains between small and fast or cheap and wasteful. The accelerated business world tends to favor the latter. Increasingly faster and higher-capacity machines help with this.

Programming languages that are closer to human thinking are called **high-level languages**, and machine code or assembly are referred to as **low-level languages**. 

Writing a few hundred lines of simple programs is sufficient using high-level languages and structured programming (for example, for microcontroller programs or smaller web scripts). No more is expected at the graduation exam level.

---

### **Page 14**

**Object-oriented programming**

Over time, the size and complexity of software demanded by the market increased to the point that traditional high-level, structured programming could no longer produce solutions that were fast, economical, and extendable enough. Therefore, a new method had to be developed: object-oriented programming.

Object-oriented programming extended already existing high-level languages (C, Pascal, Basic). This resulted in the creation of C++, C#, Java, Object Pascal, Delphi, and others.

Object-oriented source code is compiled into binary executable code by compilers. Programs developed this way are larger and slower than those created by traditional structured programming (see Windows).

**Graphical development environments**

The market demands even faster and more efficient development with increasingly complex programs. To achieve this, graphical development environments are created, allowing developers to build programs with minimal coding.

The book introduces Visual Studio, where buttons, menus, and other necessary elements for Windows applications can be dragged onto windows with the mouse. The environment generates the code for us. The program sections corresponding to events (e.g., clicking) can still be written manually. There are also development environments where control structures (e.g., loops) can be added and configured graphically.

In general, the more convenient a development environment is, the more space it takes, and the larger and slower the program compiled from it will be. The more automatic and convenient the environment, the less flexible it is and the less it supports unique and individual solutions. Often, parts of the code cannot be accessed manually and can only be generated by the development environment.

---

### **Page 15**

**Development environments for business and free use**

Free development environments are usually less sophisticated, offer fewer features, and are harder to handle compared to their commercial counterparts. The book mentions Code::Blocks, which only supports writing code and cannot embed Windows application elements.

With business development environments, work can proceed quickly. You only need to design parts of the code; the environment generates the rest based on the plan. Their biggest drawback is the high price, but for a well-performing software developer company, the investment quickly pays off due to fewer man-hours.

A common trick used for educational purposes is “baiting” by offering a free development environment. Many of my acquaintances have fallen for this: they learned programming in such an environment, only to later realize that creating sellable software required the commercial version. The company couldn't afford the price as a small business, so they had to rewrite their program in a free environment over the next three years.

Another environment discussed in the book is Visual Studio Express, an excellent example for educational use. It's free for learning purposes but not for commercial software development. For commercial development, one should buy the Visual Studio Professional (or Enterprise) version or use the free, but more limited, Visual Studio Community edition.

**Errors**

Wherever humans work, errors can occur, disrupting or making the program's operation impossible. These errors can be syntactic or semantic.

**Syntactic errors**

Syntactic, or formal errors, are **language errors that prevent the compiler from accepting the code**. Causes include:
- Typographical errors: missing or incorrect letters in commands.
- Missing required semicolons at the end of statements.
- Unmatched opening or closing brackets.

Syntactic errors are generally easy to find by carefully reviewing the code. Development environments help by showing where the error occurred during compilation. Often the error message points to the location and nature of the error.

---

### **Page 16**

**Semantic error**

Semantic, or content errors, occur when **the program compiles but does not do what we expect from it**. It might crash, give incorrect results, or stop due to illegal operations (runtime error).

Semantic errors are harder to find than syntactic errors. They are uncovered through thorough **testing**. Some appear during development testing, but some may only surface years later as hidden bugs.

**Development = coding + immediate testing**

Developing a program involves writing code line by line and, in the best case, testing the program after each part is completed and fixing any errors. The best possible test is to ensure the program compiles without errors and runs as expected.

Testing is a time-consuming process. Everyone would like to spend as little time as possible on it, since the client doesn’t pay for it, and exams don't award points for it. Still, it’s better to test frequently than write large portions at once and only then test, which can lead to difficult-to-find errors.

Beginners should test after every two lines of code! If instructions have many parameters, test every two parameters. Later, instincts will develop, and the ratio between immediate testing and coding will adjust to the appropriate level. Some parts will require more frequent testing, others less.

---


Here’s the full English translation of the provided pages:

---

### **Page 13**

**Assembly**

The appearance of assembly made things somewhat easier, where the still short machine code instructions were replaced by characteristic names. In the image, next to the machine code, the assembly instruction also appears: for example, the A9 instruction corresponds to LDA (Load Accumulator), and 8D corresponds to STA (Store the Accumulator).

Originally, programs developed in machine code or assembly occupy little space and run very fast. However, developing them is difficult, requires great expertise, and is extremely slow and expensive. In the era of fast computers, machine code is only used for special purposes. This includes illegal modifications and hacking.

**High-level programming languages**

Assembly also turned out to not be an efficient enough tool. There was a need to express thoughts in a way closer to human thinking. This led to the creation of the predecessors of today’s programming languages, such as C, Pascal, and Basic. Programming in these languages is much easier than in machine code and requires a more human-like approach. The developer writes the program in C, which is called **source code**. The source code is then converted into machine code (binary) by a **C compiler**.

Programs compiled into binary code will never be as small and fast as those written directly in machine code because compilers add unnecessary overhead. Over time, compilers have become increasingly advanced, but perfection has never been achieved. The choice remains between small and fast or cheap and wasteful. The accelerated business world tends to favor the latter. Increasingly faster and higher-capacity machines help with this.

Programming languages that are closer to human thinking are called **high-level languages**, and machine code or assembly are referred to as **low-level languages**. 

Writing a few hundred lines of simple programs is sufficient using high-level languages and structured programming (for example, for microcontroller programs or smaller web scripts). No more is expected at the graduation exam level.

---

### **Page 14**

**Object-oriented programming**

Over time, the size and complexity of software demanded by the market increased to the point that traditional high-level, structured programming could no longer produce solutions that were fast, economical, and extendable enough. Therefore, a new method had to be developed: object-oriented programming.

Object-oriented programming extended already existing high-level languages (C, Pascal, Basic). This resulted in the creation of C++, C#, Java, Object Pascal, Delphi, and others.

Object-oriented source code is compiled into binary executable code by compilers. Programs developed this way are larger and slower than those created by traditional structured programming (see Windows).

**Graphical development environments**

The market demands even faster and more efficient development with increasingly complex programs. To achieve this, graphical development environments are created, allowing developers to build programs with minimal coding.

The book introduces Visual Studio, where buttons, menus, and other necessary elements for Windows applications can be dragged onto windows with the mouse. The environment generates the code for us. The program sections corresponding to events (e.g., clicking) can still be written manually. There are also development environments where control structures (e.g., loops) can be added and configured graphically.

In general, the more convenient a development environment is, the more space it takes, and the larger and slower the program compiled from it will be. The more automatic and convenient the environment, the less flexible it is and the less it supports unique and individual solutions. Often, parts of the code cannot be accessed manually and can only be generated by the development environment.

---

### **Page 15**

**Development environments for business and free use**

Free development environments are usually less sophisticated, offer fewer features, and are harder to handle compared to their commercial counterparts. The book mentions Code::Blocks, which only supports writing code and cannot embed Windows application elements.

With business development environments, work can proceed quickly. You only need to design parts of the code; the environment generates the rest based on the plan. Their biggest drawback is the high price, but for a well-performing software developer company, the investment quickly pays off due to fewer man-hours.

A common trick used for educational purposes is “baiting” by offering a free development environment. Many of my acquaintances have fallen for this: they learned programming in such an environment, only to later realize that creating sellable software required the commercial version. The company couldn't afford the price as a small business, so they had to rewrite their program in a free environment over the next three years.

Another environment discussed in the book is Visual Studio Express, an excellent example for educational use. It's free for learning purposes but not for commercial software development. For commercial development, one should buy the Visual Studio Professional (or Enterprise) version or use the free, but more limited, Visual Studio Community edition.

**Errors**

Wherever humans work, errors can occur, disrupting or making the program's operation impossible. These errors can be syntactic or semantic.

**Syntactic errors**

Syntactic, or formal errors, are **language errors that prevent the compiler from accepting the code**. Causes include:
- Typographical errors: missing or incorrect letters in commands.
- Missing required semicolons at the end of statements.
- Unmatched opening or closing brackets.

Syntactic errors are generally easy to find by carefully reviewing the code. Development environments help by showing where the error occurred during compilation. Often the error message points to the location and nature of the error.

---

### **Page 16**

**Semantic error**

Semantic, or content errors, occur when **the program compiles but does not do what we expect from it**. It might crash, give incorrect results, or stop due to illegal operations (runtime error).

Semantic errors are harder to find than syntactic errors. They are uncovered through thorough **testing**. Some appear during development testing, but some may only surface years later as hidden bugs.

**Development = coding + immediate testing**

Developing a program involves writing code line by line and, in the best case, testing the program after each part is completed and fixing any errors. The best possible test is to ensure the program compiles without errors and runs as expected.

Testing is a time-consuming process. Everyone would like to spend as little time as possible on it, since the client doesn’t pay for it, and exams don't award points for it. Still, it’s better to test frequently than write large portions at once and only then test, which can lead to difficult-to-find errors.

Beginners should test after every two lines of code! If instructions have many parameters, test every two parameters. Later, instincts will develop, and the ratio between immediate testing and coding will adjust to the appropriate level. Some parts will require more frequent testing, others less.

### **page 17** 

---

### **Data Streams**

From the central part of the computer to the peripherals (for example, the monitor or storage devices), bytes arrive in the correct order, one after another, as data streams. In technical terminology, these data streams are called **streams**. For example, in a console window, characters appear in the order they are written, from left to right.

**(Illustration: stream from the computer to the monitor with reversed text turning into “Hello World!”)**

Every data stream has a memory area where bytes can temporarily wait. This is necessary because data can reach the central part so quickly that the peripheral may not be able to receive it immediately. This temporary waiting area is called a **buffer**, and the process of utilizing it is called **buffering**.

Buffering is important because if we interrupt the data stream too early, data loss can occur, as the data stored in the buffer may not reach its destination (such as the storage device).

From the peripheral side toward the central part of the computer (like from a keyboard or storage), we also use data streams that have buffer areas in memory.

---

If you’d like, I can compile all translated pages into a single document for you!



Here is the full English translation of the five pages you provided:

---

## Page 1 (original page 18)

**HELLO WORLD**

Traditionally, when learning a new programming language, we begin by displaying the text "Hello World!" on the screen.

### C#

1. Open Visual Studio Express.
2. In Visual Studio, we write programs within the framework of a project.  
   Therefore, let's start a new project using the **File/New Project** menu option.
3. In the left panel, select the programming language:  
   **Installed/Templates/Visual C#**.
4. In the middle panel, choose the console application:  
   **Console Application**.
5. In the lower panel of the window, specify the project name:  
   **Name: hellovilag**.
6. Specify the folder where you would like the project files to be saved, e.g.,  
   **Location: D:\works\**.

---

## Page 2 (original page 19)

7. Click the **OK** button. After a short wait, Visual Studio will prepare the file system for the project, and the code editor will appear where you can write your program.
8. We will write our programs inside a block that starts with `static void Main`. Find this block and press **Enter** while standing between the curly braces. The cursor will blink inside the braces.
9. To display text on the console screen, use the **Console.WriteLine** command. In parentheses and quotation marks, enter the text you wish to display.  
   *Type it exactly, paying attention to case sensitivity:*  
   ```csharp
   Console.WriteLine("Hello World!");
   ```
10. If we run the program now, the console window would appear for a moment, display the text, and then close immediately. It would happen so fast that we would only see a blink. Let's add another command that keeps the console window open until we press Enter.  
   *Type it exactly, paying attention to case sensitivity:*  
   ```csharp
   Console.ReadLine();
   ```
11. The finished program can now be compiled into machine code and executed. Both steps can be performed at once in the development environment:  
   *Click the Start button.*  
   As a result, a black background window will appear with white characters showing "Hello World!".
12. If the program doesn't work, look for errors. The development environment helps by underlining errors and showing details in the **Error List** window below, including the probable cause (in the **Description** field) and the line number (**Line**). After fixing the error, restart the program.

---

## Page 3 (original page 20)

### C++

1. Open **Code::Blocks**.
2. Start creating a new C++ file using the **File/New/File** menu option.
3. In the upper right panel, select the appropriate category: **C/C++ source**, and click the **Go** button.
4. In the next window, select the programming language from the list on the right: **C++**, then click **Next**.
5. In the next window, click the icon next to the **Filename with full path** field. A file browser window will appear, as is typical in Windows applications.
6. Navigate to the desired folder where the C++ file should be saved (e.g., **D:\works\**).
7. In the **Filename** field, type the file name: **hellovilag**.
8. Complete the file creation by clicking the **Finish** button. The workspace will appear, and you can begin typing your program.
9. In C++, available commands are organized into function libraries. We need to indicate at the beginning of the code which libraries we want to use. To print text to the console, we need the **iostream** library.  
   *Type it exactly, paying attention to case sensitivity:*  
   ```cpp
   #include <iostream>
   ```
10. For easier typing (fewer characters to type), it's good to set the default namespace:  
   *Type it exactly, paying attention to case sensitivity:*  
   ```cpp
   using namespace std;
   ```
11. Now let's create the main program block, where our commands will go.  
   *Type it exactly, paying attention to case sensitivity:*  
   ```cpp
   int main() {
   }
   ```
12. The command to print text to the console will go between the curly braces. Stand between the braces and press **Enter** to open a new line.

---

## Page 4 (original page 21)

13. If we want to display accented Hungarian characters correctly in the console window, we must set the console language to Hungarian.  
   *Type it exactly, paying attention to case sensitivity:*  
   ```cpp
   setlocale(LC_ALL, "hun");
   ```
14. Press **Enter** to move to a new line.
15. We can use the **cout** (Console OUTput) command to display text in the console. The **endl** keyword moves the output to a new line.  
   *Type it exactly, paying attention to case sensitivity:*  
   ```cpp
   cout << "Hello World!" << endl;
   ```
16. The finished program can now be compiled into machine code and run. Both steps can be performed at once in the development environment:  
   *Click the Build and Run icon in the menu bar.*  
   As a result, a black background window will appear with white characters showing the text "Hello World!".
17. If the program doesn't work, look for errors. The development environment will highlight the probable line of the error with a red marker, and the **Build messages** window below will show the likely cause (in the **Message** field) and the line number (**Line**). After fixing the error, restart the program.

---

## Page 5 (original page 22)

### FREQUENT QUESTIONS

**Line numbers are not visible in C#. How can I turn them on?**  
Go to the **Tools/Options** menu, select the **Text Editor/C#** category, then in the **Display** panel, check **Line numbers**.

---

**I want to transfer a program under development to another computer. What do I need to copy?**  
- **C#:** Copy the entire project directory, including subdirectories and files.  
  Example: `d:\works\hellovilag\`  
- **C++:** Copy the `.cpp` file.  
  Example: `D:\works\hellovilag.cpp`

---

**I want to run the finished program without a development environment. How do I deploy it?**  
- **C#:** The compiled program is located in a folder with the project name, under `hellovilag\bin\Debug` (e.g., `hellovilag.exe`). Copy this file to another folder, drive, or machine. The `.exe` file created by Visual Studio will work. If it was built with Visual Studio Express, it is not suitable for commercial distribution.  
  Example: `d:\works\hellovilag\hellovilag\bin\Debug\`
- **C++:** The compiled program is located where you created the `.cpp` file. Copy the file to another folder, drive, or machine — it will work without Code::Blocks.  
  Example: `d:\works\`

---

**Small windows with instructions pop up while typing. What are they for, and how do I use them?**  
This is a convenience feature of the development environment called **auto-completion**. After typing a few characters, a list appears from which you can choose using the arrow keys. The selected instruction can be inserted into the code by pressing the **Tab** key. If you can't remember the full instruction, this feature helps by suggesting possible completions.

---

Here is the full translation of the provided pages:

---

### NOTES IN THE PROGRAM

#### Concept
Notes are sections in the code that the compiler does not attempt to execute. They only exist in the source file.  
Notes are also called comments. The act of adding notes to the code is called commenting.  

We use comments as reminders for ourselves, for example, about what a certain piece of code is for. If we do not touch a program for a year and then need to modify it (extend or fix it), we are unlikely to remember what we coded and why.  

Programs are often developed by multiple people. The code we write should be understandable to others as well. A comment can contain explanatory text, thus increasing the readability of the code.  

Comments can also be practical for testing. If we want to temporarily disable a line of code, we can comment it out. The program will still run without that line, and we can check for errors by looking at the commented-out section.  

#### Creation
We can create a comment by placing `/*` at the beginning and `*/` at the end (examples 1-3).  
A line following `//` will be a comment until the end of that line (examples 6 and 8).

**C# version:**
```
1)  /* Hello World!
2)  2018.04.01.
3)    */
4)  static void Main(string[] args)
5)  {
6)  //main program
7)      Console.WriteLine("Hello World!");
8)      Console.ReadLine(); //waiting for Enter key
9)  }
```

**C++ version:**
```
1)  /* Hello World!
2)  Created: 2018.04.01.
3)  Created by:   */
4)  #include <iostream>
5)  using namespace std;
6)  //main program
7)  int main()
8)  {
9)      setlocale(LC_ALL,"hun"); //accented characters
10)     cout << "Hello World!" << endl;
11) }
```

---

### Tasks

1. Create and run a program named `hellovilag`.
2. Expand the previous program by displaying your own name below "Hello World!".
3. Introduce an error in the program and try to compile it. Check the development environment's feedback on the error: the underline in the code and the error message window below.
4. Extend the previous program with multi-line and single-line comments explaining what each command does.
5. Expand the program with a multi-line header comment at the beginning of the program where you write your name, the current date, and lines describing the software and hardware conditions (machine type, operating system, development environment).

---

### SUMMARY

The steps of program development are as follows:

1. **Thorough study of the task and assessing client requirements.**
2. **Planning:** In the case of a simpler program (such as a high school exam), this can be done in your head. For more complex programs, plans are documented with the help of supportive programs.
   - a) Decide what **data structures** to use.
   - b) Note down which **algorithms**, formulas, programming elements (see Chapter VI), or unique solutions will be applied. These notes can be made as comments or on paper.
3. **Coding** in the chosen programming language. During coding, perform **basic tests and error fixes**. This helps eliminate syntactic and simple semantic errors. The result is a working program whose correct operation is verified.
4. **Basic testing and error correction** continue to remove deeply embedded semantic errors (bugs).
5. **Documenting the program** from planning to testing.  
6. After completion, **deliver the finished program** and, if needed, install it on the client's computer.
7. Later, clients may request enhancements or new functions, requiring **updates**. If an error is found afterward, it may be necessary to replace the program on the client's computer with an updated version, i.e., **refresh** it.

The most critical part, according to experience, is continuous communication with clients. Even a year-long development can fail if there is no communication, causing the client to lose trust. Client requirements change constantly. The previously mentioned steps can slip and repeat.  

In large software companies, handling client communication is often a separate job. However, in typical software development, only about 20% is spent on coding, 40% on planning, and 40% on the most time-consuming part — testing.

---

### VARIABLES

#### Overview

**Definition of a variable**  
Variables allow us to use the RAM’s data storage capacity. RAM consists of memory cells with addresses and byte-sized compartments. It would be cumbersome to memorize and use memory addresses. Often, one byte is not enough for storing data, so multiple bytes are combined. Instead of remembering each address separately, we assign a collective name to those bytes, and this name is used to refer to them.  

Thus, we can define a **variable** as: *a part of the RAM that we can refer to by name.*

---

### Variable names

Variable names have restrictions depending on the programming language. Typically, they cannot contain special characters (like comma, semicolon, period), cannot consist of multiple words, and it’s best to avoid accented letters (although C# allows them). Also, they cannot conflict with language commands or keywords.  

It’s possible but not advisable to use overly long variable names. It makes the code harder to read and write. Many use short variable names in smaller programs, but in longer ones, they are easily forgotten. It is recommended to use short but descriptive names.  

There are commonly accepted conventions:  
- loop variables are often `i`, `j`, `k`.  
- short variables for frequent uses, longer descriptive ones for more significant roles.

---

### Types and declaration

Different data types are stored differently: integers in binary, floating-point numbers, characters by their code value, etc. Thus, variables have **types**.  

Some programming languages automatically recognize variable types — these are called **weakly typed languages** (like Basic, PHP).  

Others require variables to be declared before use — these are **strongly typed languages**, such as C++, C#, Pascal, Java. The declaration includes the type, name, and reserves space in memory.  

**Most commonly used variable types:**

| Type          | Keyword  | Values                               | Size         | Comment                                 |
|---------------|----------|--------------------------------------|--------------|----------------------------------------|
| Logical       | bool     | true/false                           | 1 bit        |                                        |
| Integer       | int      | -2,147,483,648 ... 2,147,483,647     | 4 bytes      |                                        |
| Floating-point| float    | 3.4E-38 ... 3.8E+38                  | 4 bytes      | Accurate to 6 decimal places          |
| Double        | double   | 1.7E-308 ... 1.7E+308                | 8 bytes      | Accurate to 16 decimal places         |
| Character     | char     | 1 character                          | 1 byte       | 256 characters, ASCII code range      |
| String        | string   | Sequence of characters               | 1 byte/char  |                                        |

**Example of declaring variables in C++ and C#:**
```cpp
int kor;
string nev;
bool letezik;
char jel;
int i, j, k;
```

---

Here’s the full English translation of the pages you provided (pages 29–33):

---

### Page 29

## Assignment (Value assignment)

Data can be assigned to a variable. In sentences, assignment is denoted by:
```
k := 1
```
And we read it as: k is equal to 1. This means that from now on, the variable `k` has the value 1, until we change it.  

Assignment can also occur between variables of the same type. For example:
```
i := j
```
This means that from now on, `i` has the same value as `j`. The reverse is not true! The left-hand side always receives the value from the right-hand side.

Multiple assignments also work. In this case, values are assigned from right to left. In the following example, first `k` gets the value 1, then `j` gets the value of `k`, and finally `i` gets the value of `j`:
```
i := j := k := 1
```
A declaration in most programming languages does not immediately mean that the variable is set to zero or emptied. The state of the reserved memory location defines the variable's initial value if we don't assign it one. The memory's state is unknown to us, as it depends on prior usage. Initially, the variable's memory space might be filled with garbage data.

---

### Encoding assignment

In C++ and C# languages, the colon (:=) is omitted.  
The assignment can happen in the declaration:
```
int i = 0;
```
or independently:
```
int i;
i = 0;
```
Both solutions are equivalent.  

For the types of variables introduced, assignment can be done as follows in C++ or C#:
```
int db = 0;
float vsz = 0.345;
bool talalat = true;
char jel = '+';
string nev = "Glázer Bozsó";
```

---

### Page 30

Let’s pay attention that when using strings, they must be placed between quotation marks (" "), not apostrophes (' '). For floating-point numbers, use a period (.) as a decimal separator, not a comma (,).

## Choosing the variable type

It is advisable to consider the following points in order:

1. The variable should be able to store the selected data. The planned maximum and minimum values should fit within the variable’s range and it should be accurate enough.

2. Think about what operations will be performed on the variable. For example, if we want to deduce the district in Budapest from a postal code (based on the middle two digits), it’s practical to declare it as a string, since it’s easier to extract those two digits than calculating them. Usually, if a number is only used for identification, and no calculations are performed with it, it's better to store it as a string.

3. The less memory it occupies, the better. Storing a person’s gender as a string ("male"/"female") takes up 5 bytes. Using a logical value (true/false) requires only 1 bit.

## Constant

A constant is a variable whose value cannot change during the program's execution. After declaration, its value cannot be modified.

It makes sense to use constants for values that are frequently referenced in a program and do not change. For instance, the screen’s horizontal or vertical resolution. Beginners might hardcode such values everywhere. But if it turns out that the resolution is not 1024 but 1280, every occurrence must be changed manually, which is tedious and prone to errors. Instead, it is better to define constants at the beginning and use their names throughout the program.

If you find yourself writing the same number many times, it should be replaced with a constant. The same applies to character strings frequently used in the program.

---

### Page 31

Constant declarations are done by writing the `const` keyword before the variable name. For example:
```
const int vf = 1280;
```

### Tasks

1. Declare two integer variables named `szamla` and `nevezo`.
2. Declare a character variable named `betu`.
3. Declare a variable named `vnev` to store a last name.
4. Declare a floating-point variable named `atlag` to store the average of grades with two decimal places.
5. Declare a string variable named `mobilszam` to store a phone number like 06301234567.
6. Declare an integer variable named `kor` for storing an age.
7. Declare two boolean variables: `andras` and `bela`.
8. Set `szamla` to 24.
9. Set `nevezo` to 32.
10. Set `betu` to 'B'.
11. Set `mobilszam` to "06209876543".
12. Set `kor` to 29.
13. Set `andras` to `true` and `bela` to `false`.
14. Declare constants for screen resolution with names `vf`, `ff` and assign values to them.
15. Declare an integer variable named `irsz` for postal codes and set its value to 1234.
16. Declare a variable named `tulaj` to track whether a property owner or tenant is being recorded. Declare the appropriate type and give it an initial value.

---

### Page 32

## DATA INPUT AND OUTPUT IN THE CONSOLE WINDOW

### Displaying a variable

The content of variables can be displayed in the console window. Instead of writing out "Hello World!" in quotes, we replace the text with the variable name.

| Sentence form         | C#                                        | C++                     |
|-----------------------|-------------------------------------------|-------------------------|
| t := 35; Output: t   | int t = 35; Console.WriteLine(t);         | int t = 35; cout << t << endl; |

If we omit `<< endl` in C++ or do not use `WriteLine` in C# (using only `Write`), the output will continue on the same line.

Sometimes, we need to print multiple variables and text together. For example, if `t := 35` and `k := 24`:
```
The area of the rectangle is 35 sq. m, the perimeter is 24 m.
```
In sentence form:
```
Output: "The area of the rectangle is ", t, " sq. m, perimeter is ", k, " m."
```

### In C#:
1. The output text goes inside quotation marks.
2. Variables are written after the text, separated by commas.
3. In the text, we place placeholders `{0}`, `{1}`, etc., where we want to insert variable values. `{0}` is replaced by the first variable (`t`), `{1}` by the second (`k`), etc.

Example:
```
Console.Write("The area of the rectangle is {0} sq. m, perimeter is {1} m.", t, k);
```

---

### Page 33

### In C++:
1. Break the output string where variables are inserted.
2. Place the broken pieces of text between quotation marks.
3. Insert the variables into their places.
4. Use `<<` to concatenate text and variables.

Example:
```
cout << "The area of the rectangle is " << t << " sq. m, perimeter is " << k << " m.";
```

For final exams, make sure the output matches the required pattern exactly, with correct spacing, commas, colons, line breaks, etc. If no pattern is provided, use your best judgment.

---

## Input data into variables

Data can be entered from the keyboard into variables during program execution. The input lasts until the Enter key is pressed.

The simplest example:
- Let’s say we ask the user to enter a string into a variable named `sz`.

| Sentence form    | C#                                 | C++                         |
|------------------|------------------------------------|-----------------------------|
| Input: sz        | string sz; sz = Console.ReadLine();| string sz; cin >> sz;       |

### In C#:
It gets trickier when we want to input a number. The `ReadLine` method only reads strings. Although strings can contain numbers, the program cannot treat them as numbers without conversion.  

The input string needs to be converted into the appropriate number type. This conversion is done using the `Convert.` prefix, followed by the desired type (like `ToInt32` or `ToDouble`).

Examples:
```
int a = Convert.ToInt32(Console.ReadLine());
double b = Convert.ToDouble(Console.ReadLine());
```

---

Here’s the full translation of pages 34–38:

---

### **Page 34**

**C++**

With a single instruction, we can request input for multiple variables; when typing, make sure that they are separated by a single space. For example, if we want to input three values, the following instruction applies:  

```cpp
cin >> a >> b >> c;
```

The types of data can even differ, as the `cin` command will automatically handle the conversion.

Don't forget that the data input instruction only places a blinking cursor on the screen. From this, the user will not know how many values or of what type are expected, or in what format. In a real-life program or during an exam, the input request should always be preceded by a clear message explaining what data is expected and in what form. For example:  
*"Please enter the two sides of the rectangle, separated by spaces."*

---

### **Tasks**

1. Write a greeting program that asks for our name, then prints:  
   *Hello, Your Name.*  
   Instead of *Your Name*, use the previously entered name.

2. Write a program that asks for an integer, then prints:  
   *Test for exercise 2: 13.*  
   Replace *13* with the entered number.

3. Write a program where we declare two string variables called `szo1` and `szo2`, and assign them the values `abba` and `baba`. Then print to the screen:  
   *The word "baba" is an anagram of "abba".*

4. Write a program where we declare four integer variables: `sz1`, `n1`, `sz2`, `n2`, with values `24, 32, 3, 4` respectively. Print the following to the screen:  
   *24/32 = 3/4.*

---

### **Page 35**

## **INTEGERS**

### **Basic Operations**

We can perform basic operations with declared integers according to the table shown.  

Division might need a bit of explanation. With integers, division always results in two values: a quotient (e.g., 7 divided by 3 is 2) and a remainder (1 in this case). The quotient and remainder can be determined with the `div` and `mod` operations respectively.  

Operations can be combined, and we can use parentheses to set the order of operations. For example, to calculate the surface area of a cuboid in C:  

```cpp
fel = 2 * (a * b + b * c + a * c);
```

### **In programming, we use these assignment types:**

| Description                     | In C languages       | In C short form  |
|---------------------------------|----------------------|------------------|
| c := c + 10                     | c = c + 10;         | c += 10;         |
| c := c - 10                     | c = c - 10;         | c -= 10;         |
| c := c * 10                     | c = c * 10;         | c *= 10;         |
| c := c / 10                     | c = c / 10;         | c /= 10;         |

In math, this kind of notation wouldn’t make sense. But in programming, `c = c + 10` means that `c` gets the value of `c` plus 10. This makes sense: `c` had some value before the instruction, and now it’s 10 bigger.

---

### **Page 36**

## **Incrementing and Decrementing**

It often happens that we need to increase or decrease the value of a variable by 1. The first is called **incrementing**, and the second is **decrementing**. These can be done in the standard way or using a short form operator in C-like languages:

| Operation      | Assignment      | Short form in C languages |
|----------------|----------------|---------------------------|
| incrementing   | c = c + 1;     | c++;                      |
| decrementing   | c = c - 1;     | c--;                      |

---

### **Random Numbers**

To model random phenomena in the world, we often generate random numbers using a computer. These might simulate dice throws or lottery number draws.  

Computers generate random numbers from periodic electrical signals. As such, these numbers only *appear* random unless you know exactly where the signal is at that point in time.

---

### **In C#**

First, we need to create (declare) a random object. This object can generate random numbers:

```csharp
static void Main(string[] args)
{
    Random rnd = new Random();
    int a = rnd.Next(1, 91);
    int b = rnd.Next(1, 91);
    Console.WriteLine("{0} {1}", a, b);
    Console.ReadLine();
}
```

The `Random` object (or “machine”) has a `Next` method that generates random numbers between a specified lower (inclusive) and upper (exclusive) limit.

---

### **Page 37**

### **In C++**

In C++, we use the `rand()` function to generate random integers. This function returns a number between 0 and at least 32,767. We need the `<cstdlib>` library for this.

To get numbers in a specific range (for example, between 1 and 90), we use modulo division. For instance:

```cpp
#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
    srand(time(NULL));
    int a = rand();
    int b = rand() % 90 + 1;
    cout << a << " " << b;
}
```

Without the `srand()` line, if you run this program multiple times, you’ll get the same results. The `srand()` function initializes the random number generator based on the current time (from the `<ctime>` library), ensuring different results each time.

---

### **Page 38**

## **Tasks**

1. Write a program to calculate the area and perimeter of a rectangular garden. Ask the user for two integers and display:  
   *The garden’s area is: 2000 square meters. You need to walk 210 meters to go around it.*

2. Write a program that outputs 0 if the input number is even and 1 if odd.  
   Example: input 12 → 0; input 45 → 1.

3. Write a program that outputs the units digit of a two-digit number.  
   Example: input 75 → output 5.

4. Extend the previous program to also output the tens digit.  
   Example: input 75 → tens digit 7.

5. Write a program that outputs the hundreds, tens, and units digits of a three-digit number.  
   Example: input 329 → *units: 9, tens: 2, hundreds: 3.*

6. Write a program that prints:  
   *24/6 = 4*  
   Calculate each number separately; no hardcoding. Each number should be outputted as a standalone variable.

7. Extend the previous program so that it outputs:  
   *24/32 = 3/4*  
   Again, calculate every number separately and output them one by one.

8. Ask the user for a number in a variable called `sz`. Increase this number by 1, 3, 10, and 100, then print each result on a separate line without using helper variables and without shorthand operators.

9. Repeat exercise 8, but this time use decrementing and the shorthand operators.

10. Ask the user for two numbers, `x` and `y`. Increase `x` by `y`, decrease `x` by `y`, and then multiply `x` by `y`. Don’t use helper variables. Use shorthand operators and display each result on a separate line.

11. Simulate rolling a dice twice and display the two results one below the other.

12. Simulate flipping a coin three times (0 for heads, 1 for tails). Display the results one below the other.

---

Let me know if you’d like me to translate more!

Sure! Here's a verbatim (word-for-word) English translation of pages 39–43:

---

## REAL NUMBERS

### Operations

In the case of real numbers, addition, subtraction, and multiplication are done in the same way as with integers.  

The difference is in division, where the `/` operator does not mean integer division with remainder, but division resulting in a real number. The `%` operator is not interpretable. A little confusion may be caused by the fact that the `/` operator can mean two things, so it is worth clarifying the following:  

1. If two integers are divided, the result will still be an integer with remainder, unless we declare the quotient to be real.  
2. If the dividend or the divisor is real, the quotient will be real.  

---

### Mathematical functions

**In the case of C#:** The usual mathematical functions (trigonometric functions, logarithms, exponentiation, etc.) can be found in the Math object.  

**In the case of C++:** The usual mathematical functions (trigonometric functions, logarithms, exponentiation, etc.) can be found in the cmath library, which must be included in the program in advance:  
```cpp
#include <cmath>
```

| Name                               | C# example                         | C++ example                   |
|------------------------------------|------------------------------------|--------------------------------|
| square root                        | c = Math.Sqrt(2.25);               | c = sqrt(2.25);               |
| exponentiation (base: 2, exponent: 3) | a = Math.Pow(2,3);              | a = pow(2,3);                 |
| logarithm (base: 2, number: 8)     | a = Math.Log(8,2);                 | –                              |
| base-10 logarithm                  | a = Math.Log10(100);               | a = log10(100);               |
| rounding down to the smaller integer | a = Math.Floor(2.25);            | a = floor(2.25);              |
| rounding up to the larger integer  | a = Math.Ceiling(2.25);            | a = ceil(2.25);               |
| rounding (2.15 round 2, two decimals: 2.15¹²) | a = Math.Round(2.15,1);    | –                              |
| rounding to the nearest integer    | a = Math.Round(2.25);              | a = round(2.25);              |
| absolute value                     | c = Math.Abs(-2.25);               | a = abs(-2.25);               |
| sine²³ (angle in radians: 3.14/2)  | a = Math.Sin(3.14/2);              | a = sin(3.14/2);              |
| inverse sine²⁴ (arc sine, sin⁻¹x)  | c = Math.Asin(1);                  | a = asin(1);                  |

¹² Unfortunately, 2.25 was rounded to 2.2 for me. Everything else (e.g. 2.15) was rounded well.  
²³ Cosine (cos) and tangent (tan) functions must be used similarly.  
²⁴ Inverse cosine (acos) and inverse tangent (atan) functions must also be used similarly.  

---

## Random real numbers

The method of generating random real numbers is very similar in both languages to generating integers. The difference is only in one line. In the example below, we generate a random number between 0 and 1¹⁵. Numbers differing from this range can be created by transforming numbers in the 0..1 range (e.g., multiplication, addition).  

**In the case of C#:** The NextDouble function of the random object should be used without any parameters.  

**In the case of C++:** We need to make a real number from an integer. We will not go into the understanding of this now, but for completeness’ sake, you can read the solution here:  

**C# version:**
```csharp
Random rnd = new Random();
double c = rnd.NextDouble();
Console.WriteLine("{0}", c);
Console.ReadLine();
```

**C++ version:**
```cpp
srand(time(NULL));
double a = (double)rand() / ((double)RAND_MAX+1);
cout << a;
```

¹⁵ So closed on the left, open on the right interval.  

---

## Displaying precision

In the case of real numbers, the number of decimal places indicates precision. Even though we can calculate a quantity to eight–ten decimal places, due to measured data precision from which we calculate, for example, just a single decimal place, our result will barely be more accurate than one decimal place. While the variable stores the number with eight decimal place precision, we need to ensure that the displayed number has only as many decimal places as necessary.  

The opposite situation may also occur, where fewer displayed digits reduce the accuracy of the result. In such cases, zeros are added to the end of the number to indicate precision. For example, 12 cm³ and 12.0 cm³ differ by a tenth of a cubic centimeter in precision. Similarly, the difference between 11.95 cm³ and 12.4 cm³ is about half a cubic centimeter in quantity.  

---

**In the case of C#:** The `Console.Write` and `Console.WriteLine` commands allow setting the displayed precision according to the example. The number after the letter `N` indicates how many decimal places should appear. If its value is 0, the number is displayed without decimals (17). If its value is greater than the number of digits in the variable (19), zeros are added at the end. If the number of displayed decimal places is smaller than the number of decimal places in the variable (18), rounding occurs. (See the console window image.)  

```csharp
double a = 3.14;
Console.WriteLine("{0:N0}", a);
Console.WriteLine("{0:N1}", a);
Console.WriteLine("{0:N3}", a);
```
¹⁶ The value of the variable does not change.  
¹⁷ The value of the variable does not change.  

---

**In the case of C++:** The combined use of `fixed` and `setprecision` commands allows achieving the proper precision display according to the example. The fixed command needs to be given only once in the program because it remains in effect. The `setprecision` parameter sets the number of decimal places to display. If its value is 0, the display occurs with integer precision (8). If its value is greater than the number of digits in the variable (10), zeros are added at the end. If the number of displayed decimal places is smaller than the number of decimal places in the variable (9), rounding occurs. (See the console window image.) For using `fixed` and `setprecision`, the iomanip library must be included:  

```cpp
#include <iomanip>
double a = 3.14;
cout << fixed << setprecision(0) << a << endl;
cout << setprecision(1) << a << endl;
cout << setprecision(3) << a << endl;
```

---

### Tasks

1. Ask the user for three real numbers, calculate their average, and display the result with two decimal places. (Do not round!)  
2. Ask the user for the two legs of a right-angled triangle (a, b are real numbers). Calculate the hypotenuse (c), and display the result with one decimal place precision. (Do not round!)  
³⁸ Use the a² + b² = c² formula. (Pythagorean theorem)  
3. Solve some problem that can be described with a mathematical formula (mathematics, physics, chemistry, professional knowledge, compound interest, etc.). Choose problems without "complications," for example, simple sample selection. Display the result with the appropriate precision that matches the assumed measurement accuracy.  

---

## ARRAYS

If we need many variables (e.g., 100), it would take quite a long time to give each one its own name. It is also a problem to remember the names and later refer to them. The solution is that we give one name to many variables and number them. These will be the arrays. Arrays are basically variables with a name and an index. We refer to array variables by their name and index. For example: `month(2)`.  

We can imagine arrays like a drawer cabinet (see figure). We give the cabinet a name (for example month), and number its drawers. The contents of the drawers are the values stored in the variables.  

The index of an array element is called an index (sometimes array index).  
We can consider an array as a numbered list, which has a name: for example, the list month, with element 0 being January, element 1 being February, etc.  

In C languages, arrays have types just like simple variables, and they must be declared. Compared to traditional declarations, the only difference is that when creating them, we refer to the array nature by using square brackets, and generally (but not always) we can give the planned number of elements.  

The value of an array variable can be given, changed, and read in the same way as simple variables. Usually, it is also possible to specify the number of elements at the time of declaration.  

---

You're right! Here's the verbatim translation of page 43 as well:

---

## One-dimensional array  

If we refer to an array element using a single index, we are talking about a one-dimensional array; otherwise, it is called a vector. The elements of the array can be easily listed in a row (or column). In the drawer model, imagining a single-row drawer cabinet (see the previous figure).  

Turning to coding, we need to know that in C-like languages, array indexing always starts from zero, so the last array index of a 6-element array is 5, not 6. Often, mistakes occur in array usage when a value larger than the maximum possible index is given. In such cases, the program will not work, and we get an error message: array overflow.  

It is also important to know that instead of round brackets, we must use square brackets. In other languages (Basic, Pascal), round brackets are used, and this habit remained in the sentence structure descriptions.  

- In line 1, we declare an integer array of type int with 30 elements, without initial values.  
- In line 2, we declare the last element of the array, its value will be 0.  
- In line 3, we can see an example of how to declare an array with initial values. (The placeholders for the 12 months; line 3. The values can be changed later.)  
- In line 4, we print the first element of the `honap` (month) array, which is at index 0.  
- In line 5, we print the last element of the `szuletes` (birth) array, which is at index 29 (not 30, because the indexing goes from 0 to 29). The printed value is 0.  
- In line 6, we see an example where the index of one array (month) can be the element of another array (szuletes). (This does not mean arrays within arrays; that is a different case.) The printed element is: January.  

### C# version:  
```csharp
1) int[] szuletes = new int[30];
2) szuletes[29] = 0;
3) string[] honap = new string[3] { "januar", "februar", "marcius" };
4) Console.WriteLine(honap[0]);
5) Console.WriteLine(szuletes[29]);
6) Console.WriteLine(honap[szuletes[29]]);
```

### C++ version:  
```cpp
1) int szuletes[30];
2) szuletes[29] = 0;
3) string honap[3] = { "januar", "februar", "marcius" };
4) cout << honap[0] << endl;
5) cout << szuletes[29] << endl;
6) cout << honap[szuletes[29]];
```

---

¹⁹ A vector in the plane is characterized by 2, in space by 3 coordinates, with numbers written next to each other. In N-dimensional space, a vector is described by N coordinates, i.e., by numbers written next to each other. This is where the term "vector" comes from.

---

Here is the verbatim translation of page 44:

---

## Two-dimensional array  

If our data is table-structured, i.e., like a multi-column and multi-row drawer cabinet, we use two-dimensional arrays, also known as matrices, for storage. For example, a matrix²⁰ can represent a timetable, the pixels on a screen, or any arrangement requiring multiple rows and columns.  

- In line 1, we declare an integer array with 100 rows and 50 columns, without assigning initial values to the elements.  
- In line 2, we assign the value 62 to the last column (index 49) of the first row (index 0) of the previously declared array.  
- Lines 3–5 contain a single instruction, broken into multiple lines for clarity. Here we can see an example of how to assign initial values when declaring an array. Note that each row’s elements are enclosed in curly braces, and values within a row are separated by commas. Rows are also separated by commas, and the entire matrix is enclosed in one large pair of braces. This matrix could, for instance, represent a 3x3 tic-tac-toe board. For example, 0 represents an empty square, 1 the circle, and 2 the X figure.  

- For displaying the figures, we use a character-type array created in line 6 with 3 elements, whose values are also given (the dot represents the empty space).  
- In line 7, we print the element found in the first row’s last column of the array `kep`; this value is 62.  
- In line 8, we print the value in row 2 (everyday sense: 3rd row) and column 1 (everyday sense: 2nd column) of the array `tabla`; this value is 2.  
- In line 9, we see an example where an index of one array (`tabla`) can be used to reference an element from another array (`figura`). The printed element: X.  

---

### C# version:  
```csharp
1) int[,] kep = new int[100, 50];
2) kep[0, 49] = 62;
3) int[,] tabla = new int[3, 3] { {0, 1, 2}, 
4)                                {1, 0, 2}, 
5)                                {0, 2, 1} };
6) char[] figura = new char[3] { '.', 'o', 'X' };
7) Console.WriteLine(kep[0, 49]);
8) Console.WriteLine(tabla[2, 1]);
9) Console.WriteLine(figura[tabla[2, 1]]);
```

---

### C++ version:  
```cpp
1) int kep[100][50];
2) kep[0][49] = 62;
3) int tabla[3][3] = { {0, 1, 2}, 
4)                     {1, 0, 2}, 
5)                     {0, 2, 1} };
6) char figura[3] = { '.', 'o', 'X' };
7) cout << kep[0][49] << endl;
8) cout << tabla[2][1] << endl;
9) cout << figura[tabla[2][1]];
```

---

²⁰ The word matrix simply means: a collection of data arranged in a table format.

---


Here is the verbatim translation of page 45:

---

## Associative array  

In the case of associative arrays, the role of the index is taken over by the key. The key does not necessarily have to be a number type. Depending on the implementation in different languages, the key can be a single character, a string, or any data type.  

The associative array is essentially a complex object. Just think about how it would be possible to print all the elements of such an array or sort them if various data types were allowed. These questions go beyond the scope of this book. On a basic level, however, I still consider it useful to get familiar with associative arrays because knowing them can greatly shorten the solution of tasks in high school exams and other cases.  

**In C#:** associative arrays can be implemented with the help of a hashtable, which can be found in the `System.Collections` namespace (line 1). Both the key and the value type can be arbitrary, but a practical solution is to use strings. (Sometimes, we still have to convert the read-out values to numbers for further calculations. In the example, we did this by type conversion ("casting") in line 8.)  

**In C++:** we will use the `map` object, and for this, we need to include the map library (line 1). We must specify the data types of both the key and value (lines 2 and 4), so no conversion will be needed later due to the nature of associative arrays. Unfortunately, older versions of the language do not support initialization at the point of declaration, so data loading must always be done afterward (lines 5–7).  

The following program will output:  
```
1
20
```

---

### C# version:  
```csharp
1. using System.Collections;
...
2. Hashtable rangsor = new Hashtable();
3. rangsor["Lajos"] = 1;
4. Hashtable bsz = new Hashtable() { {'A', 0}, 
5.                                   {'B', 1}, 
6.                                   {'C', 2} };
7. Console.WriteLine(rangsor["Lajos"]);
8. Console.WriteLine((int)bsz['C'] * 10);
```

---

### C++ version:  
```cpp
1. #include <map>
...
2. map <string, int> rangsor;
3. rangsor["Lajos"] = 1;
4. map <char, int> bsz;
5. bsz['A'] = 0;
6. bsz['B'] = 1;
7. bsz['C'] = 2;
8. cout << rangsor["Lajos"] << endl;
9. cout << bsz['C'] * 10;
```

---

Here is the verbatim translation of page 46:

---

## Tasks  

Tasks marked with * must be solved using associative arrays.

1. Let’s use an array to store the names of the days of the week. The names should be stored in order (Monday, Tuesday, ...).  
   a. Declare the array.  
   b. Fill it with the appropriate values.  
   c. Print the name of the day with index 0!  
   d. Print the name of the third day of the week! (In everyday life, we do not use 0 as the first day, Monday is the first day of the week for us.)  
   e. Print Saturday’s name using the array!  
   f. Ask the user for a number from 1 to 7, and based on that, display the name of the corresponding day of the week!  

2. We want to store which student gave a gift to whom at the class Christmas event. For this, let’s declare an array where the index indicates the gift giver and the value shows the recipient.  
   a. Declare the appropriate array.  
   b. Fill the array with data, for example, the 0th student gave a gift to the 6th student:  
      0 → 6, 1 → 5, 2 → 8, 3 → 7, 4 → 10, 5 → 3, 6 → 1, 7 → 2, 8 → 0, 9 → 4, 10 → 9.  
   c. Print out using the array to whom the 7th student gave a gift, in the format:  
      Student 0 gave a gift to student 6.  
   d. Who gave a gift to the student who received a gift from student 7? Print this number on the screen. Do not use an auxiliary variable to solve the task.  
   e. The 3rd and 4th students swapped the people they gave gifts to. Perform the necessary modifications on the vector. Do not change the initial values. The swap should work for arbitrary giver-receiver relationships, not only for the current example. (We can use an external auxiliary variable outside the array. Another help: there should be uniformly sized tags with different labels — e.g., cups for Apa and Kati — and they should be filled with data. If Kati’s cup was accidentally placed in Apa’s cup position, how would we swap the drinks in the cups? Use an auxiliary cup. First pour Apa’s cola into the auxiliary cup. Then pour the drink from Kati’s cup into Apa’s cup. Finally, pour the auxiliary cup into Kati’s cup. The same should be done with variables as well. An auxiliary variable is needed, etc.)  
   f. Let’s name the students using an array, declare the array:  
      0 – András, 1 – Béla, 2 – Cecília, 3 – Dóra, 4 – Elemér, 5 – Fanni, 6 – Glória, 7 – Hedvig, 8 – Ilona, 9 – József, 10 – Katalin.  

---

Here is the verbatim translation of page 47:

---

g. Ask for a number between 0 and 10, and display with names who gave a gift to the student with the entered number, in the following format:  
*Géza gave a gift to Réka.*  
Do not use an auxiliary variable.

h. Ask for a number between 0 and 10, and display with names, in a chain form, who gave a gift to whom, ending with the student who gave a gift to the entered number.  
For example:  
*Géza → Réka → Béla.*

---

3. Store our class schedule in a two-dimensional array. The first index indicates the lesson number (it can be the 0th lesson), the second index the day number. The array elements will be the subject names (e.g., mathematics).  
   a. Declare the array.  
   b. Assign values. (It can be an imaginary timetable so it doesn’t take too much time.)  
   c. What lesson do we have on Wednesday in the 3rd period? Display the subject name on the screen.  
   d. Ask for a day number and a lesson number. Display on the screen what lesson we have then, in the following format:  
      *Wednesday 6th period: physical education.*  
      (Use the array created in task 1.)  
   e. Swap Monday’s 4th lesson with Wednesday’s 3rd lesson. The swap should work for arbitrary subjects, not just the current examples. (An auxiliary variable outside the array can be used.)

---

4. We want to store the position of pieces on a chessboard (setup) in a two-dimensional array.  
The numbers representing white pieces: pawn – 1, knight – 2, bishop – 3, rook – 4, queen – 5, king – 6.  
The numbers representing black pieces: pawn – 7, knight – 8, bishop – 9, rook – 10, queen – 11, king – 12.  
0 indicates an empty square.  
   a. Declare the appropriate array.  
   b. Fill it with meaningful data.  
   c. Display on the screen what figure is in row 2, column 3.  
   d. Ask for a row and column number (1..8). Display on the screen what figure is standing there.  
   e. Ask for a row and column number (1..8). Display on the screen what figure is standing there. When printing, use the initial letter of the piece. White pieces in uppercase, black pieces in lowercase letters (for example, white queen: Q, black king: k).  
   f. *Ask for a position provided in standard notation (e.g., B7). Display on the screen which figure is standing on that square. The figures should be indicated with their initial letters. White pieces uppercase, black pieces lowercase letters (e.g., white queen: Q, black king: k). If we have not yet learned about strings, you can use separate inputs for the letter and the number.*

---

5. *Write a program that asks for a two-digit hexadecimal number (in base 16), and converts it to a base-10 number and displays the result. If we have not yet learned about strings, ask separately for the two digits.*

---

Here is the verbatim translation of page 48:

---

# CHARACTERS

A character contains a single letter, digit, punctuation mark, graphic symbol (for example, a smiley face), or control character (for example, carriage return to the beginning of the line).

The simplest data type is `char`, which stores the character’s code in a single byte, called the ASCII code.  
The capital letters of the English alphabet start from 65 (the ASCII code of ‘A’ is 65, ‘B’ is 66, etc.),  
the lowercase letters start from 97 (the ASCII code of ‘a’ is 97, ‘b’ is 98, etc.),  
digits start from 48 (the ASCII code of ‘0’ is 48, ‘1’ is 49, and so forth).  

More complex data types (e.g., `wchar`) store the character code in multiple bytes, thus capable of storing multiple types of symbols.

---

## CHARACTER STRINGS

### Definition

A character string (`string`) can be considered a special one-dimensional character array.  
Accordingly, each character can be referenced by the name of the string and the index of the letter.  
For example, store the name "András" in a string named `nev`. In this case, `nev(2)` will have the value of the letter ‘d’.  
Indexing starts from 0.

A character string is a special character array because it contains an end-of-string marker, represented by `\0`.  
With this, we can determine in functions where the end of the string is.

Any character in the string can be accessed in this way. For example: `Ki: nev(2)`.

However, while C++ allows modifying individual characters of a character string (changing their value), in C#, this is not permitted; you can only assign a new value to the entire character string (line 4).  
For example, the desired effect in line 4 is achieved by replacing the 3rd character (at index 2) of the string.

**Example:**
```csharp
1) string str = "isz";
2) string nb = "";
3) nb = "h" + str + "ed"; // becomes "hiszed"
4) str[2] = 'i';
```

---

Here is the verbatim translation of page 49:

---

Apart from line (4), everything else works the same way in both languages.  
An empty character string can be created in the manner shown in line (2).  

Character strings can be **concatenated** using the `+` operator (line 3). The result of the operation is a character string that contains the original character strings in left-to-right order.  
In the `str` variable, the character string "isz" is stored, so:  
`hb = "h" + "isz" + "ed"` = "hiszed".  

This concatenation of text strings is also called concatenation in technical language.  

---

## Basic operations  

To use the following functions in C++, the string library needs to be included²¹:  
```cpp
#include <string>
```

---

### Length of a character string  

With the help of the **Length** property (in C#) or function²² (in C++), we can determine how many characters are in our string.  
This is a commonly used operation, especially if we want to examine characters one after another in a loop and need to know how many times the loop should run. In the example, `str` is the name of the character string, and its length is stored in the variable `hossz`.  
Let’s not forget that, for example, if the length of the character string is 3, the indexes of the stored characters go from 0 to 2 (and not to 3).

| C# version                              | C++ version                                   |
|-----------------------------------------|----------------------------------------------|
| `int hossz = str.Length;` → 3           | `int hossz = str.length();` → 3              |

---

²¹ C++ can handle several types of character strings. These libraries are not compatible with each other, but character strings can be converted between them. Another frequently mentioned library is `cstring`, which was commonly used with basic C. For example, when programming for Windows at a basic level, that kind of character string would need to be used.  

²² A function is a command to which we provide one or more pieces of data, and from that, it creates another piece of data. Essentially, it works the same way as Excel functions. A more detailed explanation can be found in the chapter on functions.

---

Let me know when you're ready for page 50!

Here is the verbatim translation of pages 50 and 51:

---

## Copying part of a character string  

We can copy a part of a character string using the **Substring** function in C# or **substr** in C++. In both functions, the first parameter is the starting position of the copy (index), and the second parameter is the number of characters to copy. The starting position is an array index.  
Character indexing starts from 0 (not from 1). The second parameter is not an index but a count of characters. For example, if we want to copy 3 consecutive characters, we need to specify 3 as the parameter.  
In the example, the `str` character string contains the word "pisze". Copying starts from the character at index 1, that is, from the letter 'i'. Three characters will be copied, resulting in "isz", which will be stored in the `hb` variable.  

**C# version:**
```csharp
str = "pisze";
hb = str.Substring(1, 3);
```

**C++ version:**
```cpp
str = "pisze";
hb = str.substr(1, 3);
```

---

## Deleting part of a character string  

We can delete characters from character strings using the **Remove** function in C# or **erase** in C++. The first parameter is the starting position of the deletion (index), and the second parameter is the number of characters to delete. The starting position is an array index. The second parameter is the number of characters (not an index).  
In the example, the `hb` variable contains the word "hiszed". The deletion starts at index 0, that is, from the letter 'h'. One character is deleted, leaving the string "iszed", which is stored in the `hb` variable.  

**C# version:**
```csharp
str = "hiszed";
hb = str.Remove(0, 1);
```
→ iszed

**C++ version:**
```cpp
str = "hiszed";
hb = str.erase(0, 1);
```
→ iszed

---

## Inserting into a character string  

We can insert a character string into any position in another character string using the **Insert** function. Insertion means that the characters located at and after the given position shift to the right, and the inserted characters take their place.  
The first parameter of the Insert function is the starting position of the insertion, given as an index starting from 0. The second parameter is the character string to insert.  
In other words, the character string provided as the second parameter will be inserted before the character at the position specified by the first parameter. In the example, into the `hb` character string, which originally contains the string "iszed", we insert the letter 'v' at the beginning. This shifts the string by one character, and 'v' takes the empty place. (More characters could have been inserted instead of just one letter.)  

**C# version:**
```csharp
hb = "iszed";
str = hb.Insert(0, "v");
```
→ viszed

**C++ version:**
```cpp
hb = "iszed";
str = hb.insert(0, "v");
```
→ viszed

---

## Tasks  

1. Ask for a word and display its length.  
2. Ask for a word and display its first letter.  
3. Ask for a word and display its last letter.  
4. Ask for a five-letter word and display its middle three letters.  
5. Ask for a Budapest postal code and display which district it belongs to. (The middle two digits of the postal code give the district number.)  
6. Create a character string containing the word "leszel".  
   a. Change the first letter to 'L'.  
   b. Change the last letter to 'k'.  
   c. Delete the first and last letters.  
   d. Add the letter 'm' at the end.  
7. Ask the user for their surname and given name, store them in two separate variables. Concatenate the surname’s first letter and the full given name. Display it in this format: (example: Bodor Elek → BElek)  
8. Ask the user for their surname and given name, store them in two separate variables. Concatenate the first three letters of the surname and the first three letters of the given name, then add "01" at the end to form a username. (example: Kiss Ferenc → KisFer01)  

---

Here is the verbatim translation of page 52:

---

## RECORDS  

### Definition  

In a record, we store closely related data. For example, the data of a car: license plate number, year of manufacture, brand, color, or a person’s data: name, date of birth, number of children.  

**A record is therefore a composite data type consisting of elementary data elements not necessarily of the same type.**  

The record data type should therefore be viewed as a template based on which variables can later be created. The record type itself is not suitable for storing data. After creating the type, variables will be created based on that type, which will be able to store data.  

In the example, we store common operations between fractions in one record (lines 1–4). The parts of the record are called fields. With this naming, we refer to the fact that larger parts of a table are fields, and they themselves are not standalone data types. Any operation between two fractions requires the two fractions' numerators and denominators (szaml1, nev1, szaml2, nev2). These are integer-type fields (line 2). The operation between them is stored in the field `muvjel`, which is a character type field (line 3).  

After defining the type, we can declare concrete variables that are suitable for storing data (line 5). In the example, the variable names are `atm` and `buff`.  

We refer to the record fields by writing the variable name and then the field name separated by a dot. In line (6), for example, we assign the value 30 to the `szaml1` field of the `buff` variable. In line (7), we print this value to the screen.  

The real advantage of using records is shown by line (9). We can copy the entire content of one record to another record with a single command. We do not need to transfer the values field by field. In the example, the content of the record `buff` is transferred to the record `atm`. The value in the `buff.szaml1` field is copied into `atm.szaml1`, the value in `buff.nev1` is copied into `atm.nev1`, and so on. This type of data transfer between records is only possible between records of the same type.  

Arrays of record types can also be created, where even table-structured data can be stored with each column corresponding to a field of the record. (This is different from two-dimensional arrays.)

---

Here is the verbatim translation of page 53:

---

## Coding  

In C-like languages, the record type is declared with the keyword **struct**. Below, we can see examples of its use.

**In C#:**  
The records (struct) must be created before the **namespace**, and the fields’ types must be written with the **public** keyword. Record-type variables, however, can only be created after the **namespace** keyword.

**In C++:**  
Records (struct) can be created either in the main program (main) or in other locations appearing later. No additional keyword entry is required.

---

### C# version:
```csharp
1) Using System.Threading.Tasks;
2) struct tortek {
3) public int szaml1;
4) public int nev1;
5) public int szaml2;
6) public int nev2;
7) public char muvjel;
8) }
9) namespace ConsoleApplication1
```

---

### C++ version:
```cpp
1) struct tortek {
2) int szaml1;
3) int nev1;
4) int szaml2;
5) int nev2;
6) char muvjel;
7) };
```

---

We can create variables with the appropriate structure of the declared records (struct) and then use them in various operations.

Based on the previously declared record `tortek`, we create a three-element array variable of that record type (line 3).

In line (4), we can see how to assign values to each field separately. In line (5), there’s an example of printing values to the console.  
In line (7), data is transferred between records of the same type, assigning values field by field in order (for example, `szaml1` to `szaml1`, etc.).

---

### C# version:
```csharp
1) static void Main(string[] args)
2) {
3) tortek[] tort = new tortek[3];
4) tort[1].szaml2 = 8;
5) Console.Write(tort[1].nev1);
6) tort[1].szaml1 = tort[1].szaml2;
7) tort[2] = tort[1];
```

---

### C++ version:
```cpp
1) tortek tort[3];
2) tort[1].szaml2 = 8;
3) cout << tort[1].szaml2;
4) tort[1].szaml1 = tort[1].szaml2;
5) tort[1] = tort[2];
```

---

Here is the verbatim translation of page 54:

---

## Tasks  

### 1. Plots  
a. Create a record type named *telek* for storing the following data: 21 15 50.  
   The field names should be: *hasszam* (width), *szeles* (length), *hossz* (depth)!  
b. Create a variable named *buff* of type *telek*.  
c. Create an array named *telkek* of type *telek* with 50 elements.  
d. Assign to the *buff* variable the values provided in part (a).  
e. Assign the contents of the *buff* variable to the 10th element of the *telkek* array.  
f. Calculate the area of the plot based on the *buff* variable and display it in the following format:  
   *The area of plot number 21 is 750 square meters.*  
g. Increase the width of the plot stored in the *buff* variable by 10 meters, and decrease the length by 10 meters.

---

### 2. Fraction operations  
a. Create a record type for storing the following data under the name *tmuve* : 8 20 8 30 *.  
   The field names in order should be: *sz1*, *n1*, *sz2*, *n2*, *jel*!  
b. Create a variable named *atm* of type *tmuve*.  
c. Create an array named *tmuvel* of type *tmuve* with 100 elements.  
d. Assign the values from part (a) to the 0th element of the *tmuvel* array.  
e. Assign the 0th element of *tmuvel* to the *atm* variable.  
f. Perform the designated operation from part (a) using the 0th element of the *tmuvel* array.  
   The multiplication symbol does not need to be extracted from a variable. The final output should be:  
   *8/20 * 8/30 = 64/600.*  

---

### 3. Elevator requests  
Store elevator requests in records. One request consists of six numbers:  
- The first three numbers specify the time (hour, minute, second),  
- the fourth the group number,  
- the fifth the departure floor,  
- the sixth the destination floor.  
Example: *9 7 11 7 6 22*  

a. Create a record type for storing this data. Choose record and field names logically.  
b. Create a data structure capable of storing up to 120 elevator requests. Choose the name logically.  
c. Create a variable named *buff* for temporarily storing one elevator request.  
d. Fill two elements of the array with arbitrary data.  
e. Increase the departure floor field of one record by 1, decrease the same field in another by 1.  
f. Swap two records in the array using the *buff* variable.  
g. Display the contents of the filled records on the screen.

---

Here is the verbatim translation of page 55:

---

## TYPE CONVERSION  

### Definition  

We can perform operations on data of different types.  

For example, let’s say we have the numerator and denominator of a common fraction. How many whole units does it contain, and what is its value in decimal form? The first question can be most simply answered by integer division (line 18), so both the numerator and the denominator should be stored as integers (int) (lines 16–17).  
To determine the decimal fraction value, we must convert at least one of the variables to a floating-point number. This operation is generally called type conversion or typecasting.  

---

### C# version:
```csharp
16 int szam = 3;
17 int nev = 4;
18 Console.WriteLine(szam / nev);
19 double n = nev;
20 Console.WriteLine(szam / n);
21 Console.WriteLine(szam / (double)nev);
```

---

### C++ version:
```cpp
16 int szam = 3;
17 int nev = 4;
18 cout << szam / nev << endl;
19 double n = nev;
20 cout << szam / n << endl;
21 cout << szam / (double)nev;
```

---

### Automatic type conversion and explicit casting  

The conversion happens automatically (line 19) if we assign a value of one type to a variable of another type. In this case, we assign an integer value to a floating-point variable. After this, we can perform division and print the result (line 20).  

Often, however, we don’t want to create a separate variable just for this purpose. In that case, we can force type conversion. To do this, we only need to write, in parentheses before the value to be converted, the type we want to convert it into (line 21).  

Both automatic and forced type conversions can lead to data loss when we convert a variable with a wider interpretation into a narrower one.  
For example, if we convert a floating-point number to an integer, the fractional part will be lost.  

It is also useful to know that a character stored in a `char` type variable can be converted to its ASCII code number.  
For example, if we convert the character '0', we will get the value 48, since 48 is the ASCII code for '0'. If we convert it back to a character, it will become '0' again.  

Thus, if we want to convert numbers into characters for display, we need to add 48 to the number. Similarly, if we want to convert a character into the corresponding number, we need to subtract 48.

---


Here is the verbatim translation of page 56:

---

The above-described procedures work flawlessly for simple data types.  
For complex data types, type conversion rarely succeeds.  
For example, converting a number to a character string and then converting it back is not possible with simple casting.  
For this purpose, we need special instructions or custom methods.

---

### Converting between character strings and numbers  

It often happens that we have a number in the form of a character string (for example, read from a file or entered in a text field of a Windows application), but we need to perform some calculation with it. In such cases, we need to convert it into a numeric data type — in technical terms, we must convert it.  

In the provided sample code, we get the value 37 into a variable named `str` of type character string, which we then increase by 10 and display:  
(C#: 5 - 8, C++: 8 - 13)

The opposite can also happen: for example, we may want to embed the result of a calculation into a character string, because we want to display it in a Windows application’s text field.  
In such cases, we convert the number into a character string.  
In the provided example code, we have the number 81 stored as an integer, and then convert and display it as text. (C#: lines 1 - 4, C++: lines 1 - 7)

---
At the bottom of page 56, the text continues with the heading **"C#"**, introducing how conversions are handled in C#:  

---

**C#**  

In C#, there are built-in functions for conversion, starting with **Convert**, and after that, we simply specify what type we want to convert into (e.g., **ToInt16**, **ToString**). In parentheses, we provide the variable (or value) we want to convert.  

In the given example, we use **Convert.ToDouble** or **Convert.ToSingle** similarly, if we want to convert to floating-point numbers.  
**Convert.ToString** can convert even decimal fractions into a character string.  

The example’s brief explanation:  
1. We create an integer variable named *egesz*, and assign the value 81 to it.  
2. We create a string variable named *str*.  
3. We convert the value of *egesz* into a character string and load it into *str*.  
4. Now that it’s a string ("81"), we concatenate text to it (something like " there are db canaries in the cage"). (Without conversion, we couldn’t have done this.)  
5. We display the full string on the screen.  
6. We assign the string "37" to *str*.  
7. We convert the text in *str* into an integer and store it in *egesz*.  
8. We add 10 to the now-integer number. (Without conversion, this wouldn’t be possible.)  
9. We print the result to the screen.

---

Here is the verbatim translation of page 57:

---

## C++

In C++, there are several ways to perform conversions, depending on the version and the available libraries. From these, I selected the older, generally functioning and also practical method, which is conversion using **stringstream**.

To use a **stringstream**, we need to include the appropriate library:  
```cpp
#include <sstream>
```

By including this library, we gain access to a variable type that behaves like a stream. We can direct data into it and extract data from it using the `>>` and `<<` operators, similarly to how we have already used `cin` and `cout`. The only difference is that instead of writing to the screen or reading from it, these commands will operate on the name of the **stringstream** variable.  

As we have seen, with **iostream** data type conversions occur automatically.  
Since **stringstream** works in the same way, conversions happen as follows:  

1. The content of the variable to be converted is redirected into a **stringstream** type variable (lines 4 and 10).  
2. The content of the **stringstream** variable is then redirected into the target variable, converting its format (lines 5 and 11).  

If we direct multiple pieces of data one after another into a **stringstream** variable, they will be written sequentially.  
The value of the variable expands with the newly entered data, just like when printing to the screen.  
If we want to reuse such a variable multiple times, we will need to clear its contents.  
The **clear** function serves this purpose (line 9).  

---

**Example (C++):**
```cpp
1) int egesz = 81;
2) string str;
3) stringstream konv;
4) konv << egesz;
5) konv >> str;
6) str += " db kanari van a kalitkaban.";
7) cout << str << endl;
8) str = "37";
9) konv.clear();
10) konv << str;
11) konv >> egesz;
12) egesz += 10;
13) cout << egesz;
```

---
Here is the verbatim translation of page 58:

---

The example’s brief analysis:  

1. We create an integer variable named *egesz* and assign it the value 81.  
2. We create a string variable named *str*.  
3. We create a variable named *konv* of type **stringstream** for conversion.  
4. We load the value of *egesz* into the *konv* stream.  
5. We redirect the content of the *konv* stream into the *str* variable, converting it into a character string.  
6. We now append text to the string "81" (this wouldn’t have been possible without conversion).  
7. We print the complete character string to the screen.  
8. We load the *str* variable with the value "37".  
9. We clear the stream’s content so the previously loaded data doesn’t interfere with the new conversion.  
10. We load the value from the *str* variable into the *konv* stream.  
11. We redirect the content of the *konv* stream into the *egesz* variable, converting it back into an integer.  
12. We add 10 to the now integer value (this wouldn’t have been possible without conversion).  
13. We print the result to the screen.  

---

## Tasks

1. Ask the user to input the numerator and denominator of a common fraction. Print the fraction in its original form, first as a mixed number, then as a decimal fraction. Do not use auxiliary variables. (Example: 7/4 = 1 whole and 3/4 = 1.75.)  
2. Without using arrays, write a program that asks for a number between 10 and 15, and converts it into the corresponding hexadecimal digit (A..F).  
3. Without using arrays, write a program that asks for a character between 'a' and 'f', and converts it into a number between 10 and 15.  
4. The first two characters of a character string form a two-digit number. The remaining characters represent a unit of measure and description. The number and unit of measure should not be separated by a space in C++. (Example: "35db alma" — 35 pieces of apples.) Ask the user for such a character string, then sum the two-digit numbers and print the result on the screen.  
5. Without using arrays, write a program that prints the alphabet in random order, with uppercase and lowercase letters.

---

Here’s the full translation of the text in the image:

---

## FREQUENTLY ASKED QUESTIONS

**Is it possible to create three-dimensional or multi-dimensional arrays?**  
Yes, these can be declared and used similarly to two-dimensional arrays.

**Can a record contain another record as an element, i.e., can records be nested?**  
Yes. Care must be taken to declare the embedded record first.

---

## SUMMARY

### Classification of data by complexity:

| Simple          | Complex                                                                 |
|-----------------|------------------------------------------------------------------------|
| - Variables     | - Arrays – vectors, matrices, character strings, associative arrays   |
| - Constants     | - Records – record, record-containing array                           |
|                 | - Files                                                                |

---

### Classification of data by mutability:

| Mutability       | Constant                                             | Variable                         |
|------------------|------------------------------------------------------|----------------------------------|
| Modifiability    | Cannot be modified from the program.                 | Can be modified from the program.|
| Declaration      | `const int vf = 1280;`                               | `int db = 0;`                   |

---

### Simple data types:

| What is stored?    | Variable type (example) | Storage method          | Operations                                                              |
|--------------------|-------------------------|-------------------------|-------------------------------------------------------------------------|
| Integer number     | int                     | two's complement        | addition, subtraction, multiplication, division with remainder          |
| Real number        | double                  | floating-point          | addition, subtraction, multiplication, real division, mathematical functions (e.g., square root) |
| Logical value      | bool                    | bit                     | and, not, or                                                           |
| Character          | char                    | ASCII code              |                                                                         |

---

> *26 I have seen classifications where arrays (including character strings) are placed among simple data types. Before an oral exam, it’s worth clarifying with the examiner which classification they expect to hear or read.*

---

Here is the full translation of the text from the image:  

---



## Arrays

Variables provided with an index (numbered).  

| Name         | Usage                    | Value Assignment     | Declaration                                          |
|--------------|--------------------------|----------------------|------------------------------------------------------|
| vector       | data in a single line    | a[5] = 1;            | C#: int[] a = new int[9]; <br> C++: int a[9];        |
| matrix       | table                    | C#: b[5,3] = 2; <br> C++: b[3][5] = 2; | C#: int[,] a = new int[5,3]; <br> C++: int b[3][5]; |
| associative  | key-value pairs          | h[‘C’] = 3;          | C#: Hashtable h = new Hashtable(); <br> C++: map<char, int> h; |

---

## Strings

Character arrays terminated with an end character.  

| Operation          | Example                           | Result            |
|-------------------|-----------------------------------|-------------------|
| Concatenation     | s = "Ez" + "az!";                 | "Ezaz!"           |
| Modify character  | C#: Delete (Remove) + Insert (Insert) <br> C++: s[0] = 'A'; | "Az az!"          |
| Length            | C#: i = s.Length; <br> C++: i = s.length(); | 6                 |
| Copy substring    | C#: k = s.Substring(1,3); <br> C++: k = s.substr(1,3); | "z a"             |
| Delete            | C#: k = s.Remove(1,3); <br> C++: k = s.erase(1,3); | "Ez!"             |
| Insert            | C#: k = s.Insert(3, "meg "); <br> C++: k = s.insert(3, "meg "); | "Ez meg az!"      |
| Contains?         | C#: b = s.Contains("fa"); <br> C++: i = s.find("fa"); | C#: false <br> C++: string::npos |

---

Here is the full translation of the text from the image:  

---

## Records

Tightly related data that does not necessarily have to be of the same type, handled together.  

| Steps of Usage            | C++ example                                                   | C# example                                                    |
|---------------------------|---------------------------------------------------------------|----------------------------------------------------------------|
| 1. Creating a record type | ```struct auto { string rsz; int evjarat; bool elso; };```    | ```using... struct auto { public string rsz; public int evjarat; public bool elso; };``` |
| 2. Creating a record      | ```auto enautom, autok[90];```                               | ```auto enautom auto[] autok = new auto[90];```               |
| 3. Value assignment between identical record types | ```enautom = auto[12];```                                | ```enautom = auto[12];```                                     |
| 4. Field-by-field value assignment | ```auto[10].rsz = "ABC-123";```                             | ```auto[10].rsz = "ABC-123";```                               |

---

## Type Conversions

Sometimes data is used in a different data type, allowing different kinds of operations to be performed on it.  
Conversion may result in data loss if converting from a broader interpreted type to a more narrowly interpreted one.  

| Type                    | C# example                                     | C++ example                                          |
|-------------------------|------------------------------------------------|------------------------------------------------------|
| Automatically           | ```egesz = 2.71;```                            |                                                      |
| Type casting            | ```(double)egesz```                            |                                                      |
| With target functions   | ```e = Convert.ToInt32("13");```               |                                                      |
| Using streams           |                                                | ```istringstream("13") >> egesz;```                 |

---




**III. CONTROL STRUCTURES**  

**SEQUENTIAL EXECUTION**  

In programming, the order in which instructions are issued generally matters. If we issue the same instructions in a different order, the program may work differently or may not work at all. For example, the instruction 1. "move forward 5 steps" and 2. "move left 2 steps" can get us to the same position, provided we are in a large, empty space and can switch their order without issues. However, the situation changes if there is a wall one step to the left from our position.  

By using **control structures**, we can decide which instruction should follow which one during the execution of the program. Therefore, it can happen that instructions are not executed in the exact order they appear in the code.  

The execution of instructions in the order they appear in the code, in a step-by-step manner, is called **sequential execution**.  

In our short programs so far, we have followed sequential execution, just without explicitly naming it.  

---

**CONDITIONAL BRANCHING - BASICS**  

*Introduction*  

If, depending on a condition, the program can continue in multiple ways, we use **branching**. Branching structures are also called **selection structures**.  

The condition always has a **logical value**, meaning it is either **true** or **false**. Most of the time, conditions are given in the form of **comparisons**. For example, the condition *a > 0* can clearly determine, in a specific situation, whether it is true or false.  

*27 In mathematical terms: branching is used to create case separation.*  
*28 In mathematical terms: relations.*

Here’s the full translation of the provided text from Hungarian to English:

---

**In a flowchart, conditional branching is represented by a diamond shape with a vertex.**  
Inside the diamond, we write the condition, and on the arrows leaving it, we write the letters i (true) and h (false). This indicates which way the program continues: along the true branch or the false branch.  
**Program branches** can meet again in another place in the flowchart, at a **junction point**. The junction point is marked with a small circle.

---

### One-way branching

We can talk about one-way branching if only a true branch is created in the program.  

The structure of one-way branching can be described in sentence form as follows:  

```
If <condition> then <instructions>  
End of branching
```

**Interpretation:** if the condition is met, then the instructions after "then" are executed. After that, the program continues after the "end of branching".  
If the condition is not met, program execution continues immediately after the "end of branching".  

If there is only one instruction after "then," the "end of branching" can be omitted.  

Let’s consider the following example: calculate the absolute value of a number entered. If the number is not negative, we don't have to do anything, just print it out. Thus, we can define the condition as: `a < 0`.  
The complete algorithm can be seen in the left column below:  

| **The algorithm of the example**               | **Branching coded in C languages**         |
|-----------------------------------------------|-------------------------------------------|
| Input: a                                      | if (a < 0)                                |
| If a < 0 then a := (-1) * a                   | &nbsp;&nbsp;a = (-1) * a;                |
| Output: a                                     |                                           |

**Condition**                    | **Instruction in the true branch**  

---

The above branching coding looks like the right side in all C-like languages. The condition must always be placed between parentheses. The instruction in the true branch (for now, only one instruction) is written after it, separated by a space.  

---

29. The use of the term might sound odd since how can one branch in only one direction? However, in professional literature, this structure is often called this way, since there is no false branch.

 
65
 
 

---

### Branching in Two Directions  

We talk about two-way branching if, depending on one condition, the program needs to continue in two different ways. So we want to use the false branch.  

The syntax:  

```
If <condition> then <instructions1>
  else <instructions2>
End of branching
```  

**Interpretation**: if the condition is met, instructions1 will be executed; otherwise, instructions2 will be executed. After executing the instructions, the program continues after the End of branching.  

**Example**: negative numbers do not have a square root among real numbers. Let's write a program that asks the user for a number before computing the square root, and in the case of a negative number, it displays that the root cannot be taken. In the case of zero or a positive number, it proceeds to compute the square root. The algorithm of the solution is shown here:  

```
Input: a
If a < 0 then Output: "The operation cannot be performed."
  else Output: square_root(a)
End of branching
```  

In C-like languages, compared to what we learned earlier, the coding expands with an `else` statement, after which we give the instructions for the false branch (for now, one statement each).  

In the image below and in the previous algorithm, you can see that I started on certain lines further inward. The program works without this as well; its purpose is solely to improve readability. Such formatting may be expected at workplaces and in schools, but it cannot be required during an advanced-level graduation exam.  

**C# version**:  
```csharp
int a;
a = Convert.ToInt16(Console.ReadLine());
if (a < 0)
  Console.WriteLine("The operation cannot be performed.");
else
  Console.WriteLine(Math.Sqrt(a));
```  

**C++ version**:  
```cpp
int a;
cin >> a;
if (a < 0)
  cout << "The operation cannot be performed.";
else
  cout << sqrt(a);
```

Here is the verbatim English translation of the provided Hungarian text:

---

### Comparison  

From the following table, it can be read what relational signs we can use when giving conditions.  

In C languages, = means let it be equal. Equality, as a comparison, received the symbol == so that it cannot be confused with let it be equal and the equal to expressions.  

It is also common to code not equal. In algorithmic languages (and in many other programming languages, as well as in Excel), the logical less or greater is coded with the symbol <>. In C languages, the ! symbol is the sign of negation (not), so the not equal sign is !=.  

| Name of operation        | C languages | Algorithm   |
|--------------------------|-------------|-------------|
| greater than             | a > b       | a > b       |
| less than                | a < b       | a < b       |
| greater than or equal to | a >= b      | a ≥ b       |
| less than or equal to    | a <= b      | a ≤ b       |
| equal to                 | a == b      | a = b       |
| not equal to             | a != b      | a ≠ b       |

---

### Tasks  

1. Request a real number from the user and determine its absolute value. If you cannot do it otherwise, ask for help from the worked-out solution.  

2. Write a program that, before taking the square root, asks the user for a number, and if the number is negative, displays that the root cannot be taken. In the case of zero or a positive number, perform the square root operation. If you cannot do it otherwise, ask for help from the worked-out solution.  

3. Ask the user for the number of ships visible from the lighthouse. If this value is greater than three, display "Heavy tower" on the screen; otherwise, do not display anything.  

4. Ask the user for two numbers, which will be the numerator and denominator of a common fraction. Decide whether the entered fraction can be expressed as an integer; if so, display its integer value, if not, display "Cannot be expressed."  

5. Write a program that asks for a 3-digit positive integer from the keyboard and determines whether it is an Armstrong number. A 3-digit Armstrong number is a number where the sum of the cubes of its digits equals the number itself, for example, 371 = 3³ + 7³ + 1³. Display the result on the screen!  

---
Here is the full verbatim English translation of the provided page:  

---

## III. CONTROL STRUCTURES  

**CONDITIONAL BRANCHING – MORE COMPLEX CASES**  

### Using a block of instructions  

When thinking in C languages, sometimes we would like to place multiple instructions in the false branch of a conditional statement. How will the compiler know where the end of the false branch is, and after that, where the end of the branching is? In C languages, there is no "end of branching" instruction like in sentence-like descriptions.  

In C languages, we use **instruction blocks** when we want to provide multiple instructions in one branch of a control structure, in our case, in the false branch. The instruction block groups the instructions together. Its symbol is the pair of curly brackets `{}`, between which we write the instructions.  

In the example code, in the branching (lines 15–20), we use an instruction block in the false branch. In line (20), the closing curly bracket marks the end of the false branch starting from line (17), containing all instructions executed in that branch (line 21). In the true branch (line 15), we do not need an instruction block, since we only execute a single instruction.  

```c
14 int a, b, c, k;  
15 if (k == 3) a = 1;  
16 else {  
17     a = 0;  
18     b = 0;  
19     c = 0;  
20 }  
21 k = a + b + c;  
```  

### Branching in multiple directions  

It may happen that more than two cases need to be separated. In this case, the branches will be nested into each other. This simply means that with the first branching we select between two possibilities, and then in one or both branches, we place further branchings.  

For example: let’s decide about a number, whether it is positive, negative, or zero. This is a three-case situation, which we cannot solve with a single conditional branching. First, we separate between zero and not-zero. If it is equal to zero (line 16), we can write that it is zero, and there is nothing more to do. If it is not equal to zero (line 17), another branching will follow inside the previous one, according to lines (18)–(19), whether it is greater than zero or not. On line (18), we can write that it is positive. On line (19), we can write that it is negative.  

In C language coding, instruction blocks must also be used in lines (17) and (20), because in line (18) and in the `else` (19) branch we count on two instructions, even though it is one single control structure.  

---

Here is the full verbatim English translation of the provided page:  

---

**MAGYARY GYULA**  

**Nesting branches within branches – algorithm**  

**Algorithm for nesting branches within branches**  

16) If a = 0 then print: '0'  
17) else  
18) If a > 0 then print: '+'  
19) else print: '-'  
20) end of branch  
21) end of branch  

```c
16 if (a==0) ki='0';  
17 else {  
18     if (a>0) ki='+';  
19     else ki='-';  
20 }  
```  

By nesting multiple branches within each other, we can create branching in three or more directions as well. If the Reader truly understands this topic, they will be able to answer the following questions: How many branches are needed to be nested in order to create a five-way branching? And what about in the case of n branches? The answer can be found in the footnote. 30  

---

### Compound conditions  

Compound conditions consist of partial conditions. For example, “smaller than 7 and greater than 0” is a compound condition made up of two partial conditions: “smaller than 7” and “greater than 0.”  

Both compound conditions and partial conditions can only have values that are either true or false, so we are dealing with logical expressions.  

Creating compound conditions from partial conditions is important, because the `if` statement can only accept a single logical (true/false) value. If we have multiple conditions, it is not sufficient to simply write them after one another, as that would result in multiple logical values.  

With the help of logical operations, we can combine multiple logical values into one, thus connecting partial conditions into a compound condition.  

---

### Logical AND  

| A     | B     | A ∧ B  |  
|-------|-------|--------|  
| true  | true  | true   |  
| true  | false | false  |  
| false | true  | false  |  
| false | false | false  |  

In the case of a logical AND operation, the result is only true if **all partial conditions** are true. In every other case, it is false.  

---

_Footnote: 30 — 4 branches for 4 directions, n-1 branches for n directions._  

---



68  Here is the full verbatim English translation of the provided page:  

---

**MAGYARY GYULA**  

**Nesting branches within branches – algorithm**  

**Algorithm for nesting branches within branches**  

16) If a = 0 then print: '0'  
17) else  
18) If a > 0 then print: '+'  
19) else print: '-'  
20) end of branch  
21) end of branch  

```c
16 if (a==0) ki='0';  
17 else {  
18     if (a>0) ki='+';  
19     else ki='-';  
20 }  
```  

By nesting multiple branches within each other, we can create branching in three or more directions as well. If the Reader truly understands this topic, they will be able to answer the following questions: How many branches are needed to be nested in order to create a five-way branching? And what about in the case of n branches? The answer can be found in the footnote. 30  

---

### Compound conditions  

Compound conditions consist of partial conditions. For example, “smaller than 7 and greater than 0” is a compound condition made up of two partial conditions: “smaller than 7” and “greater than 0.”  

Both compound conditions and partial conditions can only have values that are either true or false, so we are dealing with logical expressions.  

Creating compound conditions from partial conditions is important, because the `if` statement can only accept a single logical (true/false) value. If we have multiple conditions, it is not sufficient to simply write them after one another, as that would result in multiple logical values.  

With the help of logical operations, we can combine multiple logical values into one, thus connecting partial conditions into a compound condition.  

---

### Logical AND  

| A     | B     | A ∧ B  |  
|-------|-------|--------|  
| true  | true  | true   |  
| true  | false | false  |  
| false | true  | false  |  
| false | false | false  |  

In the case of a logical AND operation, the result is only true if **all partial conditions** are true. In every other case, it is false.  

---

_Footnote: 30 — 4 branches for 4 directions, n-1 branches for n directions._  

---

Here is the full verbatim English translation of the provided page:  

---

### III. CONTROL STRUCTURES | 69  

For two partial conditions (A and B), the attached table is valid. However, it is important to know that this operation can be applied to more than two partial conditions based on the previous explanation and definition.  

For example: let’s check the correctness of a number provided by the user. It should be considered correct if its value falls between 1 and 8, including the boundaries. We can only print the message "Good" if both partial conditions a ≥ 1 and a ≤ 8 are true. In this case, we need to use the AND operation (line 16).  

The standard symbol for the AND operation in algorithmic language is: ^. However, often the words AND or the English AND are used instead, since typing the ^ character can be problematic. In C languages, we use the && symbol for this purpose. ³¹ (16).  

---

### Logical OR  

| A     | B     | A ∨ B  |  
|-------|-------|--------|  
| true  | true  | true   |  
| true  | false | true   |  
| false | true  | true   |  
| false | false | false  |  

In the case of a logical OR operation, the result is true if **any of the partial conditions** is true. This includes situations where one or more partial conditions are satisfied. In other words, the operation is false **only if all partial conditions are false**. In every other case, the result is true.  

For two partial conditions (A and B), the attached table is valid. However, it is important to know that this operation can also be applied to more than two partial conditions based on the previous explanation and definition.  

For example: let’s check the correctness of a number provided by the user. In this case, we print the message "Bad" if the number is less than or equal to 1, or greater than or equal to 8. The "Bad" message must be printed if either of the two partial conditions is satisfied. So in this case, we need to use the OR operation (line 18).  

The standard symbol for the OR operation in algorithmic language is the ∨ character. However, often the OR or the English OR words are used instead. In C languages, the `||` symbol is used. ³² (18).  

---

_Footnotes:_  
³¹ The single ampersand & symbol in C languages is used for the bitwise AND operation.  
³² The single pipe | symbol in C languages is used for the bitwise OR operation.  

---

Here is the full English translation of the page you provided:  

---

**MAGYARY GYULA**  

## Logical NOT  

| A   | ¬A   |
|-----|------|
| true  | false |
| false | true  |

The logical NOT operation simply turns truth into falsehood and falsehood into truth. In algorithm description language, it is represented by the ¬ symbol. If writing this symbol is problematic, the words NOT or NEM are used instead. The opposite (negation) of `a > 1` is `a <= 1`; for example, if a number greater than 1 is given, the word "good" will be displayed.  

### Compound conditions – algorithm  

16) If a >= 1 AND a <= 8 then  
17) Print: "good"  
18) If a <= -1 OR a >= 8 then  
19) Print: "bad"  
20) If NOT (a <= 1) then Print: "good"  

### Compound conditions – in C language  

| Line | Example in C                              |
|------|------------------------------------------|
| 16   | `if (a >= 1 && a <= 8)` <br> `printf("good");`   |
| 18   | `if (a <= -1 || a >= 8)` <br> `printf("bad");`   |
| 20   | `if (!(a <= 1))` <br> `printf("good");`   |

It is possible to connect multiple conditions using logical operations. Sometimes a complex chain of logical operations is formed, so it’s important to know the **order of operations**:  
Parenthetical expression > NOT > AND > OR  

In practice, however, I have experienced that it’s often advisable to enclose every sub-condition in parentheses, because sometimes the compiler does not interpret the operations the same way as the developer intends.  

Similarly, it can be worthwhile to subject chains of logical operations to simplification procedures, or break them down into multiple branches. The AND operation can be replaced by nested branches, and the OR operation can be replaced by sequentially applied branching.  

---

**Footnote:**  
33 The possibilities of simplification are omitted here due to space constraints. In the appropriate literature, you can find a systematic approach to simplification procedures for logical functions.  

---

Here’s the full English translation of the page you provided:

---

### III. CONTROL STRUCTURES  

### Exercises  

1. Ask the user for a real number and display whether it is positive, negative, or zero. If not used elsewhere, apply the result to a previously developed task.  

2. Ask the user for two integers and display them in ascending order. In the case of equality, display the number only once.  

3. A courier receives payment based on the distance traveled according to the table below. Ask the user for a distance between 1 and 30 km, and determine how much payment they receive for it.  

| Distance   | Payment   |
|------------|-----------|
| 1 – 2 km   | 500 Ft    |
| 3 – 5 km   | 700 Ft    |
| 6 – 10 km  | 900 Ft    |
| 11 – 20 km | 1400 Ft   |
| 21 – 30 km | 2000 Ft   |

4. Write a program that asks for three pieces of information about a plot of land: tax amount, length, and width. If the width is 15 m or less, or the length is 25 m or less, the property owner receives a 20% tax discount. Calculate and display the corrected tax amount including this discount.  

5. Write a program that reads the lengths of three line segments (a, b, and c) from the keyboard and determines (and displays on screen) whether a triangle can be constructed from those segments. Three segments can form a triangle if and only if the sum of the lengths of any two sides is greater than the length of the third side.  

---

**Footnote:**  
34 The triangle inequality theorem.  

---


