from rtl_ast.node import Node


class Port(Node):
    """
    Represents a module port.

    Example:
        input logic [7:0] data
    """

    def __init__(self, name, direction, datatype):

        self.name = name
        self.direction = direction
        self.datatype = datatype

    def __repr__(self):

        return (
            f"Port("
            f"name='{self.name}', "
            f"direction='{self.direction}', "
            f"datatype={self.datatype}"
            f")"
        )