# 母音轉換
eng = input("請輸入一串小寫英文:")
for i in eng:
    if i == 'a' :
        eng = eng.replace(i,'.')
    elif i == 'e':
        eng = eng.replace(i,'.')
    elif i == 'i':
        eng = eng.replace(i,'.')
    elif i == 'o':
        eng = eng.replace(i,'.')
    elif i == 'u':
        eng = eng.replace(i,'.')
print(eng)