import ShopUser

ProductList = [
    {"Name": "阿極", "Price": 50, "Stock": 10},
    {"Name": "胖達", "Price": 40, "Stock": 9},
    {"Name": "大大", "Price": 30, "Stock": 8}
]

while 1:
    ChooseFunction = input("[購買商品] [查看用戶資料] [查看訂單紀錄] [結束服務] \n"
                           "請輸入服務項目：")
    if ChooseFunction == "查看用戶資料":
        ShopUser.User.user_mapping()
    elif ChooseFunction == "結束服務":
        print("感謝您的使用！❤︎❤︎❤︎")
        exit()
    else:
        print("暫無此服務，請重新輸入！")
