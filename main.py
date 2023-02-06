import os

from pkg.Cash_register import Cash_register
from pkg.Storage import Storage
from pkg.Product import Product
from pkg.Printer import Printer


item = Product()
shop = Storage()

CR = Cash_register("DX6431LL", 30000)


def main():
    # product.add_product(product.generate_barcode(4, 5), 'Iphone 12 Pro Max 512GB', 12, 0.700, 5, 1200.00)
    # product.add_product(product.generate_barcode(4, 5), 'Iphone 12 Pro 512GB', 12, 0.700, 5, 1000.00)
    # product.add_product(product.generate_barcode(4, 5), 'Iphone 12 512GB', 12, 0.700, 5, 800.00)
    # product.add_product(product.generate_barcode(4, 5), 'Iphone 12 512GB', 12, 0.700, 5, 800.00)
    # product.add_product(product.generate_barcode(4, 5), 'Piens Farn Milk 3.2% 1L', 3, 0.700, 5, 0.99)
    # product.add_product(product.generate_barcode(4, 5), 'Apelsīni mazie C4/5 NAVELINA 2.šķ.', 3, 7, 5, 1.3)

    CR.scan(4521)
    CR.scan(4526)

    CR.purchashe()

    # prin = Printer()
    # prin.receipt()

if __name__ == "__main__":
    os.system("cls")
    main()

