def tokenize_text(text):
    tokens = text.split()
    return tokens

if __name__ == "__main__":
    text = "Natural Language Processing is fun"

    tokens = tokenize_text(text)

    print("Tokens:")
    print(tokens)