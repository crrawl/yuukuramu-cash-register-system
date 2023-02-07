from pkg.Storage import Storage
from os import system
import click

@click.command()
def storage():
    """Show all magasine storage products

    example: python3 storage.py

    """

    storage = Storage.storage_items(1)
    # print("\nID", "\t|", "Svītrkods", "\t|", "Produkts", "\t\t\t\t|", "Daudzums", "\t|", "Cena")
    print("\nID", "Svītrkods", "Produkts", "Daudzums", "Cena")
    print("================================================================")

    for item in storage:
        print(item["id"], " - ", item["barcode"], " - ", item["name"], " - ", item["count"], " - ", item["price"])
        print("----------------------------------------------------------------")
if __name__ == "__main__":
    system("cls")
    storage()