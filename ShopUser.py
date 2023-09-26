class User:
    def __init__(self, name, birthday, level, phone, address):
        self.name = name
        self.birthday = birthday
        self.level = level
        self.phone = phone
        self.address = address

    def user_drive(self):
        print(f"會員名稱：{self.name} \n"
              f"生日：{self.birthday} \n"
              f"會員等級：{self.level} \n"
              f"手機號碼：{self.phone} \n"
              f"地址：{self.address}")

    @staticmethod
    def user_mapping():
        user_list = [
            User("Evonne", 19970421, "VIP會員", "0911222333", "台北市大安區"),
            User("Ning", 19950315, "一般會員", "0955666777", "新北市汐止區")
        ]

        while 2:
            search_user = input("請輸入會員名稱：")
            # username 為自定義內容；username.name 指的是 User.會員名稱
            user_name_list = list(filter(lambda username: username.name == search_user, user_list))
            if len(user_name_list) > 0:
                user_name_list[0].user_drive()
            else:
                print("查無此會員")
            check = input("是否繼續查詢用戶資料？(Y/N)")
            if check == "Y":
                continue
            else:
                break
