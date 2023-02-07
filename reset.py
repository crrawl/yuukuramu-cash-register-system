import click
import os

from config import path_to_save_receipts
from file_controll import delete_all_files

@click.command()
def scan():
    delete_all_files(path_to_save_receipts)

if __name__ == "__main__":
    scan()