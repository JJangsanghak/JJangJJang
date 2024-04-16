def read_single_digit(a):
    if a==1:
        return '일'
    elif a==2:
        return '이'
    elif a==3:
        return '삼'
    elif a==4:
        return '사'
    elif a==5:
        return '오'
    elif a==6:
        return '육'
    elif a==7:
        return '칠'
    elif a==8:
        return '팔'
    elif a==9:
        return '구'
     
def read_number(b):
    num1=b//100
    num2=(b%100)//10
    num3=b%10
    aa=read_single_digit(num1)
    bb=read_single_digit(num2)
    cc=read_single_digit(num3)
    dd=aa+bb+cc
    return dd
def abc():
    num=int(input("세 자리 정수 입력:"))
    c=read_number(num)
    print(c)
