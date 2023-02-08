class Init:
        
    def __init__(self) -> None:

        self.__author__ = "Raibisu Yuu Kuramu"
        self.__email__  = "yuukuramu@proton.me"
        self.__version__ = "v7.0.1-release"
        self.__copyrights__ = """
# -----------------------------------------------------
# @Author 来ビス―クラム　(yuukuramu@proton.me)
# @github https://github.com/yuukuramu
# @LinkedIn www.linkedin.com/in/yuukuramu
# @instagram https://www.instagram.com/raibisu.kuramu
# @site https://yuukuramu.me
# -----------------------------------------------------
"""
    
    def copyrights(self) -> str:
        """copyrights

        Returns:
            str: copyrights
        """
        return self.__copyrights__

    def version(self) -> str:
        """copyrights

        Returns:
            str: copyrights
        """
        return self.__version__