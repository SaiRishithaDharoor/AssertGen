from parser.file_reader import read_rtl


def main():

    print("AssertGen v0.1")

    rtl = read_rtl("examples/counter.sv")

    print("\nReading RTL...\n")

    print("--------------------------------")
    print(rtl)
    print("--------------------------------")

    print("\nRTL loaded successfully.")


if __name__ == "__main__":
    main()