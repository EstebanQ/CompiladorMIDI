# ----------------------------------------------------------------------
# Autores: Esteban Quiros y Yohel Muñoz
#
# Analizador Lexico compilador de generador de archivos midi
# ----------------------------------------------------------------------

import sys

sys.path.insert(0, "../..")

import ply.lex as lex

error = ""

tokens = (
    #Palabras Reservadas
    'FILENAME', 'AUTHOR', 'INSTRUMENT', 'SONG', 'STRUCTURE', 'IMPROVISATION',

    #Literales integer constant, string constant,fraction constant, notes constants, degrees constants, key constants
    'ICONST','SCONST','FCONST','NCONST','DCONST','KCONST',

    #Delimitadores ( ) [ ] { } , :
    'LPAREN', 'RPAREN',
    'LBRACKET', 'RBRACKET',
    'LBRACE', 'RBRACE',
    'COMMA','COLON'
)

# Completely ignored characters
t_ignore = ' \t\x0c'


# Newlines
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# Delimeters
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_COLON = r':'

#Palabras reservadas
t_FILENAME = r'filename'

t_AUTHOR = r'author'

t_INSTRUMENT = r'instrument'

t_SONG = r'song'

t_STRUCTURE = r'structure'

t_IMPROVISATION = r'improvisation'

# Integer literal
t_ICONST = r'\d+'

# String literal
t_SCONST = r'\"([^\\\n]|(\\.))*?\"'

# Fraction literal
t_FCONST = r'1/[24816]'

# Degrees literal
t_DCONST = r'[1234567][MmAd]'

# Key literal
t_KCONST = r'CM|Am|FM|Dm|GM|Em|BMb|Gm|DM|Bm|EMb|Cm|AM|Fm\#|AMb|Fm|EM|Cm\#|DMb|Bmb|BM|Gm\#|GMb|Emb|FM\#|Dm\#|CMb|Amb|CM\#|Am\#'

# Note literal
t_NCONST = r'[ABCDEFG][b#]*'

# Comments
def t_comment(t):
    r' /\*(.|\n)*?\*/'
    t.lineno += t.value.count('\n')


# Preprocessor directive (ignored)
def t_preprocessor(t):
    r'\#(.)*?\n'
    t.lineno += 1


def t_error(t):
    global error
    error = " Lexical Error: Illegal character at line " + str(t.lineno)


def analisisLexico(input):
    global error
    error = ""
    lexer = lex.lex()
    lexer.input(input)
    try:
        token = lexer.token()
    except:
        pass
    while token:
        try:
            token = lexer.token()
        except:
            pass
            break
    return error