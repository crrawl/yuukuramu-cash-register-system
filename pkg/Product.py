from database import connection

class Product:
            
    def generate_barcode(self, sellerid: int, categoryid: int) -> str:
        """generate barcode

        Args:
            sellerid (int): seller company id
            categoryid (int): category id

        Returns:
            str: barcode
        """


        with connection.cursor() as cursor:
            sql = f"SELECT id FROM products ORDER BY id DESC LIMIT 1;"
            cursor.execute(sql)
            lastest_row = cursor.fetchone()

            for productid in lastest_row.values():
                return f"{sellerid}{categoryid}{productid + 1}"


    def get_barcode(self, product_name: str) -> list:
        """

        Args:
            product_name (str): name of product

        Returns:
            list: example - (barcode:445)
        """

        with connection.cursor() as cursor:
            sql = f"SELECT barcode FROM products WHERE name = '{product_name}'"
            cursor.execute(sql)
            result = cursor.fetchall()
            
            return result

    def add_product(self, seller_id: int, name: str, count: int, weight: float, category: int, price: float) -> None:
        """Add product in database

        Args:
            barcode (int): generate barcode
            name (str): name of product
            count (int): count of product
            weight (float): products weight
            category (int): category of product
            price (float): product price
        """
        barcode = Product.generate_barcode(1, seller_id, category)
        with connection.cursor() as cursor:
            sql = f"INSERT INTO `products` (`barcode`, `name`, `count`, `weight`, `category`, `price`) VALUES ('{barcode}', '{name}', '{count}', '{weight}', '{category}', '{price}')"
            cursor.execute(sql)
            connection.commit()

    def get_product(self, barcode: int) -> list:
        """Get all information about product with barcode

        Args:
            barcode (int): 

        Returns:
            list: all information about product
        """
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM products WHERE barcode = '{barcode}'"
            cursor.execute(sql)
            result = cursor.fetchall()
        
        return result
