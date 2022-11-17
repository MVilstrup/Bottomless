from bottomless.api.language.base import generate_type

NAME = generate_type(token="NAME", tag=r'[a-zA-Z_][a-zA-Z0-9_]*')

INDENT = generate_type(token="INDENT", tag=r"(?P<indent>^ *)")
INDENT_MATCH = generate_type(token="INDENT_MATCH", tag=r"(?P=indent)")
VAR = generate_type(token="VAR", tag=r"(?P<variable>.+?)\s*:")
VALUE = generate_type(token="VALUE", tag=r"(?P<value>(?:(?P<q2>['\"]).*?(?P=q2))|[^#]+?)")
STR_VALUE = generate_type(token="STR_VALUE", tag=r"((?:(?P<q2>['\"]).*?(?P=q2))|[^#]+?)")
NEWLINE = generate_type(token="NEWLINE", tag=r"$\n")
OPT_NEWLINE = generate_type(token="OPT_NEWLINE", tag=r"$\n?")
BLANK = generate_type(token="BLANK", tag=r" +")
INLINE_COMMENT = generate_type(token="INLINE_COMMENT", tag=r"(?: +#.*)?")

Comment = generate_type(token="COMMENT", tag=r"^ *#.*" + NEWLINE.tag, multi=True)
BlankLine = generate_type(token="BLANK_LINE", tag=r"^[ \t]*" + NEWLINE.tag, multi=True)
Dashes = generate_type(token="DASHES", tag=r"^---" + NEWLINE.tag, multi=True)
Section = generate_type(token="SECTION",
                        tag=(INDENT.tag
                             + VAR.tag
                             + INLINE_COMMENT.tag
                             + NEWLINE.tag),
                        multi=True)

SimpleType = generate_type(token="SIMPLE",
                           tag=(INDENT.tag
                                + VAR.tag
                                + BLANK.tag
                                + VALUE.tag
                                + INLINE_COMMENT.tag
                                + OPT_NEWLINE.tag),
                           multi=True)

MultiLine = generate_type(token="MULTILINE",
                          tag=(INDENT.tag
                               + VAR.tag
                               + BLANK.tag
                               + r"(?P<blockstyle>[>|])(?P<chomping>[+-]?)(?P<forceindent>\d*) *"
                               + INLINE_COMMENT.tag
                               + NEWLINE.tag
                               ),
                          multi=True)

MultiLineString = generate_type(token="MULTILINE_STR",
                                tag=(INDENT_MATCH.tag
                                     + BLANK.tag
                                     + STR_VALUE.tag
                                     + NEWLINE.tag
                                     + r"|"
                                     + BlankLine.tag),
                                multi=True)

MultiLineSection = generate_type(token="MULTILINE_SECTION",
                                 tag=(MultiLine.tag
                                      + r"(?P<lines>(?:"
                                      + MultiLineString.tag
                                      + r")*" + r")"),
                                 multi=True)

ListValue = generate_type(token="LIST_VALUE",
                          tag=(BLANK.tag
                               + r"-"
                               + BLANK.tag
                               + r"('.*?'|\".*?\"|[^#\n]+?)"
                               + INLINE_COMMENT.tag
                               + OPT_NEWLINE.tag),
                          multi=True)

ListItem = generate_type(token="LIST_ITEM",
                         tag=(BlankLine.tag
                              + r"|"
                              + Comment.tag
                              + r"|"
                              + ListValue.tag),
                         multi=True)

List = generate_type(token="LIST",
                     tag=(Section.tag
                          + r"(?P<items>(?:"
                          + ListItem.tag
                          + r")*"
                          + ListValue.tag + r")"),
                     multi=True)

NullType = generate_type(token="Null", tag=r"\b(null|Null|NULL)\b|~")
TrueType = generate_type(token="TRUE", tag=r"\b(true|True|TRUE)\b")
FalseType = generate_type(token="FALSE", tag=r"\b(false|False|FALSE)\b")
IntegerType = generate_type(token="Integer", tag=r"[-+]?[0-9]+")
FloatType = generate_type(token="Float", tag=r"([-+]?(\.[0-9]+|[0-9]+(\.[0-9]*)?)([eE][-+]?[0-9]+)?)")
StringType = generate_type(token="String", tag=r"(?P<quotes>['\"]?).*(?P=quotes)")
