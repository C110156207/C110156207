# 共同朋友的數量
friend_A = input("請輸入A的好友:").split()
friend_B = input("請輸入B的好友:").split()
x = 0
for i in range(len(friend_A)):
    for j in range(len(friend_B)):
        if friend_A[i] == friend_B[j]:
            x += 1
print(x)