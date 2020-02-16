# fypy
Function composition in python in under 20 lines of code.

## How to use:
The Fy class is callable and stores a list of callable functions.
Two functions, x() and y(), can be combined into one function f() by doing `f = (Fy() | x | y)`.
You can chain functions toghether and apply an input i like `(Fy() | x | y | z | w)(i)`.
Since Fy chains callables, you can chain multiple Fys toghether.
If a function in the chain returns a NoneType, the output from the previous function is carried over, so you can, for example, print the result in the middle of a chain like `(Fy() | x | print | y | print | z)(i)`.