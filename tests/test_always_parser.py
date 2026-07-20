from parser.file_reader import read_rtl
from parser.tokenizer import tokenize
from parser.parser import Parser


def main():

    rtl = read_rtl("examples/always_test.sv")

    tokens = tokenize(rtl)

    parser = Parser(tokens)

    file = parser.parse_file()

    print(file)

    print()

    module = file.modules[0]

    print(module)

    print("\nPorts")
    print("--------------------")
    for port in module.ports:
        print(port)

    print("\nSignals")
    print("--------------------")
    for signal in module.signals:
        print(signal)

    print("\nProcedural Blocks")
    print("--------------------")
    for block in module.procedural_blocks:
        print(block)

        print("Kind        :", block.kind)
        print("Sensitivity :", block.sensitivity)
        print("Body        :", block.body)


if __name__ == "__main__":
    main()