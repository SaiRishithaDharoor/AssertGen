import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from parser.file_reader import read_rtl
from parser.tokenizer import tokenize


def main():

    rtl = read_rtl("examples/fsm.sv")

    print("========== RTL ==========\n")
    print(rtl)

    print("\n=========================\n")

    tokens = tokenize(rtl)

    print("========== TOKENS ==========\n")

    for token in tokens:
        print(token)

    print("\n============================")


if __name__ == "__main__":
    main()