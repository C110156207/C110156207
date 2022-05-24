# 星座查詢
month, day = input("請輸入月及日:").split() 
list1 = ["",31,28,31,30,31,30,31,31,30,31,30,31]
list2 = ["",21,19,21,21,22,22,23,24,24,24,23,22]
list3 = ["摩羯座(Capricorn)","水瓶座(Aquarius)","雙魚座(Pisces)","牡羊座(Aries)","金牛座(Taurus)","雙子座(Gemini)","巨蟹座(Cancer)","獅子座(Leo)","處女座(Virgo)","天秤座(Libra)","天蠍座(Scorpio)","射手座(Sagittarius)","摩羯座(Capricorn)"]
month = int(month) ; day = int(day)
if 0 <= month and month <= 12 :
    if 0 <= day and day <= list1[month]:
        if day < list2[month]:
            print("星座為:", list3[month-1])
        else:
            print("星座為:", list3[month])