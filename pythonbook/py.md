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

### **Modifying the Program with Colors and Fill**

This section explains how to modify the previously created rectangle program to include **color and fill**, making the inner part red and the border gold.

#### **Steps:**
10. **Open the Saved Program:**
    - Open the editor, where the previous rectangle-drawing program is visible.

11. **Enter the New Program:**
    - Type the following program **line by line**, pressing **Enter** at the end of each line.

12. **Reset the Screen:**
    - The `reset()` command **clears** the graphics window and **resets the turtle** to its default position.

13. **Set Border Color:**
    - The `color("gold")` command **changes the border color** to **gold**.

14. **Set Fill Color:**
    - The `fillcolor("red")` command **sets the inner fill color** to **red**.

15. **Begin and End Fill:**
    - The **`begin_fill()`** and **`end_fill()`** commands define the **shape to be filled**.
    - Any shape drawn **between these commands** will be filled with **red**.

16. **Save the File:**
    - Click **File → Save As…**, name the file **feladat_02.py**, and save it.

17. **Run the Program:**
    - Press **F5** to execute it.
    - The **Python Turtle Graphics** window will display a **gold-bordered rectangle filled with red**.

---

### **Tasks for Further Practice**
1. **Draw the Left-side Figure:**
   - Create a drawing where each segment is **100 units long**.
   
2. **Draw the Middle Figure:**
   - Draw a **regular triangle**, where all sides are **100 units** long.

3. **Draw a Simple House:**
   - Use a single **continuous line** (without lifting the pen).
   - The **roof** should be **symmetrical**, with **equal-length slanted lines**.
   - Each segment should be **100 units long**.
   - Ensure the **right angle of the house base** is accurate.

This section expands on **basic turtle graphics**, introducing **color fills**, **structured programming**, and **more complex shapes**.

Here is the Python code for the modified rectangle with a **gold border** and **red fill** using Turtle Graphics:

```python
from turtle import *

reset()            # Clears the screen and resets the turtle
color("gold")      # Sets the border color to gold
fillcolor("red")   # Sets the fill color to red

begin_fill()       # Start filling the shape
forward(400)       # Draw bottom side
left(90)
forward(100)       # Draw left side
left(90)
forward(400)       # Draw top side
left(90)
forward(100)       # Draw right side
left(90)
end_fill()         # Stop filling the shape
```

### **Explanation:**
- `reset()` clears the screen and resets the turtle to its default position.
- `color("gold")` sets the **border** color to gold.
- `fillcolor("red")` sets the **fill** color to red.
- `begin_fill()` and `end_fill()` wrap around the **rectangle-drawing commands** to fill the shape.

#### **Execution**
- Save this script as **feladat_02.py**.
- Run it using **F5** in Python's IDLE.

This program will **draw a filled rectangle** with **gold borders** and a **red interior** in the Python Turtle Graphics window. 🚀

3. Procedure

### **3. PROCEDURE (Function)**
This section explains how to **reuse code** by defining a **procedure (function)** in Python. Instead of repeating the same instructions to draw multiple rectangles, we can define a **procedure** and call it multiple times.

---

### **Concept: Using a Function to Reuse Code**
- When we need to **draw multiple identical rectangles**, writing the same commands repeatedly is inefficient.
- A **procedure (function)** allows us to group commands together under a **name**.
- When we call the function by its name, **all the instructions inside it execute in order**.

---

### **3rd Example Task – Reusing Code with a Procedure**
We will **modify the previous program (feladat_02.py)** to draw **three rectangles** in red, white, and green, forming a **Hungarian flag**.

#### **Steps:**
1. **Open the Previous Program:**
   - Click **File → Open…** and select **feladat_02.py**.

2. **Modify the Code:**
   - Add a **procedure (function)** to define the **rectangle-drawing code**.

3. **Define the Procedure:**
   - A function is introduced using `def` followed by the function name **teglalap()** (meaning "rectangle").
   - The commands inside the function **must be indented**.

4. **Understanding Indentation:**
   - When pressing *Enter* after the function definition, the next lines **must be indented**.
   - Press the **Tab key** to maintain correct indentation.

5. **Calling the Procedure:**
   - After defining `teglalap()`, we can **call** it multiple times in different positions.

---

### **Final Python Code:**
```python
from turtle import *

def teglalap():   # Function to draw a rectangle
    begin_fill()
    forward(400)
    left(90)
    forward(100)
    left(90)
    forward(400)
    left(90)
    forward(100)
    left(90)
    end_fill()

reset()
color("gold")  
fillcolor("red")
teglalap()        # Draw first rectangle (red)

up()
forward(100)      # Move up
left(90)
down()

fillcolor("white")
teglalap()        # Draw second rectangle (white)

up()
forward(100)      # Move up again
left(90)
down()

fillcolor("green")
teglalap()        # Draw third rectangle (green)
```

---

### **Explanation:**
- **Defining a Function (`def teglalap()`)**
  - The function groups the rectangle-drawing commands together.
  - It uses `begin_fill()` and `end_fill()` to **fill the rectangle**.

- **Calling the Function Multiple Times**
  - After defining the function, we call `teglalap()` **three times**, each with a different fill color.

- **Moving the Turtle (`up()` and `down()`)**
  - The `up()` command lifts the turtle's pen, allowing it to move without drawing.
  - The `down()` command puts the pen back down to start drawing again.

---

### **Output:**
- The script draws **three rectangles**:
  - **Red at the bottom**
  - **White in the middle**
  - **Green at the top**
- The final drawing represents the **Hungarian flag** using Python Turtle Graphics.

---

### **Benefits of Using a Function:**
✅ **Reusability** – We only write the rectangle-drawing code **once**.  
✅ **Readability** – The program is **cleaner and easier to understand**.  
✅ **Efficiency** – We can change the **rectangle size or shape** by editing just one function.

This section introduces **basic functions in Python**, making code **more structured and reusable**. 🚀

### **Extending the Flag Drawing Program**

This section builds upon the previous **Hungarian flag** drawing program by refining **positioning** and **flag variations**.

---

### **Steps to Draw the Hungarian Flag Properly:**
6. **Calling the Function Three Times:**  
   - The function `teglalap()` is called **three times** (lines 17, 23, 29).
   - Each call executes the **same drawing commands**, filling each rectangle with **different colors**.

7. **Setting the Fill Colors:**  
   - Each function call **sets the fill color** before drawing:
     - **Red (line 16)**
     - **White (line 22)**
     - **Green (line 28)**

8. **Positioning the Turtle:**  
   - After drawing the **first rectangle**, the turtle is at the **bottom left corner**.
   - The next rectangle must **start from the same position** but **100 pixels lower**.
   - The turtle moves **down** by **100 pixels** (lines 19, 25).

9. **Lifting the Brush (Pen) While Moving:**  
   - To avoid drawing unintended lines while moving, the `up()` command is used (lines 18, 24).

10. **Placing the Brush Down Before Drawing:**  
   - The `down()` command ensures that the turtle **starts drawing** again before each rectangle (lines 21, 27).

11. **Adjusting the Turtle’s Orientation:**  
   - Since the drawing originally went **downwards**, the turtle **starts facing right**.
   - Before drawing each new rectangle, the turtle **rotates left by 90 degrees** (lines 20, 26).

12. **Saving the Program:**  
   - Click **File → Save As…**, and name the file **feladat_03.py**.

13. **Running the Program:**  
   - Press **F5** to execute it.
   - The **Hungarian flag** (red, white, green) appears in the **Python Turtle Graphics** window.

---

### **Additional Exercises**
1. **Modify `feladat_03.py` to Draw the German Flag:**
   - Change colors to **black, red, and yellow** (fekete-piros-sárga).

2. **Modify `feladat_03.py` for Two-Stripe Horizontal Flags:**
   - Adjust the function to draw **two equal horizontal stripes**.
   - Example: **Polish flag** (white-red).

3. **Modify `feladat_03.py` for Three-Stripe Vertical Flags:**
   - Modify the function to draw **three equal vertical stripes**.
   - Example: **Irish flag** (green-white-orange).

---

### **Key Learning Points:**
✅ **Code Reusability:** The `teglalap()` function simplifies repetitive drawing.  
✅ **Positioning Logic:** The turtle **lifts the pen, moves, and rotates** correctly.  
✅ **Adaptability:** The function is flexible, allowing easy modifications for **different flags**.  

This section strengthens **Python programming** skills by integrating **functions, movement logic, and color customization**. 🚀

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