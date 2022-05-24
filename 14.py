# 輸入字串算字元
x = input("輸入一字串為:")
s = 0
for i in range(len(x)):
    s += 1
print('There are %d characters' % (s))