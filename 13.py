# 迴文問題
x = input("輸入一字元為:")
s = ''
s = x[::-1]
if x == s:
    print("YES")
else:
    print("NO")