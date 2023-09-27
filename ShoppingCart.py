class Product:
    def __init__(self, product_name, product_price, product_stock):
        self.name = product_name
        self.price = product_price
        self.stock = product_stock

    # 將 object 定義為字串(以供後續顯示商品列表使用)，return(結束函式)需回傳字串
    def __str__(self):
        return f"{self.name} NT$ {self.price} 可售數量：{self.stock}"

    @staticmethod
    def product_list():
        product_list = [
            Product("阿極", 50, 10),
            Product("胖達", 40, 9),
            Product("大大", 30, 8)
        ]

        user_name = input("請輸入會員名稱：")
        print("商品列表".center(20, "-"))
        for i in range(len(product_list)):
            print(product_list[i])

        while True:
            product_name = input("請輸入訂購的商品名稱：")
            # product 為自定義內容；product.name 指的是 Product.self.name
            product_mapping = list(filter(lambda product: product.name == product_name, product_list))
            if len(product_mapping) > 0:
                # 透過 product_mapping 將 {product_name} 的可售數量格式轉為 int
                product_stock = int(product_mapping[0].stock)
                product_amount = int(input("請輸入購買數量："))
                if product_amount <= 0:
                    print("購買數量不可 ≤ 0")
                elif product_amount <= product_stock:
                    print(f"[{product_amount}個 {product_name}] 已成功加入購物車！")
                else:
                    print(f"[{product_name}] 可售數量為{product_stock}，請重新訂購！")
            elif product_name == "exit":
                break
            else:
                print("查無此商品")
            check = input("是否繼續訂購商品？(Y/N)")
            if check == "Y":
                continue
            else:
                break
