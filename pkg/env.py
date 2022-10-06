from config import help

class Environment:

    def __init__(self, USER: str, HOST: str, bash, product: str) -> None:
        
        self.USER = USER
        self.HOST = HOST
        self.bash = bash
        self.product = product


    def start(self) -> list:
        bash_name = f"[green]{self.USER}@{self.HOST}[/][white]:[/][light_blue]~[/][white]$[/] "
        self.cmd = self.bash.input(bash_name).split()
        
        try:
            # if command is not in help dict -> config file
            if self.cmd[0] not in help:
                self.bash.print(f"[help]{self.cmd[0]}: Command not found[/]")
        except IndexError:
            pass

        try:
            # If command no arguments given, print command's help info
            if self.cmd[1]:
                pass
        except IndexError:
            try:
                self.bash.print(help[self.cmd[0]])
            except:
                pass

        return self.cmd



    #####################################
    ##### To add new command        #####
    ##### Code logic                #####
    ##### Add in handler            #####
    ##### Add in help()             #####
    ##### Add in help -> config file ####
    #####################################



    #  commands handler
    def help(self) -> str:

        cmd = self.cmd[1]
        
        if self.cmd[0] == "help":

            try:
                if cmd == "help":
                    self.bash.print(help["help"])

                elif cmd == "addseller":
                    self.bash.print(help["addseller"])
                elif cmd == "clear":
                    self.bash.print(help["clear"])

            except IndexError:
                self.bash.print("[help]help \[comand][/]")


    def addseller(self) -> None:
        if self.cmd[0] == "addseller":
            self.product.add_seller(self.cmd[1], self.cmd[2])   
            print("seller is added")
        
    def konnichiwa (self) -> None:

        if self.cmd[0] == "konnichiwa":
            print(f"こんいしわ {self.cmd[1]}ーさん")
                
    def clear(self) -> None:
        if self.cmd[0] == "clear":

            import os
            os.system("cls")




    # declare commands
    def commands(self) -> None:
        
        try:

            Environment.help(self)
            Environment.konnichiwa(self)
            Environment.clear(self)

            Environment.addseller(self)
        except:
            pass