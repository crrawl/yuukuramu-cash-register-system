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
            if self.cmd[0] not in help:
                self.bash.print(f"[help]{self.cmd[0]}: Command not found[/]")
        except IndexError:
            pass

        try:
            if self.cmd[1]:
                pass
        except IndexError:
            try:
                self.bash.print(help[self.cmd[0]])
            except:
                pass

        return self.cmd

        
        # return self.cmd
    

    def help(self) -> str:

        cmd = self.cmd[1]
        
        # commands without arguments
        if cmd == "id":
            Environment.has_atributes == False
            self.bash.print(help["id"])      
        
        # commands with arguments
        if self.cmd[0] == "help":

            try:
                if cmd == "help":
                    self.bash.print(help["help"])

                elif cmd == "addseller":
                    self.bash.print(help["addseller"])

            except IndexError:
                self.bash.print("[help]help \[comand][/]")


    def addseller(self) -> None:
        if self.cmd[0] == "addseller":
            self.product.addseller(self.cmd[1], self.cmd[2])   
            print("seller is added")
        
    def id (self) -> None:
        self.cmd[1] == "Nones"
        if self.cmd[0] == "id":
            print("Your id")

            # for item in config

    def konnichiwa (self) -> None:

        if self.cmd[0] == "konnichiwa":
            print(f"こんいしわ {self.cmd[1]}ーさん")
                

    def commands(self) -> None:
        
        try:

            Environment.id(self)
            Environment.help(self)
            Environment.addseller(self)
            Environment.konnichiwa(self)

        except:
            pass