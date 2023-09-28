class Order:
    @staticmethod
    def order_list():
        while True:
            user_name = input("請輸入會員名稱：")
            try:
                # 讀取該用戶的訂單記錄.txt
                f = open(user_name + '.txt')
                text = f.read()
                print(text)
                f.close()
            except IOError:
                print("\n"+"查無此會員訂單記錄")
            check = input("是否繼續查詢用戶訂單記錄？(Y/N)")
            if check == "Y":
                continue
            else:
                break
