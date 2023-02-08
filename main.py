import os

from pkg.Cash_register import CashRegister
from pkg.intro import Init
from time import sleep

Init = Init()
CR = CashRegister("DX6431LL", 30000)


def main():
    print("""
                     _    _      _                              _         
                    | |  | |    | |                            | |        
                    | |  | | ___| | ___ ___  _ __ ___   ___    | |_ ___   
                    | |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \   | __/ _ \  
                    \  /\  /  __/ | (_| (_) | | | | | |  __/   | || (_) | 
                     \/  \/ \___|_|\___\___/|_| |_| |_|\___|    \__\___/  
 _____           _      ______           _     _              _____           _                 
/  __ \         | |     | ___ \         (_)   | |            /  ___|         | |                
| /  \/ __ _ ___| |__   | |_/ /___  __ _ _ ___| |_ ___ _ __  \ `--. _   _ ___| |_ ___ _ __ ___  
| |    / _` / __| '_ \  |    // _ \/ _` | / __| __/ _ \ '__|  `--. \ | | / __| __/ _ \ '_ ` _ \ 
| \__/\ (_| \__ \ | | | | |\ \  __/ (_| | \__ \ ||  __/ |    /\__/ / |_| \__ \ ||  __/ | | | | |
 \____/\__,_|___/_| |_| \_| \_\___|\__, |_|___/\__\___|_|    \____/ \__, |___/\__\___|_| |_| |_|
                                    __/ |                            __/ |                      
                                   |___/                            |___/               """)
    sleep(3)
    print(Init.copyrights())
    print("Version:", Init.version())

    sleep(1)

    print("\nOpen cmds.md or py user.py to check commands\n")

    sleep(1)


    os.system("py user.py")

    sleep(1)

    print("Write 'pip: -r requirements.txt' to install important modules")
    sleep(1)
    print("\nCMD SYNTAX: python [cmd].py [args] [-options]")
if __name__ == "__main__":
    os.system("cls")
    main()

