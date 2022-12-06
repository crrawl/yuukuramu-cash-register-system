from pkg.Storage import Storage
from pkg.Product import Product
from pkg.Printer import Printer

printer = Printer()
shop = Storage
item = Product()

class Cash_register(Storage):
        
   # __init__ cash register
    def __init__(self, name: str, money: int) -> None:

        self.name = name
        self.money = money
    
    def scan(self, barcode: int) -> None:
        product = item.get_product(barcode)

        shop.basket.append(product)


    def remove(self, barcode: int) -> None:
        product = item.get_product(barcode)
        shop.basket.remove(product)


    def cancel(self) -> None:
        shop.basket.clear()

    def purchashe(self) -> None:
        
        printer.basket = shop.basket
        printer.receipt()

    