from rtl_ast.node import Node


class Signal(Node):

    def __init__(self, name, datatype):

        self.name = name
        self.datatype = datatype

    def __repr__(self):

        return (
            f"Signal("
            f"name='{self.name}', "
            f"datatype={self.datatype}"
            f")"
        )