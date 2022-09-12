
from pkg.__init__ import Cash_register
from pkg.products import Products

def main() -> None: 

    CR = Cash_register("DX6431LL", 30000)
    milk = Products(127,2,755565)
    print( CR.copyrights())

    
    print(type(milk.get_category_info()))




if __name__ == "__main__":
    main()