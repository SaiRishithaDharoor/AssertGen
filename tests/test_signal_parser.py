from parser.file_reader import read_rtl
from parser.tokenizer import tokenize
from parser.parser import Parser


def main():

    rtl = read_rtl("examples/signal_test.sv")

    tokens = tokenize(rtl)

    parser = Parser(tokens)

    file = parser.parse_file()

    # ---------- AST Tests ----------

    assert len(file.modules) == 1

    module = file.modules[0]

    assert module.name == "signal_test"

    assert len(module.ports) == 1
    assert module.ports[0].name == "clk"

    assert len(module.signals) == 2

    assert module.signals[0].name == "ready"
    assert module.signals[1].name == "data"

    assert module.signals[0].datatype.kind == "logic"
    assert module.signals[1].datatype.width == "[7:0]"

    print("✅ All AST tests passed!")

    print("\nModules:")
    print(module)

    print("\nPorts:")
    for port in module.ports:
        print(port)

    print("\nSignals:")
    for signal in module.signals:
        print(signal)


if __name__ == "__main__":
    main()