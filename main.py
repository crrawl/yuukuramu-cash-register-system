import os

# from rich import emoji
from rich.console import Console
from rich.theme import Theme
# from rich.table import Table 


from pkg.__init__ import Cash_register
from pkg.products import Products
from pkg.env import Environment

from config import USERNAME, HOSTNAME


crtheme = Theme(
    {
        "error": "bold red",
        "success": "bold green",
        "attention": "bold yellow",
        "warning": "bold magenta",
        "help": "#1C1C1C",
        "option": "#4169E1",
        "blocked": "#383B40",
        "green": "green",
        "white": "white",
        "light_blue": "#3B78FF",
    }
)
# shortcut
# thee shortcut
bash = Console(theme=crtheme)

product = Products(127, 6, 127)
CR = Cash_register("DX6431LL", 30000)

env = Environment(USERNAME, HOSTNAME, bash, product)


def main() -> None: 
    while True:
        env.start()
        env.commands()

if __name__ == "__main__":
    os.system("cls")
    main()
