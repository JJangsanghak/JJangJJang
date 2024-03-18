Python 3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def get_radisu(prompt):
...     r=int(input(prompt))
...     return r
... 
>>> def get_radius(prompt):
...     r=int(input(prompt))
...     return r
... 
>>> get_radius('넓이를 구하고자 하는 원의 반지름은?')
넓이를 구하고자 하는 원의 반지름은?4
4
>>> def get_circle_area():
...     r=int(input(넓이를 구하고자 하는 원의 반지름은?)
...           
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> def get_circle_area()
SyntaxError: expected ':'
>>> def get_circle_area():
...     r=int(input('넓이를 구하고자 하는 원의 반지름은?')
...     print('반지름',r,'인 원의 넓이=');return r*r*3.14
...           
SyntaxError: '(' was never closed
>>> def get_circle_area():
...     r=int(input('넓이를 구하고자 하는 원의 반지름은?'))
...     print('반지름',r,'인 원의 넓이=');return r*r*3.14
... 
...     
>>> 
>>> get_circle_area()
넓이를 구하고자 하는 원의 반지름은?4
반지름 4 인 원의 넓이=
50.24
