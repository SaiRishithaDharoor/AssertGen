def read_rtl(filename):
    """
    Reads a SystemVerilog file and returns its contents as a string.
    """

    with open(filename, "r") as file:
        rtl = file.read()

    return rtl