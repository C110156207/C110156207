# 吃兵數
m, s = input("請輸入遊戲時間:").split(':')
m = int(m)*60
s = int(s)
time = m + s
round = time//30
s = 0
for i in range(1, round-1):
    if i % 3 == 0:
            if i % 2 == 0:
                s += 6
            else:
                s += 7
    else:
        if i % 2 == 0:
            s += 5
        else:
            s += 6
print(str(s)+'隻兵')  