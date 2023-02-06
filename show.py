
from pkg.Storage import Storage
import click

@click.command()

def show():
    Storage.show_basket(1)

if __name__ == "__main__":
    show()