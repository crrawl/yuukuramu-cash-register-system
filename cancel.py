from pkg.Cash_register import CashRegister
import click

@click.command()
def cancel():
    CashRegister.cancel(1)

if __name__ == "__main__":
    cancel()