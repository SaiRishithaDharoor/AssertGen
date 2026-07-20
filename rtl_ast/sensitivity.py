from rtl_ast.node import Node


class Sensitivity(Node):

    def __init__(self, edge, signal):

        self.edge = edge
        self.signal = signal

    def __repr__(self):

        return f"{self.edge} {self.signal}"