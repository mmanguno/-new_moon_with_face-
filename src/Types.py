#--------------------------------------------------------#
# This class contains a list of types for Token objects. #
#--------------------------------------------------------#
import string

UNFORMATTED = string.letters + string.digits + string.whitespace + "." + ","

HEADER_1 = "#"
HEADER_2 = "##"
HEADER_3 = "###"
HEADER_4 = "####"
HEADER_5 = "#####"
HEADER_6 = "######"

BLOCKQUOTE = ">"

ITALIC = "*" + "_"
BOLD = "**" + "__"

# LIST_ORDERED = string.digits + "."

LIST_UNORDERED = "* " + "- " + "+ "

LINK = "("
LINK_TEXT = "["

CODE_INLINE = "`"
CODE_MULTIPLE = "```"
