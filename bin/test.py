
from pkg.Cash_register import CashRegister
import click

@click.command()
def test():
    CashRegister.test(1)

if __name__ == "__main__":
    test()