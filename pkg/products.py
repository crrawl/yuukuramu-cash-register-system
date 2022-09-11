from database import connection

class Products():
    def __init__(self, sellerid, categoryid, productid) -> None:

        self.sellerid = sellerid
        self.categoryid = categoryid
        self.productid = productid

    def generate_barcode(self) -> str:
        self.categoryid = str(self.categoryid)
        self.sellerid = str(self.sellerid)
        self.productid = str(self.productid)

        return f"{self.categoryid.zfill(3)}-{self.sellerid.zfill(3)}-{self.productid.zfill(6)}"


    def add_product(self) -> None:
        pass

    def add_seller(self, seller_name: str, category: int) -> None:
        """add seller

        Args:
            seller_name (str): seller company name: SIA KURAMU CORP
            category (int): category id : 127 -> hackers books
        """
        
        # TODO: select category_id:category_name
        with connection.cursor() as cursor:
            # sql = f"INSERT INTO `sellers` (`seller_name`, `category`) VALUES ('Kuramu corp', 6)"
            sql = f"INSERT INTO `sellers` (`seller_name`, `category`) VALUES ('{seller_name}', {category})"
            cursor.execute(sql)
            connection.commit()