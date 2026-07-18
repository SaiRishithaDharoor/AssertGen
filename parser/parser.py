class Parser:
    
    print("Loading parser.py")
    def __init__(self, tokens):

        self.tokens = tokens
        self.position = 0

        print("=== Parser Created ===")
        print("Position:", self.position)
        print("Number of tokens:", len(self.tokens))
    
    def current_token(self):

        print("\n=== current_token() ===")
        print("Position:", self.position)
        print("Length:", len(self.tokens))

        if self.position >= len(self.tokens):
            print("Returning None")
            return None

        print("Returning:", self.tokens[self.position])

        return self.tokens[self.position]