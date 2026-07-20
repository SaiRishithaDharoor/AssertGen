from rtl_ast.port import Port
from rtl_ast.datatype import DataType


def main():

    datatype = DataType(
        kind="logic",
        width="[7:0]",
        signed=False
    )

    port = Port(
        name="count",
        direction="output",
        datatype=datatype
    )

    print("Port Object")
    print(port)

    print()

    print("Name       :", port.name)
    print("Direction  :", port.direction)
    print("Datatype   :", port.datatype.kind)
    print("Width      :", port.datatype.width)
    print("Signed     :", port.datatype.signed)


if __name__ == "__main__":
    main()