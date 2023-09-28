import datetime


class Product:
    def __init__(self, product_name, product_price, product_stock):
        self.name = product_name
        self.price = product_price
        self.stock = product_stock

    # 將 object 定義為字串(以供後續顯示商品列表使用)，return(結束函式)需回傳字串
    def __str__(self):
        return f"{self.name} NT$ {self.price} 可售數量：{self.stock}"

    @staticmethod
    def shopping():
        product_list = [
            Product("阿極", 50, 10),
            Product("胖達", 40, 90),
            Product("大大", 30, 80)
        ]

        cart_list = []
        product_subtotal = []

        user_name = input("請輸入會員名稱：")
        print("\n"+"商品列表".center(20, "-"))
        for i in range(len(product_list)):
            print(product_list[i])

        while True:
            product_name = input("\n"+"請輸入訂購的商品名稱：")
            # good 為自定義內容；good.name 指的是 Product.self.name
            product_mapping = list(filter(lambda good: good.name == product_name, product_list))
            if len(product_mapping) > 0:
                # 透過 product_mapping 將 {product_name} 的可售數量格式轉為 int
                product_stock = int(product_mapping[0].stock)
                product_amount = int(input("請輸入購買數量："))
                if product_amount <= 0:
                    print("\n"+"購買數量不可 ≤ 0")
                elif product_amount <= product_stock:
                    print("\n"+f"[{product_amount}個 {product_name}] 已成功加入購物車！")
                    # 商品小計計算
                    subtotal = product_mapping[0].price * product_amount
                    # 儲存每筆加入購物車(成功)紀錄
                    cart_list.append(f"{product_name}  {product_mapping[0].price}  {product_amount}  " + str(subtotal))
                    # 儲存商品小計資訊
                    product_subtotal.append(subtotal)
                    # 更新庫存數值
                    product_mapping[0].stock -= product_amount
                else:
                    print("\n"+f"[{product_name}] 可售數量為{product_stock}，請重新訂購！")
            elif product_name == "exit":
                break
            else:
                print("\n"+"查無此商品！")

            check = input("\n"+"是否繼續訂購商品？(Y/N)")
            if check == "Y":
                continue
            else:
                today = datetime.date.today()
                product_total = sum(product_subtotal)

                # 儲存購物紀錄至txt
                with open(user_name + '.txt', "a") as f:
                    f.write("\n")
                    f.write(str(today) + "\n")
                    f.write("本次購物總計：" + str(product_total) + " 元 \n")
                    f.write("名稱 單價 數量 小計 \n")
                    for i in range(len(cart_list)):
                        f.write(cart_list[i] + "\n")

                print("\n" + "購物清單".center(16, "-"))
                print("名稱 單價 數量 小計")
                for i in range(len(cart_list)):
                    print(cart_list[i])
                print("\n"+"本次購物總計：" + str(product_total) + " 元 \n")
                break
