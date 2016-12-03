# ----------------------------------------------------------------------
# Autores: Esteban Quiros y Yohel Muñoz
#
# Analizador Sintactico compilador de generador de archivos midi
# ----------------------------------------------------------------------

import ply.yacc as yacc, sys

from AnalizadorLexico import tokens

error = ""

#Estructura principal del archivo
def p_principal(t):
    'principal : FILENAME SCONST AUTHOR SCONST INSTRUMENT ICONST song structure'
    t[0] = t[5]

def p_principal2(t):
    'principal : FILENAME SCONST AUTHOR SCONST INSTRUMENT ICONST improv structure'
    t[0] = t[5]

#Estructura de una cancion (cancion implica que una persona ingresara todas las notas)
def p_song(t):
    'song : SONG COLON notesLines'
    pass

#Lineas de definicion de notas
def p_notesLines(t):
    'notesLines : notesLine notesLines'
    pass

def p_notesLines2(t):
    'notesLines : notesLine'
    pass

#Linea(Singular) de definicion de notas
def p_notesLine(t):
    'notesLine : notes LBRACKET ICONST RBRACKET'
    pass

#Conujnto de notas
def p_notes(t):
    'notes : note notes'
    pass

def p_notes2(t):
    'notes : note'
    pass

#Nota
def p_note(t):
    'note : NCONST LPAREN ICONST COMMA ICONST RPAREN'
    pass

def p_note2(t):
    'note : NCONST LPAREN ICONST COMMA FCONST RPAREN'
    pass

#Estructura de una improvisacion(improvisacion implica que la persona ingresera solo unos valores y el compilador generara el resto)
def p_improv(t):
    'improv : IMPROVISATION LPAREN KCONST RPAREN COLON degreeLines'
    pass

#Lineas de grados musicales
def p_degreeLines(t):
    'degreeLines : degreeLine degreeLines'
    pass

def p_degreeLines2(t):
    'degreeLines : degreeLine'
    pass

#Linea(Singular) de grados musicales
def p_degreeLine(t):
    'degreeLine : degrees LBRACKET ICONST RBRACKET'
    pass

#Grados musicales
def p_degrees(t):
    'degrees : degree degrees'
    pass

def p_degrees2(t):
    'degrees : degree'
    pass

#Grado musical
def p_degree(t):
    'degree : DCONST LPAREN ICONST RPAREN'
    pass

#Estructura
def p_structure(t):
    'structure : STRUCTURE LBRACE repeat RBRACE'
    pass

#Conjunto de valores a repetir
def p_repeat(t):
    'repeat : repeatValues COMMA repeat'
    pass

def p_repeat2(t):
    'repeat : repeatValues'
    pass

#Valor a repetir
def p_repeatValues(t):
    'repeatValues : ICONST LPAREN ICONST COMMA ICONST RPAREN'
    pass

def p_error(p):
    global error
    error = " Sintactical Error: Illegal expression '%s'" % p.value

def analisisSintactico(input):
    global error
    error = ""
    parser = yacc.yacc(method='LALR')
    try:
        parser.parse(input)
    except:
        pass
    return error
