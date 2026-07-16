from rtl_ast.node import Node


class Module(Node):

    def __init__(self, name):

        self.name = name

        self.parameters = []

        self.ports = []

        self.signals = []

        self.instances = []

        self.continuous_assignments = []

        self.procedural_blocks = []

    def __repr__(self):
        return f"Module({self.name})"