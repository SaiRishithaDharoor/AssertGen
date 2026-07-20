from rtl_ast.expressions.expression import Expression


class NumberLiteral(Expression):

    def __init__(self, value):

        self.value = int(value)

    def __repr__(self):

        return str(self.value)