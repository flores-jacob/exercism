#include <string>
#include <iostream>
// original code, error is: hello_world_test.cpp:(.text+0x56a): undefined reference to `hello_world::hello()'
// Question
// 1. why doesn't this work? Is it a boost/testing framework related issue? Or something's wrong with the code?
/**
std::string hello()
{
    std::string mystring;

    mystring = "Hello, World!";

    return mystring;

};
**/

// new working code

// More questions
// 1. Is it always necessary to encapsulate functions in a namespace?
// 2. Is namespace encapsulation not required but best practice?
// 3. Does the namespace need to have the same name as its *.cpp file?
// 4. How about multiple namespaces in a single *.cpp file?
// 5. Maybe namespace encapsulation really isn't needed, and we simply need it for the Boost testing framework?

const bool DEBUGGING = false;

namespace hello_world {
  std::string hello() {
    // just to see if it is running
    if (DEBUGGING){
        std::cout<<"Hello";
    }
    return "Hello, World!";
  }
}

