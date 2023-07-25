"""
6025
 a, b = input().split()
c = int(a) + int(b)
print(c) """

"""
6026
 a = input()
b = input()
c = float(a) + float(b)
print(c) """

""" 6027
a= input()
n = int(a)
print('%x'% n) """

""" 6028
a= input()
n = int(a)
print('%X'% n) """

""" 6029
a= input()
n = int(a, 16)
print('%o'% n) """

""" 6030
a = ord(input())
print(a) """

""" 6031
c = int(input())
print(chr(c)) """

""" 6032
a = input()
a = int(a)
print(-a) """

""" 6033
a = ord(input())
print(chr(a+1)) """

""" 6034
a, b = input().split()
a = int(a)
b = int(b)
print(a-b)

a, b = input().split()
a = int(a)
b = int(b)
c = a - b
print(c) """

""" 6035
a, b = input().split()
a = float(a)
b = float(b)
print(a*b)

a, b = input().split()
a = float(a)
b = float(b)
c = a * b
print(c) """

""" 6036
a, b = input().split()
print(a*int(b))

a, b = input().split()
b = int(b)
print(a*b) """

""" 6037
a = input()
b = input()
print(int(a)*b)

a = input()
b = input()
a = int(a)
print(a*b) """

""" 6038
a, b = input().split()
a = int(a)
b = int(b)
print(a**b)

a, b = input().split()
a = int(a)
b = int(b)
c = a**b
print(c) """

""" 6039
a, b = input().split()
a = float(a)
b = float(b)
print(a**b)

a, b = input().split()
a = float(a)
b = float(b)
c = a**b
print(c) """

""" 6040
a, b = input().split()
a = int(a)
b = int(b)
print(a//b) """

""" 6041
a, b = input().split()
a = int(a)
b = int(b)
print(a%b) """

""" 6042
a = input()
a = float(a)
print(format(a, ".2f")) """

""" 6043
a, b = input().split()
a = float(a)
b = float(b)
print(format(a/b, ".3f")) """

""" 6044
a, b = input().split()
a = int(a)
b = int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(format(a/b, ".2f")) """

""" 6045
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
print(a+b+c, format((a+b+c)/3, ".2f")) """

""" 6046
a = input()
a = int(a)
print(a*2)

a = input()
a = int(a)
print(a<<1) """

""" 6047
a, b = input().split()
a = int(a)
b = int(b)
print(a*(2**b)) """

""" 6048
a, b = input().split()
a = int(a)
b = int(b)
print(a<b) """

""" 6049
a, b = input().split()
a = int(a)
b = int(b)
print(a==b) """

""" 6050
a, b = input().split()
a = int(a)
b = int(b)
print(b>=a) """

""" 6051
a, b = input().split()
a = int(a)
b = int(b)
print(a!=b) """

""" 6052
a = int(input())
print(bool(a)) """

""" 6053
a = bool(int(input()))
print(not a) """

""" 6054
a, b = input().split()
print(bool(int(a)) and bool(int(b))) """

""" 6055
a, b = input().split()
print(bool(int(a)) or bool(int(b))) """

""" 6056
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((c and (not d)) or ((not c) and d)) """

""" 6057
a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print(a==b) """

""" 6058
a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print(not(a or b)) """

""" 6059
a = int(input())
print(~a) """

""" 6060
a, b = input().split()
a = int(a)
b = int(b)
print(a&b) """

""" 6061
a, b = input().split()
a = int(a)
b = int(b)
print(a|b) """

""" 6062
a, b = input().split()
a = int(a)
b = int(b)
print(a^b) """

""" 6063
a, b = input().split()
a = int(a)
b = int(b)
print(a if (a>=b) else b) """

""" 6064
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
print((a if a<b else b) if ((a if a<b else b)<c) else c) """

""" 6065
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a%2==0 :
    print(a)
if b%2==0 :
    print(b)
if c%2==0 :
    print(c) """

""" 6066
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a%2==0 :
    print("even")
else :
    print("odd")
if b%2==0 :
    print("even")
else :
    print("odd")
if c%2==0 :
    print("even")
else :
    print("odd") """

""" 6067
a = int(input())
if a<0 : 
    if a%2==0 :
        print("A")
    else :
        print("B")
else :
    if a%2==0 :
        print("C")
    else :
        print("D") """

""" 6068
a = int(input())
if a >= 90 :
    print('A')
else :
    if a>=70 :
        print('B')
    else :
        if a>=40 :
            print('C')
        else :
            print('D') """

""" 6069
a = input()
if a == 'A' :
    print('best!!!')
else :
    if a == 'B' :
        print('good!!')
    else :
        if a == 'C' :
            print('run!')
        else :
            if a == 'D' :
                print('slowly~')
            else :
                print('what?') """

""" 6070
a = int(input())
if a//3==1 :
    print("spring")
elif a//3==2 :
    print("summer") 
elif a//3==3:
    print("fall")
else :
    print("winter")

a = int(input())
if (a == 12 or a == 1 or a == 2) :
    print("winter")
elif (a == 3 or a == 4 or a == 5) :
    print("spring")
elif (a == 6 or a == 7 or a == 8) :
    print("summer")
else :
    print("fall") """

""" 6071
while True:
    a=input()
    a=int(a)
    if a==0:
        break
    else:
        print(a) """

""" 6072
a = int(input())
while a!=0:
    print(a)
    a=a-1 """

""" 6073
a = int(input())
while a!=0 :
    a-=1
    print(a) """

""" 6074
a = ord(input())
b = ord('a')
while b<=a :
    print(chr(b), end=' ')
    b+=1 """

""" 6075
a = int(input())
b = 0
while b<=a :
    print(b)
    b+=1 """

""" 6076
a = int(input())
for i in range(a+1) :
    print(i) """

""" 6077
n = int(input())
sum = 0
for i in range(1, n+1) :
    if i%2==0:
        sum=sum+i
print(sum) """

""" 6078
while True :
    a = input()
    print(a)
    if a == 'q' :
        break """

""" 6079
a = int(input())
b = 0
c = 0
while b < a :
    c += 1
    b += c
print(c) """


""" 6080
a, b = input().split()
a = int(a)
b = int(b)
for i in range(1, a+1) :
    for j in range(1, b+1) :
        print(i, j) """

""" 6081
n = int(input(), 16)

for i in range(1, 16) :
  print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='') """

""" 6082
n = int(input())
for i in range(1, n+1) :
    if i%10==3 or i%10==6 or i%10==9 :
        print("X", end=' ')
    else :
        print(i, end=' ') """


r, g, b = map(int, input().split())
for i in range(0, r) :
    for j in range(0,g) :
        for k in range(0, b) :
            print(i, j, b) 

print(r*g*b)
