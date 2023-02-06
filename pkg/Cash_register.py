import time
from pkg.Storage import Storage
from pkg.Product import Product
from pkg.Printer import Printer

from config import path_to_save_basket
from json_formatter import json_formatter

printer = Printer()
shop = Storage
item = Product()

class CashRegister(Storage):
        
   # __init__ cash register
    def __init__(self, name: str, money: int) -> None:

        self.name = name
        self.money = money
    
    def scan(self, barcode: int) -> None:
        print("Scanning ... ")
        time.sleep(1)
        product = item.get_product(barcode)

        shop.append_product_to_basket(1, product)
        
        for list in product:
            print("Scanned -", list['name'])

        json_formatter(path_to_save_basket)


    def remove(self, barcode: int) -> None:
        print("Removing ...")
        time.sleep(1)
        
        shop.remove_product_from_basket(1, barcode)

        product = item.get_product(barcode)
        
        for list in product:
            print("Removed -", list['name'])





    def cancel(self) -> None:
        shop.basket.clear()

    def purchashe(self) -> None:
        
        printer.basket = shop.basket
        printer.receipt()
    
    def test(self) -> None:
        print(shop.basket)

    