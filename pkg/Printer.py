from datetime  import datetime
import calendar
import time
import os


from config import path_to_save_receipts, path_to_save_basket
from pkg.Storage import Storage

class Printer:

    if not os.stat(path_to_save_basket).st_size==0:
        basket = Storage.show_basket(1)
    else:
        basket = []

    print(Storage.show_basket, "shitty")
    def __init__(self) -> None:
        self.basket = Printer.basket


    def get_datetime(self, format: str = "%Y-%m-%d %H:%M:%S %Z%z") -> datetime:
        """get datetime from

        Args:
            format (str, optional): datetime format. Defaults to "%Y-%m-%d %H:%M:%S %Z%z".

        Returns:
            datetime: str with datetime 
        """
        time = datetime.now()
        return time.strftime(format)

    def get_timestamp(self) -> str:
        """get timestamp

        Returns:
            str: timestamp
        """
        return calendar.timegm(time.gmtime())

    def receipt(self) -> str:
        time = Printer.get_datetime(self)
        timestamp = Printer.get_timestamp(self)
        path = os.path.join(path_to_save_receipts, f"{timestamp}.txt")


        if not os.path.isdir(path_to_save_receipts):
            os.mkdir(path_to_save_receipts)


        with open(path, "w", encoding="utf-8") as f:
            f.write(f"""
db    db db    db db    db db   dD db    db d8888b.  .d8b.  .88b  d88. db    db .d8888. db   db  .d88b.  d8888b. 
`8b  d8' 88    88 88    88 88 ,8P' 88    88 88  `8D d8' `8b 88'YbdP`88 88    88 88'  YP 88   88 .8P  Y8. 88  `8D 
 `8bd8'  88    88 88    88 88,8P   88    88 88oobY' 88ooo88 88  88  88 88    88 `8bo.   88ooo88 88    88 88oodD' 
   88    88    88 88    88 88`8b   88    88 88`8b   88~~~88 88  88  88 88    88   `Y8b. 88~~~88 88    88 88~~~   
   88    88b  d88 88b  d88 88 `88. 88b  d88 88 `88. 88   88 88  88  88 88b  d88 db   8D 88   88 `8b  d8' 88      
   YP    ~Y8888P' ~Y8888P' YP   YD ~Y8888P' 88   YD YP   YP YP  YP  YP ~Y8888P' `8888Y' YP   YP  `Y88P'  88
-----------------------------------------------------------------------------------------------------------------  
SIA "YUUKURAMUSHOP Japan"
Veikals "ゆうくらむショップ"
Jelgavas iela 97A, Saldus, t. Unknown
Kase Nr.1
Juridiskā adrese: 〒106-0074東京都港区東麻布1-9-1 東麻布ISビル4F                                                                                                 
PVN maksātāja kods offical - JP4000548636
PVN maksātāja kods - LV4000548636        
""")
            total = 0

            for items in self.basket:

                f.write(f"""
{items["name"]}                                                                                  {items["price"]}$
""")

            f.write(f"""
==================================================================================================================
Kopā apmaksai                                                                                             {total}$
------------------------------------------------------------------------------------------------------------------
DOKUMENTA Nr        103812-221205
TERMINĀĻA ID        DX-RAZER
LAIKS               {time}

SS8SA7FJSF8MSF8AS7FDS8FAMAS9F8ASDNFSA987FS98F7SAD8F79SF7A9S8DF9S8FSM9F8S9F7SF987FSN9F78SF98S7F9FNSF987ASFAF6A3978TG
SSAFDF7MSA9DF87A9387AM4F98WA7FWA9MF78WA98F7A9DDDDF8AW7FM8A37AWFDDD8ARM798EFA8FA9F8AMAAAE98FAE9F8AM9F8AFAUSFPASEMFAG
SFF3RFU2098RQFNVA09SADSAFDAS8DFA7F0FAPWEPDF8A9PESFUWAP382Q8ER8REQUANCZUCNSXZHC9EWQ8NQ098CYSA98YS9F8NUQW98QFOIFSUFIG
SSAFDF7MSA9DF87A9387AM4F98WA7FWA9MF78WA98F7A9DDDDF8AW7FM8A37AWFDDD8ARM798EFA8FA9F8AMAAAE98FAE9F8AM9F8AFAUSFPASEMFAG """)

            print("Čeks ir izprintēts")
            f.close()