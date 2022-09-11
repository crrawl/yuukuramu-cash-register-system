
from pkg.__init__ import Cash_register
from pkg.products import Products

def main() -> None: 

    CR = Cash_register("DX6431LL", 30000)
    EH_Books = Products(127,865,755565)
    print( CR.copyrights())

    
    EH_Books.add_seller('seller_name', 6)




if __name__ == "__main__":
    main()