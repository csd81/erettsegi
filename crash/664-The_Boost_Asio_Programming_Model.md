    The Boost Asio Programming Model
                   In the Boost programming model, an I/O context object abstracts the oper-
                   ating system interfaces that handle asynchronous data processing. This
                   object is a registry for I/O objects, which initiate asynchronous operations.
                   Each object knows its corresponding service, and the context object medi-
                   ates the connection.

        NOTE       All Boost Asio classes appear in the <boost/asio.hpp> convenience header.

                       Boost Asio defines a single service object, boost::asio::io_context. Its
                   constructor takes an optional integer argument called the concurrency hint,
                   which is the number of threads the io_context should allow to run concur-
                   rently. For example, on an eight-core machine, you might construct an
                   io_context as follows:

                   boost::asio::io_context io_context{ 8 };

                       You’ll pass the same io_context object into the constructors of your I/O
                   objects. Once you’ve set up all your I/O objects, you’ll call the run method on
                   the io_context, which will block until all pending I/O operations complete.
                       One of the simplest I/O objects is the boost::asio::steady_timer, which
                   you can use to schedule tasks. Its constructor accepts an io_context object
                   and an optional std::chrono::time_point or std::chrono_duration. For example,
                   the following constructs a steady_timer that expires in three seconds:

                   boost::asio::steady_timer timer{
                      io_context, std::chrono::steady_clock::now() + std::chrono::seconds{ 3 }
                   };

                        You can wait on the timer with a blocking or a non-blocking call. To
                   block the current thread, you use the timer’s wait method. The result is
                   essentially similar to using std::this_thread::sleep_for, which you learned
                   about in “Chrono” on page 387. To wait asynchronously, you use the
                   timer’s async_wait method. This accepts a function object referred to as a
                   callback. The operating system will invoke the function object once it’s time
                   for the thread to wake up. Due to complications arising from modern oper-
                   ating systems, this might or might not be due to the timer’s expiring.
                        Once a timer expires, you can create another timer if you want to
                   perform an additional wait. If you wait on an expired timer, it will return
                   immediately. This is probably not what you intend to do, so make sure you
                   wait only on unexpired timers.
                        To check whether the timer has expired, the function object must accept
                   a boost::system::error_code. The error_code class is a simple class that represents

664   Chapter 20
operating system–specific errors. It converts implicitly to bool (true if it repre-
sents an error condition; false otherwise). If the callback’s error_code evaluates
to false, the timer expired.
     Once you enqueue an asynchronous operation using async_wait, you’ll
call the run method on your io_context object because this method blocks
until all asynchronous operations are complete.
     Listing 20-1 illustrates how to construct and use timers for blocking and
non-blocking waits.

#include <iostream>
#include <boost/asio.hpp>
#include <chrono>

boost::asio::steady_timer make_timer(boost::asio::io_context& io_context) { u
  return boost::asio::steady_timer{
          io_context,
          std::chrono::steady_clock::now() + std::chrono::seconds{ 3 }
  };
}

int main() {
  boost::asio::io_context io_context; v

    auto timer1 = make_timer(io_context); w
    std::cout << "entering steady_timer::wait\n";
    timer1.wait(); x
    std::cout << "exited steady_timer::wait\n";

    auto timer2 = make_timer(io_context); y
    std::cout << "entering steady_timer::async_wait\n";
    timer2.async_wait([] (const boost::system::error_code& error) { z
      if (!error) std::cout << "<<callback function>>\n";
    });
    std::cout << "exited steady_timer::async_wait\n";
    std::cout << "entering io_context::run\n";
    io_context.run(); {
    std::cout << "exited io_context::run\n";
}

entering steady_timer::wait
exited steady_timer::wait
entering steady_timer::async_wait
exited steady_timer::async_wait
entering io_context::run
<<callback function>>
exited io_context::run

Listing 20-1: A program using boost::asio::steady_timer for synchronous and asynchro-
nous waiting

     You define the make_timer function for building a steady_timer that expires
in three seconds u. Within main, you initialize your program’s io_context v
and construct your first timer from make_timer w. When you call wait on this

                                                     Network Programming with Boost Asio   665
                   timer x, the thread blocks for three seconds before proceeding. Next, you
                   construct another timer with make_timer y, and then you invoke async_wait
                   with a lambda that prints <<callback_function>> when the timer expires z.
                   Finally, you invoke run on your io_context to begin processing operations {.


