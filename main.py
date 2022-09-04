#!/usr/bin/python3

from pkg.__init__ import Cash_register

def main() -> None:

    CR = Cash_register("DX6431LL", 30000)

    print(CR.copyrights())

if __name__ == "__main__":
    main()