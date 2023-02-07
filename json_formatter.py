import json

def json_formatter(filename: str) -> json:
    """json_formatter

        Args:
            filename (str): path to the json file
        """

    # read file
    filer = open(filename, "r")
    content = filer.read()
    
    # replace symbols
    content = content.replace("][", ",")

    content = content.replace("[,", "[")

    # write content, delete old file
    file = open(filename, "w")

    file.write(content)
