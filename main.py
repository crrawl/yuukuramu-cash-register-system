
from pkg.__init__ import Cash_register

from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWD
from database import _Database_

def main() -> None: 

    db = _Database_(DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWD)
    CR = Cash_register("DX6431LL", 30000)

    print( CR.copyrights())





if __name__ == "__main__":
    main()