import numpy as np

drink_list = []
food_list = []
product_list = []
list_order = []
class CoffeShop:
    product_list = ["orange juice", "lemonade", "cranberry juice", "pineapple juice", "lemon iced tea", "vanilla chai latte", "hot chocolate", "iced coffee","tuna sandwich", "ham and cheese sandwich", "bacon and egg", "steak", "hamburger", "cinnamon roll"]
    price_list=[1,2,3,4,3,4,6,2,4,5,6,7,4,2]
   
    def __init__(self):
        self.list_order = [] #public variable which is availble
        #self.__list.order = [] #private_variable
       
    @staticmethod
    def addOrder(name_product):
        product_list = CoffeShop.product_list
        if product_list.count(name_product) > 0:
            print("Order added!")
            list_order.append(name_product)
        else:
            print("This item is currently unavailable!")
    
    def listOrders(self):
        print(list_order)
    
    def dueAmount(self):
        totalAmt = 0
        pos = 0
        price_list = CoffeShop.price_list
        for x in list_order:
            pos = CoffeShop.product_list.index(x)
            totalAmt += price_list[pos]
        print(totalAmt)
    
    def cheapestItem(self):
        price_list = CoffeShop.price_list
        product_list = CoffeShop.product_list
        price_list_min = np.min(price_list)
        pos_min = 0
        pos_min = price_list.index(price_list_min)
        print(product_list[pos_min])
        
tcs = CoffeShop()
tcs.addOrder("cinnamon roll")
tcs.addOrder("iced coffee")
tcs.listOrders()  
tcs.dueAmount()
tcs.cheapestItem()
        