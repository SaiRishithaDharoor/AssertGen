from rtl_ast.expressions.identifier import Identifier
from rtl_ast.expressions.number_literal import NumberLiteral
from rtl_ast.expressions.binary_expression import BinaryExpression

from rtl_ast.statements.assignment import Assignment
from rtl_ast.statements.statement_block import StatementBlock


left = Identifier("count")

right = BinaryExpression(
    Identifier("count"),
    "+",
    NumberLiteral(1)
)

assignment = Assignment(
    left,
    "<=",
    right
)

print(assignment)

block = StatementBlock()

block.add_statement(assignment)

print(block)