from pkg.Storage import Storage
from os import system
import click

@click.command()
def showcategories():
    """Show all categories

    To add category use: addcategorie.py


    example: python3 showcategories.py
    """

    data = Storage.get_category_info(1)

    print("Parrent ID\t", "Category ID\t", "Category")
    print("=========================================")
    for item in data:
        print(item["parrent_id"],"\t\t", item["category_id"],"\t\t",  item["category_name"])



if __name__ == "__main__":
    system("cls")
    showcategories()
