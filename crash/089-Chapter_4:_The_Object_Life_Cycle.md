## Chapter 4: The Object Life Cycle in C++  

### Introduction  
In C++, objects are fundamental to object-oriented programming (OOP). Understanding how objects are created, used, and destroyed is crucial for writing efficient and error-free code. The **object life cycle** consists of several stages, including creation (construction), usage, and destruction. This chapter explores these stages in detail, discussing constructors, destructors, dynamic memory allocation, and best practices to manage object lifetime effectively.

---

### 4.1 Object Creation and Constructors  

When an object is instantiated, its constructor is automatically invoked to initialize it. C++ provides several types of constructors:  

#### **Default Constructor**  
A default constructor is automatically called when an object is created without any arguments. If no constructor is explicitly defined, the compiler generates a default one.

```cpp
class Car {
public:
    Car() { 
        std::cout << "Car created!" << std::endl; 
    }
};

int main() {
    Car myCar;  // Default constructor is called
    return 0;
}
```

#### **Parameterized Constructor**  
A parameterized constructor allows initializing an object with specific values at creation.

```cpp
class Car {
    std::string model;
public:
    Car(std::string m) : model(m) { 
        std::cout << "Car model: " << model << std::endl;
    }
};

int main() {
    Car myCar("Tesla Model S");
    return 0;
}
```

#### **Copy Constructor**  
The copy constructor initializes a new object using an existing object of the same class.

```cpp
class Car {
    std::string model;
public:
    Car(std::string m) : model(m) {}
    
    // Copy constructor
    Car(const Car& other) : model(other.model) { 
        std::cout << "Copy constructor called for " << model << std::endl;
    }
};

int main() {
    Car car1("Toyota");
    Car car2 = car1; // Copy constructor is called
    return 0;
}
```

#### **Move Constructor (C++11)**  
A move constructor transfers ownership of resources instead of copying them, improving efficiency.

```cpp
class Car {
    std::string model;
public:
    Car(std::string m) : model(std::move(m)) {}
    
    // Move constructor
    Car(Car&& other) noexcept : model(std::move(other.model)) {
        std::cout << "Move constructor called" << std::endl;
    }
};

int main() {
    Car car1("Ford");
    Car car2 = std::move(car1); // Move constructor is called
    return 0;
}
```

---

### 4.2 Object Lifetime and Scope  

The lifetime of an object depends on how it is created and where it is declared.

#### **Automatic (Stack) Storage**  
Objects declared inside a function or block exist until the block ends.

```cpp
void createCar() {
    Car car("Honda"); // Created on the stack
} // car is destroyed here
```

#### **Dynamic (Heap) Storage**  
Dynamically allocated objects persist until explicitly deleted.

```cpp
Car* myCar = new Car("BMW");
// Some operations
delete myCar; // Explicitly destroy the object
```

#### **Static Storage**  
Static objects exist throughout the program's lifetime.

```cpp
class Logger {
public:
    Logger() { std::cout << "Logger initialized!" << std::endl; }
    ~Logger() { std::cout << "Logger destroyed!" << std::endl; }
};

static Logger loggerInstance; // Exists for the entire program duration
```

---

### 4.3 Object Destruction and Destructors  

A destructor is a special member function invoked when an object goes out of scope or is explicitly deleted. It is used to release resources.

```cpp
class Car {
public:
    Car() { std::cout << "Car created!" << std::endl; }
    ~Car() { std::cout << "Car destroyed!" << std::endl; }
};

int main() {
    Car myCar; // Constructor called
} // Destructor called at the end of scope
```

For dynamically allocated objects, destructors must be explicitly called using `delete`.

```cpp
Car* carPtr = new Car();
delete carPtr; // Destructor is invoked
```

#### **Virtual Destructors**  
In polymorphic classes, destructors should be declared virtual to ensure proper cleanup.

```cpp
class Base {
public:
    virtual ~Base() { std::cout << "Base destructor" << std::endl; }
};

class Derived : public Base {
public:
    ~Derived() { std::cout << "Derived destructor" << std::endl; }
};

int main() {
    Base* obj = new Derived();
    delete obj; // Calls both destructors
    return 0;
}
```

---

### 4.4 Managing Object Lifetime with Smart Pointers  

C++11 introduced **smart pointers** to automatically manage dynamic objects and prevent memory leaks.

#### **Unique Pointer (`std::unique_ptr`)**  
A `std::unique_ptr` ensures sole ownership of an object.

```cpp
#include <memory>

std::unique_ptr<Car> carPtr = std::make_unique<Car>("Audi");
```

#### **Shared Pointer (`std::shared_ptr`)**  
A `std::shared_ptr` allows multiple pointers to share ownership of an object.

```cpp
#include <memory>

std::shared_ptr<Car> car1 = std::make_shared<Car>("Mercedes");
std::shared_ptr<Car> car2 = car1; // Shared ownership
```

#### **Weak Pointer (`std::weak_ptr`)**  
A `std::weak_ptr` avoids circular references in `std::shared_ptr`.

```cpp
#include <memory>

std::weak_ptr<Car> weakCarPtr = car1;
```

---

### 4.5 Object Slicing and Lifetime Considerations  

#### **Object Slicing**  
Object slicing occurs when an object of a derived class is assigned to a base class object, losing derived-specific attributes.

```cpp
class Base {
public:
    int x;
};

class Derived : public Base {
public:
    int y;
};

int main() {
    Derived d;
    d.x = 10; d.y = 20;
    
    Base b = d; // Object slicing: `y` is lost
}
```

#### **Dangling Pointers and Memory Leaks**  
Failing to delete dynamically allocated memory results in memory leaks.

```cpp
void createMemoryLeak() {
    int* ptr = new int(10);
} // `ptr` is lost, memory leak occurs
```

#### **Best Practices to Prevent Leaks**  
- Always use **smart pointers** instead of raw `new/delete`.
- Use **RAII (Resource Acquisition Is Initialization)**.
- Avoid **unnecessary heap allocation**.
- **Explicitly manage** object lifetimes with `delete` or smart pointers.

---

### 4.6 Conclusion  

The object life cycle in C++ is a critical concept that governs how objects are created, managed, and destroyed. Properly understanding constructors, destructors, dynamic memory allocation, and smart pointers ensures efficient memory usage and avoids common pitfalls like memory leaks and dangling pointers. By adhering to best practices, developers can write robust and maintainable C++ programs.