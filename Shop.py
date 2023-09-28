import ShopUser
import ShoppingCart
import OrderManagement

while 1:
    ChooseFunction = input("[購買商品] [查看用戶資料] [查看訂單紀錄] [結束服務] \n"
                           "請輸入服務項目：")
    if ChooseFunction == "查看用戶資料":
        ShopUser.User.user_mapping()
    elif ChooseFunction == "購買商品":
        ShoppingCart.Product.shopping()
    elif ChooseFunction == "查看訂單紀錄":
        OrderManagement.Order.order_list()
    elif ChooseFunction == "結束服務":
        print("感謝您的使用！❤ ︎❤ ︎❤")
        exit()
    else:
        print("暫無此服務，請重新輸入！")
