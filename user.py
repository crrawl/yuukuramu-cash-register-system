import click
@click.group()
def user():
    """user commands"""

@user.command('storage.py', short_help='View magasine storage')
def storage():
    """"""

@user.command('scan.py', short_help='scan product from storage')
def scan():
    """"""

@user.command('remove.py', short_help='remove product from basket')
def remove():
    """"""
@user.command('cancel.py', short_help='Cancel purchashe')
def cancel():
    """"""
@user.command('purchashe.py', short_help="purchashe all products from basket")
def purchashe():
    """"""
@user.command('show.py', short_help="View basket products")
def show():
    """"""

if __name__ == "__main__":
    user()