# 求解一元二次方程式
a = int(input("輸入a係數:"))
b = int(input("輸入b係數:"))
c = int(input("輸入c係數:"))

s = (b**2)-(4*a*c)

if s > 0:
    ans = ((b*(-1))+s**0.5)/(2*a)
    ans2 = ((b*(-1))-s**0.5)/(2*a)
    print(int(ans))
    print(int(ans2))
elif s == 0:
    ans = ((b*(-1))+s**0.5)/(2*a)
    print(int(ans))
elif s < 0:
    print(0)
