from rtl_ast.statements.statement import Statement


class Assignment(Statement):

    def __init__(
        self,
        left,
        operator,
        right
    ):

        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):

        return (
            f"Assignment("
            f"{self.left} "
            f"{self.operator} "
            f"{self.right})"
        )