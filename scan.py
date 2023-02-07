from pkg.Cash_register import CashRegister
from os import system
import click

@click.command()
@click.argument('barcode')
def scan(barcode):
    """Scan product to add in basket.

    example: python3 scan.py [barcode]

    to check barcodes, products - use, python3 storage.py --help

    """
    CashRegister.scan(1, barcode)

if __name__ == "__main__":
    system("cls")
    scan()