auto increment = [](auto x, int y = 1) { return x + y; };

increment(10);     // returns 11 (uses default y = 1)
increment(10, 5);  // returns 15 (uses provided y = 5)
