
### Chapter 5: Runtime Polymorphism in C++

#### Introduction  
Polymorphism is one of the fundamental pillars of Object-Oriented Programming (OOP), alongside encapsulation and inheritance. The word *polymorphism* means "many forms." In C++, polymorphism allows objects to behave differently based on their actual derived type, even when accessed through a pointer or reference to a base type.  

There are two kinds of polymorphism in C++:
1. Compile-time polymorphism (function overloading, operator overloading, templates)
2. **Runtime polymorphism (using virtual functions)**  

This chapter focuses on **runtime polymorphism**, which is achieved through inheritance and virtual functions. At runtime, the correct function for an object is called using dynamic dispatch, depending on the type of object the pointer or reference is pointing to.  

---

#### Basic Concepts of Runtime Polymorphism  
Runtime polymorphism in C++ works through three core mechanisms:
- Inheritance (base and derived classes)
- Virtual functions (functions declared with the `virtual` keyword in the base class)
- Dynamic binding (deciding at runtime which function to call)

When you declare a function as `virtual` in the base class, and then override it in derived classes, calling that function through a base-class pointer or reference will invoke the derived class's implementation, based on the actual object type.  

---

#### Syntax Example:  

```cpp
#include <iostream>
using namespace std;

class Animal {
public:
    virtual void sound() {
        cout << "Animal makes a sound" << endl;
    }
};

class Dog : public Animal {
public:
    void sound() override {
        cout << "Dog barks" << endl;
    }
};

class Cat : public Animal {
public:
    void sound() override {
        cout << "Cat meows" << endl;
    }
};

int main() {
    Animal* animalPtr;
    Dog dog;
    Cat cat;

    animalPtr = &dog;
    animalPtr->sound(); // Output: Dog barks

    animalPtr = &cat;
    animalPtr->sound(); // Output: Cat meows

    return 0;
}
```

---

#### How it works under the hood  
When a class has virtual functions, the compiler creates something called a **vtable** (virtual table). This is an internal structure that holds function pointers for each virtual function. Each object that uses virtual functions has a hidden pointer to the vtable (often called a vptr). At runtime, when you call a virtual function through a pointer or reference, the program looks up the actual function from the vtable.  

---

#### The Role of the `virtual` Keyword  
Declaring a function `virtual` in the base class tells the compiler to use dynamic dispatch. Without `virtual`, the call would be resolved at compile time, and it would call the base class function regardless of the object type.  

**Example without virtual:**

```cpp
class Animal {
public:
    void sound() { // not virtual
        cout << "Animal makes a sound" << endl;
    }
};

class Dog : public Animal {
public:
    void sound() {
        cout << "Dog barks" << endl;
    }
};

int main() {
    Animal* a;
    Dog d;
    a = &d;
    a->sound(); // Output: Animal makes a sound (not dynamic)
}
```

---

#### The `override` and `final` specifiers  
Modern C++ (C++11 and beyond) introduced two useful keywords:
- `override` — ensures that the derived class function is actually overriding a virtual function from the base class. If it doesn't match any base class virtual function, the compiler gives an error.
- `final` — prevents further overriding of a virtual function in derived classes.  

**Example:**

```cpp
class Animal {
public:
    virtual void sound() const {
        cout << "Animal sound" << endl;
    }
};

class Dog : public Animal {
public:
    void sound() const override final {
        cout << "Dog barks" << endl;
    }
};

// class Puppy : public Dog {
// public:
//     void sound() const override { // Error: sound() is final in Dog
//         cout << "Puppy squeaks" << endl;
//     }
// };

```

---

#### Pure Virtual Functions and Abstract Classes  
If a virtual function is set to `= 0`, it becomes a **pure virtual function**, and the class containing it becomes an **abstract class**. You cannot instantiate abstract classes; they serve as interfaces for derived classes.

**Example:**

```cpp
class Shape {
public:
    virtual void draw() = 0; // pure virtual function
};

class Circle : public Shape {
public:
    void draw() override {
        cout << "Drawing Circle" << endl;
    }
};

int main() {
    // Shape s; // Error: cannot instantiate abstract class
    Circle c;
    c.draw(); // Output: Drawing Circle
}
```

---

#### Runtime Polymorphism with References  
Polymorphism works just as well with references:

```cpp
void makeSound(Animal& a) {
    a.sound();
}

Dog d;
Cat c;
makeSound(d); // Output: Dog barks
makeSound(c); // Output: Cat meows
```

---

#### Destructors and Polymorphism  
When using inheritance and polymorphism, it’s critical to make destructors in base classes virtual. If you delete a derived object through a base pointer without a virtual destructor, only the base destructor will be called, leading to resource leaks.

**Example:**

```cpp
class Base {
public:
    virtual ~Base() {
        cout << "Base destructor" << endl;
    }
};

class Derived : public Base {
public:
    ~Derived() {
        cout << "Derived destructor" << endl;
    }
};

int main() {
    Base* ptr = new Derived();
    delete ptr; // Both Derived and Base destructors called
}
```

Without a virtual destructor, only `Base`'s destructor would run, and the `Derived` part of the object wouldn't be cleaned up properly.

---

#### Advantages of Runtime Polymorphism  
- **Extensibility:** You can write flexible code that works for a family of related objects without changing the calling code.
- **Maintainability:** New classes and behaviors can be added without changing the existing logic.
- **Dynamic behavior:** The exact function call depends on the object type at runtime.

---

#### Disadvantages of Runtime Polymorphism  
- **Slight performance overhead** due to vtable lookups and dynamic dispatch.
- **More complex debugging**, as calls may not be easily traceable.
- **Memory overhead**, because each object may need additional space for the vptr.

---

#### Conclusion  
Runtime polymorphism is a powerful tool that allows your programs to be dynamic and flexible. Using virtual functions, base and derived classes, and dynamic dispatch, C++ lets you write code that is adaptable to future changes. While there are some costs involved, the benefits far outweigh them in large, complex applications. It also forms the basis for design patterns, like the Factory, Strategy, and Visitor patterns, that rely on dynamic object behavior.  

By mastering runtime polymorphism, you open the door to writing scalable, maintainable, and elegant C++ code that can grow along with your projects.

---

Here’s a **C++ Runtime Polymorphism Cheatsheet** you can use for quick reference:  

---

## ✅ C++ Runtime Polymorphism Cheatsheet

---

### 1. **Key Concepts**  
| Concept                | Description                                                              |
|------------------------|--------------------------------------------------------------------------|
| Polymorphism           | "Many forms" — one interface, multiple behaviors.                        |
| Runtime polymorphism   | Behavior determined at runtime via virtual functions and dynamic binding.|
| Virtual table (vtable) | Internal lookup table used by the compiler for dynamic dispatch.         |
| vptr                   | Pointer inside the object that points to the vtable.                    |

---

### 2. **Basic Syntax**  

```cpp
class Base {
public:
    virtual void func();   // Virtual function
};

class Derived : public Base {
public:
    void func() override;  // Overrides base virtual function
};

Base* ptr = new Derived;
ptr->func();  // Calls Derived::func() dynamically
```

---

### 3. **Virtual Functions**  
| Keyword   | Purpose                                                               |
|-----------|-----------------------------------------------------------------------|
| `virtual` | Declares a function for dynamic dispatch.                             |
| `override`| Ensures correct overriding of base class virtual functions.           |
| `final`   | Prevents further overriding of a virtual function in derived classes. |

---

### 4. **Pure Virtual Functions / Abstract Classes**  

```cpp
class Interface {
public:
    virtual void display() = 0; // Pure virtual function
};
```
> Abstract classes cannot be instantiated — they serve as base interfaces.

---

### 5. **Virtual Destructor**  
```cpp
class Base {
public:
    virtual ~Base(); // Always use virtual destructor in polymorphic base classes
};
```

> Ensures proper cleanup when deleting derived objects through base pointers.

---

### 6. **Calling Virtual Functions through References**  

```cpp
void callSound(Animal &a) {
    a.sound(); // dynamic call
}
```

---

### 7. **Pitfalls to Avoid**  
| Mistake                    | Consequence                                                        |
|----------------------------|--------------------------------------------------------------------|
| Forgetting `virtual`       | Function call resolved at compile-time instead of runtime.         |
| No virtual destructor      | Leads to resource leaks when deleting derived object via base ptr. |
| Incorrect override spelling| Without `override`, easy to silently introduce bugs.               |

---

### 8. **Quick Example Recap**  

```cpp
class Animal {
public:
    virtual void sound() { cout << "Animal sound\n"; }
};

class Dog : public Animal {
public:
    void sound() override { cout << "Dog barks\n"; }
};

Animal* a = new Dog();
a->sound(); // Output: Dog barks
```

---

### 9. **Pros and Cons**  

| Pros                         | Cons                                |
|------------------------------|-------------------------------------|
| Extensible code design       | Slight runtime performance overhead |
| Easier maintenance           | Harder to debug                    |
| Dynamic behavior at runtime  | Requires careful destructor design  |

---

### 10. **Summary**  
✅ Use `virtual` for dynamic dispatch.  
✅ Use `override` and `final` for safer, cleaner code.  
✅ Always make base class destructors `virtual`.  
✅ Use runtime polymorphism to write flexible, extensible, and scalable applications.  

 
