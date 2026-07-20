from parser.file_reader import read_rtl
from parser.tokenizer import tokenize
from parser.parser import Parser

rtl = read_rtl("examples/always_test.sv")
tokens = tokenize(rtl)

parser = Parser(tokens)

print("Current token:", parser.current_token())

file = parser.parse_file()

print(file)
