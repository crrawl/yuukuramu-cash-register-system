from pkg.Storage import Storage
from os import system
import click
storage = Storage()

@click.command()
def show():
    """Show all basket produkts

    We can scan products with - python3 scan.py --help
    """
    basket = storage.show_basket()

    if not basket:
        print("Basket is empty")
        exit()

    for obj in basket:
        print("\n")
        for item in obj:
            print(item, obj[item])
        
if __name__ == "__main__":
    system("cls")
    show()
