from rtl_ast.node import Node


class DataType(Node):

    def __init__(
        self,
        kind,
        width=None,
        signed=False
    ):

        self.kind = kind

        self.width = width

        self.signed = signed

    def __repr__(self):
        return f"{self.kind}"