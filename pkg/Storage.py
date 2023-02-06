import json

from database import connection
from config import path_to_save_basket

class Storage:
    
    # basket = [[{'id': 25, 'barcode': '4510', 'name': 'Samsung Galaxy A20e', 'count': 1, 'weight': 0.7, 'category': 5, 'price': 300.99}]]

    def append_product_to_basket(self, product):
        json_obj = json.dumps(product, indent=4, separators=(", ", " : "))

        file = open(path_to_save_basket, "a")
        file.write(json_obj)

        file.close()
    
    def read_basket_element(self, product):
        file = open(path_to_save_basket, "r")

        content = file.read()
        products = json.loads(content)

        for product in products:
            print(product)

        file.close()




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
        
        return result

    def storage_items(self) -> list:

        with connection.cursor() as cursor:
            sql = "SELECT * FROM products WHERE count > 0"
            cursor.execute(sql)
            result = cursor.fetchall()
        
        return result
    