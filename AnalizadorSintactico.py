# ----------------------------------------------------------------------
# Autores: Esteban Quiros y Yohel Muñoz
#
# Analizador Lexico compilador de generador de archivos midi
# ----------------------------------------------------------------------

import AnalizadorLexico ,ply.yacc as yacc, sys

from AnalizadorLexico import tokens

def p_principal(t):
    'principal : FILENAME SCONST AUTHOR SCONST INSTRUMENT ICONST song structure'
    t[0] = t[5]

def p_principal2(t):
    'principal : FILENAME SCONST AUTHOR SCONST INSTRUMENT ICONST improv structure'
    t[0] = t[5]

def p_song(t):
    'song : SONG COLON notesLines'
    pass

def p_notesLines(t):
    'notesLines : notesLine notesLines'
    pass

def p_notesLines2(t):
    'notesLines : notesLine'
    pass

def p_notesLine(t):
    'notesLine : notes LBRACKET ICONST RBRACKET'
    pass

def p_notes(t):
    'notes : note notes'
    pass

def p_notes2(t):
    'notes : note'
    pass

def p_note(t):
    'note : NCONST LPAREN ICONST COMMA ICONST RPAREN'
    pass

def p_note2(t):
    'note : NCONST LPAREN ICONST COMMA FCONST RPAREN'
    pass

def p_improv(t):
    'improv : IMPROVISATION LPAREN KCONST RPAREN COLON degreeLines'
    pass

def p_degreeLines(t):
    'degreeLines : degreeLine degreeLines'
    pass

def p_degreeLines2(t):
    'degreeLines : degreeLine'
    pass

def p_degreeLine(t):
    'degreeLine : degrees LBRACKET ICONST RBRACKET'
    pass

def p_degrees(t):
    'degrees : degree degrees'
    pass

def p_degrees2(t):
    'degrees : degree'
    pass

def p_degree(t):
    'degree : DCONST LPAREN ICONST RPAREN'
    pass

def p_structure(t):
    'structure : STRUCTURE LBRACE repeat RBRACE'
    pass

def p_repeat(t):
    'repeat : repeatValues COMMA repeat'
    pass

def p_repeat2(t):
    'repeat : repeatValues'
    pass

def p_repeatValues(t):
    'repeatValues : ICONST LPAREN ICONST COMMA ICONST RPAREN'
    pass

def p_error(p):
    print("Syntax error in input!")
    print(p)

if len(sys.argv) > 1:
    parser = yacc.yacc(method='LALR')
    entrada = sys.argv[1]
    file = open(entrada)
    if len(sys.argv) > 2:
        salida = sys.argv[2]
        efile = open(salida, 'w+')
    else:
        efile = open('Salida.txt', 'w+')
    s = ""
    for line in file.readlines():
        s += line
    result = parser.parse(s)
    print(result)
