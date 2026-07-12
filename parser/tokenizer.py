import re

from models.token import Token


KEYWORDS = {
    "module",
    "endmodule",
    "input",
    "output",
    "logic",
    "always_ff",
    "always_comb",
    "begin",
    "end",
    "if",
    "else"
}


SYMBOLS = {
    "(",
    ")",
    "[",
    "]",
    "{",
    "}",
    ";",
    ",",
    "@",
    ":"
}


def tokenize(text):

    tokens = []

    words = re.findall(r"[A-Za-z_]\w*|\d+|<=|==|!=|[^\s]", text)

    for word in words:

        if word in KEYWORDS:
            tokens.append(Token("KEYWORD", word))

        elif word in SYMBOLS:
            tokens.append(Token("SYMBOL", word))

        elif word.isdigit():
            tokens.append(Token("NUMBER", word))

        else:
            tokens.append(Token("IDENTIFIER", word))

    return tokens