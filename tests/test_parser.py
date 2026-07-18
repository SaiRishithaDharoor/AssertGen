from parser.file_reader import read_rtl
from parser.tokenizer import tokenize
from parser.parser import Parser


rtl = read_rtl("examples/counter.sv")

print("RTL:")
print(rtl)

tokens = tokenize(rtl)

print("\nNumber of tokens:", len(tokens))

print("\nTokens:")
for token in tokens:
    print(token)

parser = Parser(tokens)

print("\nCurrent token:")
print(parser.current_token())