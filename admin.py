import click
@click.group()
def admin():
    """Admin commands"""

@admin.command('addproduct.py', short_help=' Add product in database')
def addproduct():
    """
    Usage: py addproduct.py [seller id] [Product name] [Count] [weight] [category] [price]
    """

@admin.command('addseller.py', short_help='Add seller in database')
def addseller():
    """
    Usage: py addseller.py [seller name] [category id]
    """

@admin.command('checkproduct.py', short_help='Check Product information')
def checkproduct():
    """
    Usage: py checkproduct.py [barcode]
    """

@admin.command('showcategories.py', short_help='Show All Categories')
def showcategories():
    """
    Usage: py showcategories.py
    """

if __name__ == "__main__":
    admin()