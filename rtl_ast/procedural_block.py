from rtl_ast.node import Node


class ProceduralBlock(Node):

    def __init__(self, kind, sensitivity, body):

        self.kind = kind
        self.sensitivity = sensitivity
        self.body = body

    def __repr__(self):

        return (
            f"ProceduralBlock("
            f"kind='{self.kind}', "
            f"sensitivity={self.sensitivity})"
        )