FOREWORD

The preface of the book explains that it is primarily aimed at students preparing for an advanced-level IT exam, but it can also be useful for vocational training, university studies, or self-learning. The book uses Python as the programming language due to its simplicity, logical structure, and suitability for beginners. 

It follows a step-by-step approach through exercises and problem-solving. The chapters introduce programming basics, different programming languages, algorithms, Python's core elements, programming structures, and graphical applications. The book avoids deep dives into object-oriented programming, as it is not required for the exam, and focuses on practical problem-solving. 

The final section of the preface highlights that the book includes a summary chapter (Chapter IX) for review and reinforcement of key concepts. Due to space constraints, not all full programs are included in the book, but the most important ones are in the appendices, and additional materials can be downloaded from the publisher's website.

The book was written using Python 3.8.0, and both Windows and Linux-based Python development environments are included in the exam's software options. PyCharm users should not encounter issues using this book.

For learning Python, the book references Gérard Swinnen’s freely available guide under the GNU Free Documentation License. Official Python documentation and Hungarian-language web resources are also mentioned as helpful references. 

Additionally, exam-related sample tasks can be downloaded from the Hungarian Education Office’s website. The preface concludes with well wishes for readers on their learning journey.

I. INTRODUCTION TO PROGRAMMING
1. Commands

This section introduces programming by explaining how computers execute commands. It begins with basic command-line interactions in Python.

### Key Points:
- **Commands:** Programming involves giving instructions (commands) to the computer.
- **Python Interpreter:** When Python starts, it opens a command window (interpreter) where users can type commands.
- **Executing Commands:** Commands are entered at the prompt (`>>>`), and pressing *Enter* executes them.

### Sample Exercise – Using Commands:
1. Open Python's interpreter from the *Start* menu under *Python x.x (IDLE Python x.x 64-bit)*.
2. In the interpreter window, type commands after the `>>>` prompt.
3. The first command initializes the environment.
4. Users then enter commands, followed by *Enter* to execute them.

This section serves as a beginner-friendly introduction to Python command execution.


This section introduces the **Python Turtle Graphics** module, which allows users to draw shapes using simple commands.

### Key Points:
- **No Errors:** If the command interpreter does not display a red error message, the command was entered correctly.
- **Turtle Concept:** Imagine a turtle with a brush on its belly that moves across the screen to draw.

### Drawing with Python Turtle:
1. **Drawing a Line:**
   - The turtle moves **forward 400 units** with:
     ```python
     forward(400)
     ```
   - A new graphics window appears, showing a straight line.

2. **Turning the Turtle:**
   - To rotate **90 degrees left**, enter:
     ```python
     left(90)
     ```

3. **Continuing the Drawing:**
   - Move the turtle **100 units forward** with:
     ```python
     forward(100)
     ```

4. **Challenge: Completing a Rectangle**
   - To finish the rectangle, the user must add:
     ```python
     left(90)
     forward(400)
     left(90)
     forward(100)
     ```
   - This completes a **rectangular shape** with the turtle.

### Learning Outcome:
- Users learn **basic movement commands** (`forward`, `left`).
- Parameters (values inside parentheses) define the movement **distance** and **angle**.
- Encourages problem-solving by asking users to complete the shape themselves.

This section provides a hands-on introduction to Python's **Turtle Graphics** for visual programming.




2. Program

This section explains how to **save and run a Python program** that draws a rectangle using the Turtle Graphics module.

### Key Steps:
1. **Create a New File:**
   - In **Python Shell**, click on **File → New File** to open an **editor window**.

2. **Enable Line Numbers:**
   - For better readability, enable **line numbering** under **Options → Show Line Numbers**.

3. **Write the Program:**
   - Type the following code into the editor:
     ```python
     from turtle import *
     forward(400)
     left(90)
     forward(100)
     left(90)
     forward(400)
     left(90)
     forward(100)
     left(90)
     ```
   - This script **draws a rectangle** using the turtle.

4. **Save the File:**
   - Click **File → Save As…**, choose a location, and name the file **feladat_01.py**.

5. **Understanding Programs:**
   - Until now, users **executed commands one by one**.
   - Now, **commands are saved in a file**, making it a **program** that runs **all instructions automatically**.

6. **Run the Program:**
   - Press **F5** in the editor to execute the script.
   - The **Python Turtle Graphics** window will display a **rectangle**.

7. **Reopen the Program:**
   - Close the script window using the **X button**.
   - Reopen it later by clicking **File → Open…** and selecting **feladat_01.py**.

### Learning Outcome:
- Introduces **saving and running Python scripts**.
- Differentiates between **interactive commands** and **scripts**.
- Emphasizes **code organization** and **execution from files**.

This section transitions learners from **manual commands** to **writing and running full programs** efficiently.


3. Procedure
4. Variables
5. Branching
6. Counting cycle
7. Using variables
8. Random number
9. List
10. Conditional loop
11. Recursion

II. BASICS OF PROGRAMMING
1. General structure of a program
2. Algorithm
3. Programming languages
4. Errors
5. Steps in program development

III. PYTHON BASICS
1;
2. Basic operations
3. Variables
4. Program
5. Data request
6. Formatted printout
7. Random numbers
8. Notes in the program
9. Logical variable, logical value
10. Practical exercises

IV. BASIC CONTROL STRUCTURES
1. Sequential execution
2. Conditional branching - basics
3. Multi-directional branching (elif)
4. branching with a compound condition (not, and, or)
5. Characters and strings in the condition
6. Principle of full coverage
7. Cycles
8. Counting cycles
9. nesting cycles
10. Conditional cycles
11. Subroutines
12. Procedures
13. Functions
14. Recursion
15. Modular programming and testing

V. COMPLEX DATA STRUCTURES
1. List
2. List entry (for)
3. String as a list
4. Further operations with strings
5. List in a list, multidimensional list
6. Lists in procedures and functions
7. Dictionaries
8. Records
9. Simple text files
10. Reading files
11. Write to file

VI. PROGRAMMING ITEMS
1. Introduction
2. Sequence calculation
3. Aggregation
4. Counting
5. Maximum selection
6. Decision
7. Linear search
8. Selection
9. Sorting
10. Solving problem sets

VII. OBJ

Translated with www.DeepL.com/Translator (free version)