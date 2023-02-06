from .. import hello
import click

print(dir(hello.hello))

# @click.command()
# @click.argument('barcode')
# def scan(barcode):
#     CR.scan(barcode)

def scan():
    pass
    # CR.scan(4555)
if __name__ == "__main__":
    scan()