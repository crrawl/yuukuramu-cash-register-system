from pkg.Storage import Storage
import click
from os import system
@click.command()
@click.argument('seller_name')
@click.argument('category_id')
def addseller(seller_name, category_id):
    """Purchashe products and get receipt

    Usage: python3 addseller.py [seller_name] [category_id]
    example, python3 addseller.py "Evil Corp" 4

    4 is category_id from 'PC'

    You can check categories with,

    python3 showcategories.py
    """

    Storage.add_seller(1, seller_name, category_id)

if __name__ == "__main__":
    system("cls")
    addseller()
