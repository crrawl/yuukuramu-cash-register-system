class Cash_register:
        
   # __init__ cash register
    def __init__(self, name: str, money: int) -> None:

        self.__author__ = "Raibisu Yuu Kuramu"
        self.__email__  = "yuukuramu@proton.me"
        self.__version__ = "v1.0-alpha"
        self.__copyrights__ = """
# -----------------------------------------------------
# @Author 来ビス―クラム　(yuukuramu@proton.me)
# @github https://github.com/yuukuramu
# @LinkedIn www.linkedin.com/in/yuukuramu
# @instagram https://www.instagram.com/raibisu.kuramu
# @site https://yuukuramu.xyz
# -----------------------------------------------------"""

        self.__name = name
        self.money = money
    
    def copyrights(self) -> str:
        return self.__copyrights__
        

    def id(self) -> str:
        return self.__name


