Python 3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def get_integer(prompt):
...     return int(input(prompt))
... 
>>> def exchange(a):
...     n1=a//500
...     a%=500
...     n2=a//100
...     a%=100
...     n3=a//50
...     a%=50
...     n4=a//10
...     print("500원 동진의 개수:",n1);print("100원 동전의 개수:",n2);print("50원 동전의 개수:",n3);print("10원 동전의 개수:",n4)
... 
...     
>>> a=get_integer("동전으로 교환하고자 하는금액은?")
동전으로 교환하고자 하는금액은?3520
>>> exchange(a)
500원 동진의 개수: 7
100원 동전의 개수: 0
50원 동전의 개수: 0
10원 동전의 개수: 2
