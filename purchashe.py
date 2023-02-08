
from pkg.Cash_register import CashRegister
from os import system
import click

@click.command()
@click.argument('barcode')
def purchashe(barcode):
    """Purchashe products
    Usage: py purchashe.py
    """
    CashRegister.purchashe(1)

if __name__ == "__main__":
    system("cls")
    purchashe()