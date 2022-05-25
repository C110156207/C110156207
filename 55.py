# 借閱書籍
list1 = ['飢餓遊戲3','解憂雜貨店','怪獸與牠們的產地','哈利波特6','我的阿富汗筆友','祈念之樹','樓下的房客','小王子']
list2 = ['房思琪的初戀樂園','等一個人咖啡','鬼滅之刃14','神農嘗百草','麥田捕手','老人與海','傲慢與偏見','與神同行']
book = input("請輸入欲租借的書籍:")
if book in list1:
    for i in range(len(list1)):
        if book == list1[i]:
            print("在書架A的第%d本" % (i+1))
elif book in list2:
    for i in range(len(list2)):
        if book == list2[i]:
            print("在書架B的第%d本" % (i+1))
else:
    print("查無此書籍")