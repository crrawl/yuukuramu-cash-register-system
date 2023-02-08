from pkg.Cash_register import CashRegister
from os import system
import click

@click.command()
def cancel():
    """Cancel paymant. Clear basket
    Usage: python3 cancel.py
    """
    CashRegister.cancel(1)

if __name__ == "__main__":
    system("cls")
    cancel()