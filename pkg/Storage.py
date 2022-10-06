from database import connection

class Storage:

    def add_product(self, barcode: int, name: str, count: int, weight: float, category: int, price: float) -> None:
        pass

    def get_product(self, barcode: int) -> list:
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
            return result[item]['category_id'], \
                    result[item]['category_name']