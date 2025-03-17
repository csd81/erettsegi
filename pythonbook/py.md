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

### **4. VARIABLES**
This section introduces **variables** in Python, which allow us to write a **generalized function** that can draw **any tricolor flag** without modifying the code every time.

---

### **Concept: Why Use Variables?**
- Instead of hardcoding the colors in our function, we can **use variables** to store **values** dynamically.
- A **variable is a temporary storage space** that we can refer to by name.
- Imagine a **labeled drawer**: you can put something in, check it later, and update it whenever needed.

---

### **Goal: A Flexible Tricolor Flag Function**
We want to create a **function named `trikolor()`** that:
- Accepts **three parameters** (colors for the top, middle, and bottom stripes).
- Uses those parameters to draw a **tricolor flag** dynamically.

---

### **4th Example Task – Using Variables**
1. **Open the `feladat_03.py` file.**
2. **Modify the Program:**
   - Add the **new function** `trikolor()` as shown below.
   - The first **13 lines remain unchanged** from `feladat_03.py`.

3. **Define the Function:**
   - The `trikolor(f, k, a)` function accepts **three color parameters** (`f`, `k`, `a`).
   - These represent the **top, middle, and bottom stripe colors**.

4. **Using Variables in the Function:**
   - Instead of hardcoding the colors, replace them with the **parameters**.

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

def trikolor(f, k, a):   # Function to draw a tricolor flag
    fillcolor(f)
    teglalap()
    up()
    forward(100)
    left(90)
    down()
    fillcolor(k)
    teglalap()
    up()
    forward(100)
    left(90)
    down()
    fillcolor(a)
    teglalap()

reset()
color("gold")

# Call the function with different color sets
trikolor("red", "white", "green")     # Hungarian flag
up()
goto(-420, 0)     # Move turtle left
down()
trikolor("red", "yellow", "black")    # German flag
```

---

### **Explanation:**
- **Defining `trikolor(f, k, a)`**
  - This function **receives three parameters** (`f`, `k`, `a`) to determine the flag colors.
  - Instead of **hardcoding fill colors**, it **uses the passed values** dynamically.

- **Calling the Function**
  - `trikolor("red", "white", "green")` → **Draws the Hungarian flag**.
  - Moves the turtle **left** using `goto(-420, 0)`.
  - `trikolor("red", "yellow", "black")` → **Draws the German flag**.

---

### **Key Learning Points**
✅ **Reusability** – The function works for any **tricolor flag**.  
✅ **Efficiency** – No need to modify the function; just **change parameters**.  
✅ **Scalability** – Easily extendable for **more flag designs**.  

This lesson introduces **dynamic programming with variables**, making Python **more powerful and flexible**! 🚀

### **Enhancing the Flag Drawing with Variables**
This section refines the **tricolor flag drawing function** by optimizing how colors are passed and reusing code efficiently.

---

### **Key Improvements**
5. **Using Variables for Fill Colors:**
   - Instead of hardcoding colors, the **fillcolor** command now takes the first parameter (`f`) for the **top stripe** (line 15).

6. **Assigning the Middle and Bottom Colors:**
   - The function assigns the **middle stripe** color from the **second parameter (`k`)** (line 21).
   - The **bottom stripe** takes the **third parameter (`a`)** (lines 14 and 27).

7. **Calling the Function Twice:**
   - The `trikolor()` function is called twice to draw **two different flags** (lines 33 & 37).

8. **Positioning Flags Correctly:**
   - To prevent overlapping, the **second flag starts at (-420, 0)**.
   - The `goto(-420, 0)` command moves the turtle to this **new position** (line 35).

9. **Saving the Program:**
   - Save the file as **feladat_04.py** and run it.

---

### **Understanding the Use of Variables**
- **Text-type variables** store color names as **strings** (e.g., `"gold"` or `'gold'`).
- **Numbers are unnecessary** for storing colors.
- **Code Efficiency**:
  - Without **functions**, the program would need **60+ lines**.
  - By using **functions**, we reduced it to **just 7 lines**, saving **53 lines** of repetition.
  - **Improves readability and maintainability**.

---

### **Additional Exercises**
1. **Create a `dicolor()` Function:**
   - Modify `feladat_04.py` to define a **dicolor function** for **two-striped horizontal flags**.
   - The **flag size remains the same**.
   - The function takes **two colors** (e.g., `"white", "red"` for the Polish flag).

2. **Create a `trikolor()` Function for Vertical Flags:**
   - Modify an earlier program (`gyak_04_1.py`) to handle **three-striped vertical flags**.
   - The **flag dimensions match the horizontal tricolor flags**.
   - The function takes **three colors**, assigning them to the **left, middle, and right stripes** (e.g., `"green", "white", "orange"` for the Irish flag).

---

### **Key Learning Points**
✅ **Optimized Code** – Uses **functions and variables** instead of repetitive instructions.  
✅ **Scalability** – Works for **multiple flag designs** with **minimal changes**.  
✅ **Efficient Coding Practices** – Saves **53+ lines** and **improves readability**.

This section builds **strong Python skills** by integrating **functions, parameters, and efficient code structures**! 🚀


5. Branching
### **5. CONDITIONAL STATEMENTS (Branching)**

This section introduces **conditional statements (if-elif-else)** in Python, allowing a program to choose different actions based on given conditions.

---

### **Concept: Why Use Conditional Statements?**
- Instead of calling different functions manually, we can **create a function that automatically selects the correct flag** based on the country's name.
- The program will **branch** and execute different instructions depending on the country name given as input.

---

### **5th Example Task – Using Conditional Statements**
We will create a function called **`zaszlo()`** that:
- Accepts a **country name (`nemzet`)** as a parameter.
- Draws the **appropriate horizontal tricolor flag** based on the country.
- Defaults to a **white-white-white** flag if an unlisted country is entered.

#### **Flag Assignments**
| Country  | Colors (Top-Middle-Bottom) |
|----------|----------------------------|
| Hungary  | Red - White - Green        |
| Austria  | Red - White - Red          |
| Germany  | Black - Red - Yellow       |
| Netherlands | Red - White - Blue      |
| Others   | White - White - White (Error Flag) |

---

### **Final Python Code:**
```python
def zaszlo(nemzet):
    if nemzet == "magyar":
        trikolor("red", "white", "green")
    elif nemzet == "osztrak":
        trikolor("red", "white", "red")
    elif nemzet == "nemet":
        trikolor("black", "red", "yellow")
    elif nemzet == "holland":
        trikolor("red", "white", "blue")
    else:
        trikolor("white", "white", "white")  # Default flag for incorrect input

reset()
color("gold")

zaszlo("magyar")  # Draw Hungarian flag

up()
goto(-420, 0)  # Move turtle left for second flag
down()

zaszlo("nemet")  # Draw German flag
```

---

### **Explanation**
1. **Defining `zaszlo(nemzet)`**
   - The function takes a **country name** as input.
   - The **`if` statement** checks if `nemzet` matches a known country.
   - If a match is found, it calls `trikolor()` with the correct **colors**.
   - If no match is found, the **default flag** (`white-white-white`) is drawn.

2. **Using `if`, `elif`, and `else`**
   - `if` checks for **Hungary**.
   - `elif` checks for **Austria, Germany, and Netherlands**.
   - `else` assigns a **default flag** for **unknown country names**.

3. **Calling the Function**
   - `zaszlo("magyar")` → Draws **Hungarian flag**.
   - Moves the turtle **left** (`goto(-420, 0)`).
   - `zaszlo("nemet")` → Draws **German flag**.

---

### **Key Learning Points**
✅ **Automated Decision Making** – The function chooses the correct flag **based on input**.  
✅ **Efficiency** – No need to manually call `trikolor()` for each flag.  
✅ **Error Handling** – Unrecognized inputs result in a **white-white-white flag**.  

This section introduces **if-elif-else logic**, a fundamental concept in Python programming! 🚀

### **Enhancing Conditional Logic in the Flag Drawing Program**
This section expands the **zaszlo()** function, introducing additional countries and refining **conditional statements (`if-elif-else`)**.

---

### **Understanding Conditional Execution**
- If the input matches `"magyar"`, the function calls `trikolor()` with Hungary’s flag colors.
- If `"magyar"` **is not matched**, the program **skips that part** and checks the next condition (`elif`).
- If `"osztrak"` is given, the Austrian flag is drawn.
- The same logic applies to other countries.
- If no match is found, the function **defaults** to a **white-white-white** flag.

---

### **Key Steps in the Code**
5. **Using `if` for Hungary**  
   - Calls `trikolor("red", "white", "green")`.

6. **Using `elif` for Other Countries**  
   - Each `elif` checks for another country name.
   - Example:  
     ```python
     elif nemzet == "osztrak":
         trikolor("red", "white", "red")
     ```
   - The last `elif` is for Germany.

7. **Adding `else` for Invalid Inputs**  
   - If **none of the conditions match**, it executes:
     ```python
     else:
         trikolor("white", "white", "white")
     ```
   - This displays a **default flag** to indicate an invalid input.

8. **Modifying the Main Program**  
   - Replace `trikolor()` calls with `zaszlo()`, passing the **country name** as an argument.

9. **Saving and Running the Program**  
   - Save the file as **feladat_05.py**.
   - Run it to see different flags based on input.

---

### **Additional Exercises**
1. **Extend `feladat_05.py`**  
   - Add support for the **Yemeni** (red-white-black) and **Russian** (white-blue-red) flags.

2. **Modify `gyak_05_1.py`**  
   - Detect and draw **vertically striped** flags like:
     - **Polish (red-white)**
     - **Monaco (red-white)**
     - **Nigerian (green-white-green)**
     - **Italian (green-white-red)**

3. **Understanding `==` vs. `=` in Python**  
   - `==` checks if two values are **equal**.
   - `=` assigns a **new value** to a variable.
   - Example:
     ```python
     a = 2  # Assigns 2 to 'a'
     if a == 2:  # Checks if 'a' is equal to 2
         print("a is 2")
     ```

---

### **Key Learning Points**
✅ **Expands Condition Handling** – Can now handle **more country flags**.  
✅ **Code Efficiency** – Uses **functions** instead of repeating code.  
✅ **Logical Comparisons** – Introduces `==`, `!=`, `<`, `>` operators.  

This section builds on **control flow in Python**, reinforcing **decision-making and automation**! 🚀

6. Counting cycle

### **6. COUNTED LOOPS (For Loop)**

This section introduces **loops** in Python, allowing the program to **repeat instructions** efficiently instead of writing them multiple times.

---

### **6th Example Task – Repeating a Program Section with a Loop**
We will write a program that **draws a regular octagon**, where each side is **100 pixels long**.

---

### **Steps to Draw an Octagon**
1. **Open the Python Command Prompt**
   - Open the Python Shell and type commands manually.

2. **Clear the Screen and Reset the Turtle**
   ```python
   reset()
   ```
   - This clears the **graphics window** and resets the **turtle’s position**.

3. **Draw the First Side**
   ```python
   forward(100)
   ```
   - Moves the turtle **forward by 100 pixels**.

4. **Turn Right by 45 Degrees**
   ```python
   right(45)
   ```
   - Rotates the turtle **to start drawing the next side**.

5. **Repeat Steps 3 and 4 for a Total of 8 Times**
   - Instead of **writing this eight times manually**, we use a **loop**.

---

### **Using a For Loop**
A **loop** allows Python to **repeat the same instructions** automatically.

```python
from turtle import *

reset()  # Clear screen and reset turtle

for _ in range(8):  # Repeat 8 times
    forward(100)  # Move forward
    right(45)  # Turn right 45 degrees
```

---

### **Explanation**
- `for _ in range(8):`  
  - This means **"repeat the following block 8 times"**.
- `_` is a **throwaway variable** (since we don’t use it inside the loop).
- Inside the loop:
  - The turtle **moves forward 100 pixels**.
  - The turtle **turns right by 45 degrees**.
- After 8 repetitions, the turtle **completes the octagon**.

---

### **Key Learning Points**
✅ **Eliminates Repetition** – The **loop replaces 16 lines of manual code**.  
✅ **Efficient** – We can easily **change the number of sides** by modifying `range(8)`.  
✅ **Flexible** – This method works for **other polygons** (e.g., hexagons, pentagons).  

This section introduces **counted loops (`for` loops)**, a fundamental programming concept for **automation and efficiency**! 🚀

### **6. COUNTED LOOPS (For Loop) – Continued**

This section continues with **for loops**, focusing on **loop variables** and more **efficient shape drawing**.

---

### **Key Insights**
8. **Typing the Code Precisely**  
   - Enter the commands **exactly as shown**, pressing **Enter** after each line.

9. **Understanding the For Loop in Line 3**
   ```python
   for i in range(8):
   ```
   - This is a **counted loop**, running **8 times**.
   - `i` is the **loop variable**, increasing from **0 to 7**.
   - The loop **repeats the commands** below it each time.

10. **Loop Indentation**
   - Python **requires indentation** (4 spaces or **Tab**) inside the loop.
   - The commands **inside the loop**:
     ```python
     forward(100)
     right(45)
     ```
   - These **repeat 8 times**, drawing the **octagon**.

11. **Saving the Program**
   - Click **File → Save As…** and name the file **feladat_06.py**.

12. **Running the Program**
   - Press **F5** to execute it.
   - The **Turtle Graphics window** will display an **octagon**.

---

### **Additional Exercises**
1. **Modify `feladat_06.py` to Draw a Hexagon**
   - Change the loop to **repeat 6 times**.
   - Modify the **turning angle**.

2. **Draw a Tiled Wall of 20×20 Squares**
   - Create **25 columns** and **12 rows**.
   - Use **nested loops** to **reduce repetition**.

3. **Draw the Star from the Image**
   - The **rays** should be **200 units long**.
   - Each **small square** at the end of a ray is **20×20 units**.
   - Use **loops** to automate the drawing.

---

### **Key Learning Points**
✅ **Loop Variables** – Allow precise repetition without manual code duplication.  
✅ **Efficient Drawing** – **Eliminates redundant commands** with loops.  
✅ **Nested Loops** – Enable complex **patterns and grid-based designs**.  

This section reinforces **Python loops**, laying the groundwork for **automated pattern generation**! 🚀

7. Using variables

### **7. USING VARIABLES**
This section introduces **variables** in Python, demonstrating how to **store, modify, and use values dynamically**.

---

### **7th Example Task – Understanding Variables**
1. **Opening the Python Command Line**
   - Open the **Python Shell** and enter commands interactively.

2. **Assigning a Value to a Variable**
   ```python
   x = 10
   ```
   - Stores the value **10** in the variable `x`.

3. **Checking the Stored Value**
   ```python
   x
   ```
   - The output should display **10**.

4. **Increasing the Value of `x`**
   ```python
   x += 20
   ```
   - Adds **20** to `x`, making `x = 30`.

5. **Verifying the Change**
   ```python
   x
   ```
   - Displays **30**, confirming the update.

6. **Decreasing the Value of `x`**
   ```python
   x -= 15
   ```
   - Subtracts **15** from `x`, making `x = 15`.

7. **Verifying the Change Again**
   ```python
   x
   ```
   - Displays **15**.

8. **Multiplying the Value Without Changing `x`**
   ```python
   x * 10
   ```
   - Displays **160**, but `x` remains **unchanged**.

---

### **Drawing the Spiral Using a Loop**
The accompanying **spiral** pattern suggests using **loops** to automate movement.

```python
from turtle import *

reset()
x = 10  # Initial side length

for _ in range(16):  # Repeat 16 times
    forward(x)
    left(90)
    x += 10  # Increase side length
```

---

### **Key Learning Points**
✅ **Storing Values** – Variables **hold values** that can be **changed or used** later.  
✅ **Updating Variables** – Use `+=` and `-=` for **incrementing and decrementing**.  
✅ **Looping with Variables** – **Dynamic updates** allow **automated shape drawing**.  

This section teaches **essential programming logic**, making Python **more powerful for automation**! 🚀

### **8. Example Task – Using Variables in a Program**

This section explains how to use **variables and loops** to draw a **spiral pattern**, where each step is longer than the previous one.

---

### **Step-by-Step Instructions**
1. **Create a New Program**
   - Open **File → New File** in Python IDLE.
   - Save it as **feladat_07_1.py**.

2. **Initialize a Variable**
   ```python
   x = 10
   ```
   - The turtle will move **10 units** initially.

3. **Set Up a Loop**
   ```python
   for i in range(20):
   ```
   - The loop will **repeat 20 times**, drawing each segment.

4. **Move Forward and Turn Left**
   ```python
   forward(x)
   left(90)
   ```
   - Moves the turtle **forward by `x`** units.
   - Rotates **90 degrees left**.

5. **Increase the Length of Each Step**
   ```python
   x += 10
   ```
   - After each loop iteration, `x` increases by **10**.
   - The next segment will be **longer**.

6. **Save and Run**
   - Save the file and press **F5** to execute.

---

### **Final Python Code**
```python
from turtle import *

x = 10  # Initial step length

for i in range(20):  # Repeat 20 times
    forward(x)
    left(90)
    x += 10  # Increase step size
```

---

### **How It Works**
✅ **Starts with a Short Step** – `x = 10`.  
✅ **Each Step Gets Longer** – `x` increases by `10` every time.  
✅ **Forms a Spiral** – The turtle **keeps turning left**, creating the shape.

This method efficiently draws a **growing square spiral** using **loops and variables**! 🚀

### **Optimizing the Spiral Drawing with Loop Variables**

This section introduces **more efficient ways to modify step sizes** using the **loop variable itself**.

---

## **Second Version – Using the Loop Variable (`i`)**
Instead of using a separate variable (`x`), we directly utilize **the loop variable `i`** to determine step length.

### **Steps**
1. **Create a New Program**
   - Save it as **feladat_07_2.py**.

2. **Modify the `for` Loop**
   ```python
   for i in range(20):
       forward(10 * i + 10)
       left(90)
   ```
   - The loop runs **20 times**.
   - The step size is determined by:  
     **`10 * i + 10`** → Results in **10, 20, 30, ..., 200**.

3. **Save and Run**
   - Press **F5** to execute.

---

## **Third Version – Adjusting the Loop Range (`range(start, stop, step)`)**
A more **structured approach** to controlling the loop variable.

### **Steps**
1. **Create a New Program**
   - Save it as **feladat_07_3.py**.

2. **Modify the `for` Loop**
   ```python
   for i in range(10, 210, 10):
       forward(i)
       left(90)
   ```
   - **Start at 10**, end before **210**, increasing by **10** each time.
   - Generates: **10, 20, 30, ..., 200**.

3. **Save and Run**
   - Press **F5**.

---

## **Key Differences**
| Version | Step Calculation | Code Simplicity | Best Use Case |
|---------|-----------------|-----------------|--------------|
| **07_1** | Uses `x` as an independent variable | Simple, but extra variable needed | Beginner-friendly |
| **07_2** | Uses `i` to generate step size dynamically | Removes extra variable | Efficient for fixed calculations |
| **07_3** | Uses `range(start, stop, step)` | Most readable | Best for precise control |

---

### **Key Learning Points**
✅ **Efficiency** – Directly using `i` eliminates extra calculations.  
✅ **Loop Control** – `range(start, stop, step)` **simplifies step size adjustments**.  
✅ **Scalability** – Easily adaptable for different patterns.

These refinements **streamline programming logic**, making Python **more powerful and readable**! 🚀

### **Customizing the Loop with `range()` Parameters**

This section explains how the `range()` function can be used with **one, two, or three parameters** to control loop behavior.

---

### **Understanding `range()` Variations**
1. **One Parameter – Default Counting (`range(n)`)**
   - Example: `range(10)` → Counts **0 to 9** (increments by `1`).
   
2. **Two Parameters – Custom Start (`range(start, stop)`)**
   - Example: `range(5, 15)` → Counts **5 to 14** (increments by `1`).

3. **Three Parameters – Custom Step (`range(start, stop, step)`)**
   - Example: `range(0, 20, 2)` → Counts **0, 2, 4, ..., 18**.
   - Example: `range(200, 0, -10)` → **Counts backward**: **200, 190, ..., 10**.

---

### **Exercises**
1. **Modify `feladat_07_1.py`**
   - Change the **spiral direction** to rotate **right** (`right(90)`) instead of **left**.
   
2. **Draw the Left-side Shape**
   - Use **minimal instructions** (likely a **loop**).

3. **Draw the Middle Shape**
   - Again, **minimize code** using a **loop**.

4. **Draw the Right-side Shape**
   - Use a **loop** for efficiency.
   - If needed, **calculate diagonal lengths** (hint in the footnote).

---

### **Key Learning Points**
✅ **Using `range()` Effectively** – Controls loop **start, stop, and step size**.  
✅ **Loop Direction** – `right(90)` vs. `left(90)`.  
✅ **Minimizing Code** – Efficient use of **loops**.  

This section helps refine Python **looping skills** for **smarter automation**! 🚀

8. Random number

### **8. RANDOM NUMBERS**
This section introduces **random number generation in Python**, which allows programs to behave **unpredictably**, like a dice roll or coin flip.

---

### **Understanding Random Numbers in Python**
- Computers can generate **random values** using Python’s **`random` module**.
- These numbers can be used for **games, simulations, and random selections**.

---

### **9th Example Task – Getting Started with Random Numbers**
1. **Open the Python Shell**
   - Start an interactive session.

2. **Import the `randrange` Function**
   ```python
   from random import randrange
   ```
   - This allows us to **generate random numbers**.

3. **Generate a Random Number (0 to 5)**
   ```python
   randrange(6)
   ```
   - Returns a random number **from 0 to 5**.

4. **Modify for a Dice Roll (1 to 6)**
   ```python
   randrange(6) + 1
   ```
   - Ensures values are **1, 2, 3, 4, 5, or 6** (instead of starting at 0).

5. **Check Results**
   - Run it **multiple times** to see **different values**.

6. **Generate a Random Number in a Custom Range**
   ```python
   randrange(1, 7)
   ```
   - Produces **1 to 6**, like a **dice roll**.
   - `randrange(start, stop)` includes the **start** but **excludes** the stop.

---

### **Key Learning Points**
✅ **Randomness in Python** – `randrange()` simulates **dice, coins, and more**.  
✅ **Controlling Ranges** – `randrange(a, b)` generates numbers in **[a, b-1]**.  
✅ **Practical Uses** – Can apply to **colors, movement, or random behavior**.  

This section introduces **randomized programming**, useful in **games and simulations**! 🎲🚀

### **10. Example Task – Using Random Numbers in a Program**
This section demonstrates how to use **random numbers** in a Python program to create a **star-like shape** where the lengths of the rays are random.

---

### **Steps to Create the Random Star Shape**
1. **Create a New Program**
   - Open **File → New File**.
   - Save it as **feladat_08_1.py**.

2. **Import `randrange` for Random Numbers**
   ```python
   from random import randrange
   ```
   - This allows us to generate **random numbers**.

3. **Use a Loop to Draw 20 Rays**
   ```python
   for i in range(20):
   ```
   - The loop runs **20 times**, once for each ray.

4. **Generate a Random Length**
   ```python
   x = randrange(0, 200)
   ```
   - The ray length is chosen **randomly between 0 and 199**.

5. **Move Forward and Backward to Draw the Ray**
   ```python
   forward(x)
   backward(x)
   ```
   - Moves forward by **random `x`** and back to the center.

6. **Rotate for the Next Ray**
   ```python
   left(18)
   ```
   - **360° divided by 20 rays = 18° per turn**.

7. **Save and Run**
   - Save and press **F5** to execute.

---

### **Final Python Code**
```python
from turtle import *
from random import randrange

for i in range(20):
    x = randrange(0, 200)  # Random length
    forward(x)
    backward(x)
    left(18)
```

---

### **How It Works**
✅ **Uses `randrange(0, 200)`** to generate a **random length**.  
✅ **Moves forward and back** to **keep the turtle in the center**.  
✅ **Evenly spaces the rays** by rotating **18° each time**.

This introduces **randomness into graphics**, making Python great for **generative art and simulations**! 🚀


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