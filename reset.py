import click
from os import system

from config import path_to_save_receipts
from file_controll import delete_all_files

@click.command()
def reset():
    """reset all system
    example, python3 reset.py
    """
    delete_all_files(path_to_save_receipts)

if __name__ == "__main__":
    system("cls")
    reset()