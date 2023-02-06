import json

from database import connection
from config import path_to_save_basket

class Storage:

    def append_product_to_basket(self, product):

        json_obj = json.dumps(product, indent=4, separators=(", ", " : "))

        file = open(path_to_save_basket, "a")
        file.write(json_obj)

        file.close()
    
    def show_basket(self):
        file = open(path_to_save_basket, "r")

        content = file.read()
        products = json.loads(content)

        for product in products:
            print(product)

        file.close()
    def remove_product_from_basket(self, barcode: str) -> None:
        """Delete a one 

        Args:
            barcode (str): Deleting only one product from basket.
        """
        barcode = str(barcode)

        filer = open(path_to_save_basket, "r")
        content = filer.read()
        content = json.loads(content)

        for idx, obj in enumerate(content):

            if obj['barcode'] == barcode:
                content.pop(idx)
                break
                


        with open(path_to_save_basket, 'w', encoding='utf-8') as f:
            f.write(json.dumps(content, indent=4))




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
    