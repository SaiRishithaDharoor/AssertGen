from parser.file_reader import read_rtl
from parser.tokenizer import tokenize
from parser.parser import Parser


def main():

    rtl = read_rtl("examples/counter.sv")

    tokens = tokenize(rtl)

    parser = Parser(tokens)

    file = parser.parse_file()

    print(file)

    print()

    for module in file.modules:

        print(module)

        print("\nPorts:")

        for port in module.ports:
            print("   ", port)
        
        

if __name__ == "__main__":
    main()