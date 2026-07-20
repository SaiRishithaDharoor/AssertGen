from rtl_ast.file import File
from rtl_ast.module import Module
from rtl_ast.port import Port
from rtl_ast.datatype import DataType
from rtl_ast.signal import Signal
from rtl_ast.procedural_block import ProceduralBlock
from rtl_ast.sensitivity import Sensitivity
from rtl_ast.statement_block import StatementBlock

class Parser:

    def __init__(self, tokens):

        self.tokens = tokens
        self.position = 0

    def current_token(self):

        if self.position >= len(self.tokens):
            return None

        return self.tokens[self.position]

    def advance(self):

        self.position += 1

    def expect(self, token_type, value=None):

        token = self.current_token()

        if token is None:
            raise SyntaxError("Unexpected end of file")

        if token.token_type != token_type:
            raise SyntaxError(
                f"Expected {token_type}, found {token.token_type}"
            )

        if value is not None and token.value != value:
            raise SyntaxError(
                f"Expected '{value}', found '{token.value}'"
            )

        self.advance()

        return token
    
    def parse_file(self):

        file = File()

        while self.current_token() is not None:

            module = self.parse_module()

            file.add_module(module)

        return file

    def peek(self, offset=1):

        index = self.position + offset

        if index >= len(self.tokens):
            return None

        return self.tokens[index]
    
    def parse_module(self):

        # -------------------------
        # module
        # -------------------------
        self.expect("KEYWORD", "module")

        # Module name
        name_token = self.expect("IDENTIFIER")

        module = Module(name_token.value)

        # (
        self.expect("SYMBOL", "(")

        # -------------------------
        # Parse ports
        # -------------------------
        ports = self.parse_port_list()

        for port in ports:
            module.add_port(port)

        # )
        self.expect("SYMBOL", ")")

        # ;
        self.expect("SYMBOL", ";")

        # -------------------------
        # Parse module body
        # -------------------------
        while True:

            token = self.current_token()

            if token is None:
                raise SyntaxError("Unexpected EOF inside module")

            # End of module
            if token.token_type == "KEYWORD" and token.value == "endmodule":
                break

            # Signal declaration
            if token.token_type == "KEYWORD" and token.value == "logic":

                signal = self.parse_signal()

                module.add_signal(signal)

                continue

            # Procedural block
            if (
                token.token_type == "KEYWORD"
                and token.value in ("always_ff", "always_comb")
            ):

                block = self.parse_always_block()

                module.add_procedural_block(block)

                continue

            raise SyntaxError(
                f"Unexpected token inside module: {token}"
            )

        # -------------------------
        # endmodule
        # -------------------------
        self.expect("KEYWORD", "endmodule")

        return module

    def parse_port_list(self):

        ports = []

        while True:

            token = self.current_token()

            if token is None:
                raise SyntaxError("Unexpected EOF while parsing ports")

            if token.token_type == "SYMBOL" and token.value == ")":
                break

            port = self.parse_port()

            ports.append(port)

            token = self.current_token()

            if token.token_type == "SYMBOL" and token.value == ",":
                self.advance()

        return ports
    
    def parse_port(self):

        direction = self.parse_direction()

        datatype = self.parse_datatype()

        name = self.expect("IDENTIFIER")

        return Port(
            name=name.value,
            direction=direction,
            datatype=datatype
        )
    
    def parse_direction(self):

        token = self.current_token()

        if token.value not in ("input", "output", "inout"):

            raise SyntaxError(
                f"Expected port direction, found {token.value}"
            )

        self.advance()

        return token.value
    
    def parse_datatype(self):

        token = self.current_token()

        if token.value != "logic":

            raise SyntaxError(
                f"Expected datatype, found {token.value}"
            )

        self.advance()

        width = None

        token = self.current_token()

        if token.token_type == "SYMBOL" and token.value == "[":

            self.advance()

            msb = self.expect("NUMBER")

            self.expect("SYMBOL", ":")

            lsb = self.expect("NUMBER")

            self.expect("SYMBOL", "]")

            width = f"[{msb.value}:{lsb.value}]"

        return DataType(
            kind="logic",
            width=width,
            signed=False
        )
        

    def parse_signal(self):

        datatype = self.parse_datatype()

        name = self.expect("IDENTIFIER")

        self.expect("SYMBOL", ";")

        return Signal(
            name=name.value,
            datatype=datatype
        )
    
    def parse_always_block(self):

        kind = self.expect("KEYWORD").value

        self.expect("SYMBOL", "@")

        self.expect("SYMBOL", "(")

        sensitivity = self.parse_sensitivity()

        self.expect("SYMBOL", ")")

        body = self.parse_statement_block()

        return ProceduralBlock(
            kind=kind,
            sensitivity=sensitivity,
            body=body
        )
    
    def parse_sensitivity(self):

        edge = self.expect("IDENTIFIER")

        signal = self.expect("IDENTIFIER")

        return Sensitivity(
            edge=edge.value,
            signal=signal.value
        )
    
    def parse_statement_block(self):

        block = StatementBlock()

        self.expect("KEYWORD", "begin")

        while True:

            token = self.current_token()

            if token.token_type == "KEYWORD" and token.value == "end":
                break

            self.advance()

        self.expect("KEYWORD", "end")

        return block
    
