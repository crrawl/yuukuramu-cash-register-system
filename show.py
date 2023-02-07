from pkg.Storage import Storage
import click
storage = Storage()

@click.command()
def show():
    basket = storage.show_basket

    if not basket:
        print("Basket is empty")
        exit()

    for obj in basket:
        print("\n")
        for item in obj:
            print(item, obj[item])
        
if __name__ == "__main__":
    show()
