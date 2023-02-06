
from pkg.Cash_register import CashRegister
import click

@click.command()
@click.argument('barcode')
def scan(barcode):
    CashRegister.scan(1, barcode)

if __name__ == "__main__":
    scan()