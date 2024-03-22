def get_integer(prompt):
    return int(input(prompt))

def exchange(a):
    n1=a//500
    a%=500
    n2=a//100
    a%=100
    n3=a//50
    a%=50
    n4=a//10
    print("500원 동진의 개수:",n1);print("100원 동전의 개수:",n2);print("50원 동전의 개수:",n3);print("10원 동전의 개수:",n4)

