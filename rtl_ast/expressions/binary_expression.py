from rtl_ast.expressions.expression import Expression


class BinaryExpression(Expression):

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
            f"({self.left} "
            f"{self.operator} "
            f"{self.right})"
        )