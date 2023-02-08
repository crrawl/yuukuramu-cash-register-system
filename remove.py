from pkg.Cash_register import CashRegister
from os import system
import click

@click.command()
@click.argument('barcode')
def remove(barcode):
    """Remove product from basket
    Usage: python3 remove.py [barcode]
    """
    CashRegister.remove(1, barcode)

if __name__ == "__main__":
    system("cls")
    remove()