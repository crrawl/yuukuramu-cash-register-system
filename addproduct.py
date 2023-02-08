import click
from os import system
from pkg.Product import Product

@click.command()
@click.argument("seller_id")
@click.argument("name")
@click.argument("count")
@click.argument("weight")
@click.argument("category")
@click.argument("price")
def addproduct(seller_id, name, count, weight, category, price):
    """Add product in storage

    Usage: python3 addproduct.py \n
                        seller_id (int): seller id \n
                        name (str): name of product\n
                        count (int): count of product\n
                        weight (float): products weight\n
                        category (int): category of product\n
                        price (float): product price

    """
    Product.add_product(1, seller_id, name, count, weight, category, price)


if __name__ == "__main__":
    system("cls")
    addproduct()

