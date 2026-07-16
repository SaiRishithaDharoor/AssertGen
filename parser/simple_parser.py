def get_module_name(tokens):

    for i in range(len(tokens)):

        token = tokens[i]

        if (
            token.token_type == "KEYWORD"
            and token.value == "module"
        ):

            return tokens[i + 1].value

    return None