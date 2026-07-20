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

    def add_parameter(self, parameter):
        self.parameters.append(parameter)

    def add_port(self, port):
        self.ports.append(port)

    def add_signal(self, signal):
        self.signals.append(signal)

    def add_instance(self, instance):
        self.instances.append(instance)

    def add_continuous_assignment(self, assignment):
        self.continuous_assignments.append(assignment)

    def add_procedural_block(self, block):
        self.procedural_blocks.append(block)

    def __repr__(self):

        return (
            f"Module("
            f"name='{self.name}', "
            f"ports={len(self.ports)}, "
            f"signals={len(self.signals)}, "
            f"blocks={len(self.procedural_blocks)}"
            f")"
        )