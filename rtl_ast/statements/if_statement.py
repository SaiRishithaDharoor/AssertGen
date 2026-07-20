from rtl_ast.statements.statement import Statement


class IfStatement(Statement):

    def __init__(
        self,
        condition,
        then_block,
        else_block=None
    ):

        self.condition = condition

        self.then_block = then_block

        self.else_block = else_block

    def __repr__(self):

        return (
            f"IfStatement("
            f"condition={self.condition}, "
            f"then_block={self.then_block}, "
            f"else_block={self.else_block})"
        )