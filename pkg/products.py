# REDESIGN SYSTEM -> Product.py
# REDESIGN SYSTEM -> Product.py
# REDESIGN SYSTEM -> Product.py
# REDESIGN SYSTEM -> Product.py
# REDESIGN SYSTEM -> Product.py
# REDESIGN SYSTEM -> Product.py
# REDESIGN SYSTEM -> Product.py
# REDESIGN SYSTEM -> Product.py

from database import connection

class Product():
    def __init__(self, sellerid, categoryid, productid) -> None:

        self.sellerid = sellerid
        self.categoryid = categoryid
        self.productid = productid

    def generate_barcode(self) -> str:
        self.categoryid = str(self.categoryid)
        self.sellerid = str(self.sellerid)
        self.productid = str(self.productid)

        return f"{self.categoryid.zfill(3)}-{self.sellerid.zfill(3)}-{self.productid.zfill(6)}"

    def get_category_info(self) -> tuple:
        """return category id:name

        Returns:
            tuple: all db rows - category_id:category_name
        """
        with connection.cursor() as cursor:
            sql = "SELECT * FROM category"
            cursor.execute(sql)
            result = cursor.fetchall()
            connection.commit()

        for item in range(len(result)):
            return result[item]['category_id'], result[item]['category_name']

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
            sql = f"INSERT INTO `sellers` (`seller_name`, `category`) VALUES ('{seller_name}', {category})"
            cursor.execute(sql)
            connection.commit()