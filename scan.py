
from pkg.Cash_register import Cash_register
import click

@click.command()
@click.argument('barcode')
def scan(barcode):
    Cash_register.scan(1, barcode)

if __name__ == "__main__":
    scan()