from rtl_ast.node import Node


class File(Node):

    def __init__(self):
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def __repr__(self):
        return f"File({len(self.modules)} modules)"