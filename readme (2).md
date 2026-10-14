# Module 5: APIs You Use

This module is about using tools that Python already provides, and
learning how to work with tools made by other people.

# 1. The idea: call / arguments / result / failure --- what you do not need to know

An **API** is a way for one piece of program to ask another piece of
program to do something or it simply means one program communicating with another program.

Think of using a calculator: - **Call:** You ask the calculator to do
something for example addition. - **Arguments:** The values you give it for example 1+1. - **Result:** The
answer it gives back for example 2. - **Failure:** Something goes wrong, such as
giving it an invalid value for example since caculator deals with integer if users input a string it will throw an error.

You actually do not need to know how a tool was built inside or how it works inside. You
need to know what it does, what information your expects, what it returns,
and what errors it can raise.

# 2. Language and standard-library APIs: docs, return values, and exceptions

In Python, the standard library is a collection of built-in modules that provide useful tools for your programs. You usually don't need to install them separately because they come with Python.

Examples: - `pathlib` helps you work with file and folder paths. -
`datetime` helps you work with dates and times. - `json` helps you save
and read data in JSON format.

For example, opening a file that does not exist can cause a
`FileNotFoundError`. Knowing that helps you decide how to handle the
problem.

# 3. System-ish APIs: talking to the computer and other programs

These are tools that let your Python program interact with the computer
or another program.



