# 車資
s1 = 75
s2 = 1.5
s3 = 0.25
total = 0
km = float(input("請輸入路程公里數(km):"))
while True:
    if km <= 1.5:
        total = s1
        print("所需車資為:", total)
        break
    else:
        while km > s2:
            km -= s3
            total += 5
            if km <= s2:
                total = total + s1
                print("所需車資為:", total)
                break
        break