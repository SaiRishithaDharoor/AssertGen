from rtl_ast.node import Node


class StatementBlock(Node):

    def __init__(self):

        self.statements = []

    def add_statement(self, statement):

        self.statements.append(statement)

    def __repr__(self):

        return (
            f"StatementBlock("
            f"{len(self.statements)} statements)"
        )