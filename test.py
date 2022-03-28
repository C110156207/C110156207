print("Hollw world")
a=65
a=a+10
print(a)
if a>=60:
    print("pass")
elif a<60:
    print("fail")


b=2003
c=1
d=18
sum1=b//1000+b%1000//100+b%100//10+b%10
sum2=d//10+d%10
sum=sum1+sum2+c
print(sum)
if sum > 10:
    print(sum%10+sum//10)
elif sum < 10:
    print(sum)

a='20030118'
sum=0
for i in a:
    sum=sum+int(i)
if sum>=10:
    sum=sum//10+sum%10
elif sum<10:
    sum=sum//10+sum%10
print(sum)


x=0
for i in range(1,11,2):
    x=x+i
for j in range(2,11,2):
    x=x-j
print(x)

x=0
for i in range(1,11,2):
    x=x+i-(i+1)

x=0
for i in range(1,11,1):
    if i%4==0 or i%4==1:
        x=x+i
    elif i%4!=0 or i%4!=1:
        x=x-i
print(x)

x=0
for i in range(1,11,2):
    x= x + 1/i - (1 / (i+1))
print(x)

e = 0
for i in range(2,11,1):
    if i%2==0:
        e-=(i-1)/i
    else:
        e+=(i-1)/i
e+=1
print(e)

x=0
for i in range(2,11,2):
    x-=(i-1)/i + i/(i+1)
