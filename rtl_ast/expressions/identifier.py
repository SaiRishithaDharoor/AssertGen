from rtl_ast.expressions.expression import Expression


class Identifier(Expression):

    def __init__(self, name):

        self.name = name

    def __repr__(self):

        return self.name