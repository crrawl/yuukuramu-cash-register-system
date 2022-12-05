from pkg.Storage import Storage
from pkg.Product import Product
from pkg.Printer import Printer

class Cash_register(Storage):
        
   # __init__ cash register
    def __init__(self, name: str, money: int) -> None:

        self.name = name
        self.money = money
    
    def scan(self, barcode: int) -> None:
        product = Product.get_product(1, barcode)

        Storage.basket.append(product)


    def remove(self, barcode: int) -> None:
        product = Product.get_product(1, barcode)
        Storage.basket.remove(product)


    def cancel(self) -> None:
        Storage.basket.clear()

    def purchashe(self) -> None:
        
        Printer.basket = Storage.basket

    