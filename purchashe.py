
from pkg.Cash_register import CashRegister
import click

@click.command()
def purcashe():
    CashRegister.purchashe(1)

if __name__ == "__main__":
    purcashe()