class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def current_token(self):
        pass

    def advance(self):
        pass

    def expect(self, token_type, value=None):
        pass

    def parse_file(self):
        pass

    def parse_module(self):
        pass