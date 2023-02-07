
from pkg.Cash_register import CashRegister
from os import system
import click

@click.command()
@click.argument('barcode')
def purchashe(barcode):
    """Add seller

    """
    CashRegister.scan(1, barcode)

if __name__ == "__main__":
    system("cls")
    purchashe()