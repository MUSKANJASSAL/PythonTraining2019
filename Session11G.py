CCode = """
#include <stdio.h>
int main()
{
    printf("Hello, World!");
    return 0;
}
"""
print(CCode)
print(type(CCode))

file = open("C:/Users/vb/Desktop/Training/Python/Auribises/FILES/MyApp.c", "w")
file.write(CCode)
file.close()

print(">> C Code Written")


cppCode = """
#include<iostream>
using namespace std;
int main(){
    cout<<"Hello World";
    return 0;
}
"""

print(cppCode)
print(type(cppCode))

file = open("C:/Users/vb/Desktop/Training/Python/Auribises/FILES/MyApp.cpp", "w")
file.write(cppCode)
file.close()

print(">> CPP Code Written")


javaCode = """
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World");
    }
}
"""

print(javaCode)
print(type(javaCode))

file = open("C:/Users/vb/Desktop/Training/Python/Auribises/FILES/MyApp.java","w")
file.write(javaCode)
file.close()

print(">> JAVA Code Written")

pythonCode = """
print("Hello World!")
"""

print(pythonCode)
print(type(pythonCode))

file = open("C:/Users/vb/Desktop/Training/Python/Auribises/FILES/MyApp.py","w")
file.write(pythonCode)
file.close()

print(">> Python Code Written")


goCode = """
package main

import "fmt"

// this is a comment

func main() {
    fmt.Println("Hello World")
}
"""
print(goCode)
print(type(goCode))

file = open("C:/Users/vb/Desktop/Training/Python/Auribises/FILES/MyApp.go","w")
file.write(goCode)
file.close()

print(">> Go Code Written")

scalaCode = """
object HelloWorld {
   /* This is my first java program.  
   * This will print 'Hello World' as the output
   */
   def main(args: Array[String]) {
      println("Hello, world!") // prints Hello World
   }
}
"""

print(scalaCode)
print(type(scalaCode))

file = open("C:/Users/vb/Desktop/Training/Python/Auribises/FILES/MyApp.scala","w")
file.write(scalaCode)
file.close()

print(">> Scala Code Written")


dartCode = """
void main() => print('Hello, World!');
"""
print(dartCode)
print(type(dartCode))

file = open("C:/Users/vb/Desktop/Training/Python/Auribises/FILES/MyApp.dart","w")
file.write(dartCode)
file.close()

print(">> Dart Code Written")


"""
print("Options Available are:")
print("1. Hello World in C language")
print("2. Hello World in C++ language")
print("3. Hello World in JAVA language")
print("4. Hello World in PYTHON language")
print("5. Hello World in GO language")
print("5. Hello World in SCALA language")
print("6. Hello World in DART language")
choice = input("Enter your choice:")
if choice == 1:
"""


# HW: Create Hello World Programs in
# 10 different computer programming languages
# Ruby, Dart, Kotlin, Scala, JS, Go

# PS: If you can use Inheritance RTP that will be more effective