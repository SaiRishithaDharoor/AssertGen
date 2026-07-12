from parser.file_reader import read_rtl
from parser.tokenizer import tokenize

def main():

    print("AssertGen v0.1")

    rtl = read_rtl("examples/counter.sv")

    print("\nReading RTL...\n")

    print("--------------------------------")
    print(rtl)
    print("--------------------------------")

    print("\nRTL loaded successfully.")

    tokens = tokenize(rtl)
    print("\nTOKENS\n")

    for token in tokens:
        print(token)


if __name__ == "__main__":
    main()