'''
#Python Architecture

    it explains how Python code is executed internally by the Python Interpreter.

Python does NOT directly convert code to machine language like C.
Instead, it uses an interpreter + bytecode + virtual machine.

High-Level View of Python Architecture

Python Source Code (.py)
        ↓
   Python Interpreter
        ↓
   Bytecode (.pyc)
        ↓
 Python Virtual Machine (PVM)
        ↓
     Output

#Python Source Code (.py) : are the python files which we are writing the code 
     
# Python Interpreter
    The Python Interpreter is the heart of Python.

#What does the interpreter do?
It performs two main steps:
Compilation (Syntax Check)
Checks for syntax errors
Converts source code into bytecode
Bytecode is not machine code
#If syntax error → execution stops

#Bytecode (.pyc)
After successful compilation, Python creates bytecode.

What is Bytecode?
Intermediate representation
Platform-independent
Stored as .pyc files inside __pycache__

why ??
Faster execution
Reusable
No need to recompile every time


#Python Virtual Machine (PVM)

#What is PVM?
Python Virtual Machine (PVM) executes the bytecode line by line.
PVM is the actual runtime engine of Python.

What PVM does:
Reads bytecode
Converts it to machine instructions
Executes the program

Platform-dependent
Hidden from the user


'''