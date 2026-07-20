from rtl_ast.statements.statement import Statement


class StatementBlock(Statement):

    def __init__(self):

        self.statements = []

    def add_statement(self, statement):

        self.statements.append(statement)

    def __repr__(self):

        return f"StatementBlock({len(self.statements)} statements)"