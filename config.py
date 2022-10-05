
# database connection
DB_HOST: str    = "127.0.0.1"
DB_PORT: int    = 3306
DB_NAME: str    = "cash-register-database"
DB_USER: str    = "root"
DB_PASSWD: str  = ""


# bash name
USERNAME = "yuukuramu"
HOSTNAME = "CASH-REGISTER"

help_without_arguments = {
    "id": """[help]id
id returns current user information
[/]""",
}
help = {
    "help": """[help]help \[comand]
help give you a information about the command
[/]""",

    "addseller": """[help]addseller \[seller name] \[product category]
Add new seller in database
[/]""",
    "konnichiwa": """[help]konnichiwa \[name] 
greetings
[/]"""
}

def Merge(dict1, dict2):
    new_dic = {}
    # return(dict2.update(dict1))

    new_dic.update(dict1)
    new_dic.update(dict2)
    return new_dic
    
all_commands_list = Merge(help_without_arguments, help)
