import json

from .Storage import Storage
from .Product import Product
from .Printer import Printer

from config import path_to_save_basket


printer = Printer()
shop = Storage
item = Product()

class Cash_register(Storage):
        
   # __init__ cash register
    def __init__(self, name: str, money: int) -> None:

        self.name = name
        self.money = money
    
    def scan(self, barcode: int) -> None:
        print("Scanning")
        product = item.get_product(barcode)


        product = str(product).replace("[", "")
        product = str(product).replace("]", "")
        
        shop.append_product_to_basket(1, product)
        
        print("Scanned", product)

        # shop.read_basket_element(1, product)



    def remove(self, barcode: int) -> None:
        product = item.get_product(barcode)
        shop.basket.remove(product)


    def cancel(self) -> None:
        shop.basket.clear()

    def purchashe(self) -> None:
        
        printer.basket = shop.basket
        printer.receipt()
    
    def test(self) -> None:
        print(shop.basket)

    