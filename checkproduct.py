import click
from os import system
from pkg.Product import Product

@click.command()
@click.argument("barcode")
def checkproduct(barcode):
    """Check product information

    Usage: python3 checkproduct.py [barcode]"""

    product = Product.get_product(1, barcode)
    print("\nID", "|", "Barcode", "|", "Product", "|", "count", "|",  "weight", "|",  "category", "|",  "price")
    print("==========================================================")
    for obj in product:
        print(obj["id"], "-", obj["barcode"], "-", obj["name"], "-", obj["count"], "-", obj["weight"], "-", obj["category"], "-", obj["price"], "\n")


if __name__ == "__main__":
    system("cls")
    checkproduct()