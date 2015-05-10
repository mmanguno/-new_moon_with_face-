class Token:
    """
    A Token is a "block" of text. It consists of the text
    from the markdown file (self. text), as well as a type
    of formatting (self.type): whether it's underlined,
    italicized, a header, and so on.
    """

    def __init__(self, start):
        """
        Constructs a token, where start is the
        starting character.
        """
        self.text = start.text
        self.type = None
