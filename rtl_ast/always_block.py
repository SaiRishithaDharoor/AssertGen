from rtl_ast.procedural_block import ProceduralBlock


class AlwaysBlock(ProceduralBlock):

    def __init__(self, sensitivity_list):

        self.sensitivity_list = sensitivity_list

        self.statement_block = None