# ----------------------------------------------------------------------
# Autores: Esteban Quiros y Yohel Muñoz
#
# Analizador Sintactico compilador de generador de archivos midi
# ----------------------------------------------------------------------

import ply.yacc as yacc
from AnalizadorLexico import tokens

largoA = 0

error = ""

instrumento = 0

tipo = ""

titulo = ""

tonalidad = ""

notas = []

ritmos = []

octavas = []

grados = []

estructura1 = []

estructura2 = []

estructura3 = []

#Estructura principal del archivo
def p_principal(t):
    'principal : FILENAME SCONST AUTHOR SCONST INSTRUMENT ICONST song structureSong'
    global instrumento,titulo
    instrumento = t[6]
    titulo = t[2]
    titulo += "By"
    titulo += t[4]
    titulo = titulo.replace("\"", "")

def p_principal2(t):
    'principal : FILENAME SCONST AUTHOR SCONST INSTRUMENT ICONST improv structureImprovisation'
    global instrumento,titulo
    instrumento = t[6]
    titulo = t[2]
    titulo += "By"
    titulo += t[4]
    titulo = titulo.replace("\"", "")

#Estructura de una cancion (cancion implica que una persona ingresara todas las notas)
def p_song(t):
    'song : SONG COLON notesLines'
    global tipo
    tipo = "song"

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
    notas.append('-')
    octavas.append('-')
    ritmos.append('-')

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
    nota = t[1]
    nota = nota.lower()
    notaV = nota[0]
    if len(nota) > 1:
        if nota[1] == '#':
            notaV += 'Sus'
        else:
            notaV += 'Bem'
    notas.append(notaV)
    octavas.append(int(t[3]))
    ritmos.append(float(t[5]))


def p_note2(t):
    'note : NCONST LPAREN ICONST COMMA FCONST RPAREN'
    nota = t[1]
    nota = nota.lower()
    notaV = nota[0]
    if len(nota) > 1:
        if nota[1] == '#':
            notaV += 'Sus'
        else:
            notaV += 'Bem'
    notas.append(notaV)
    octavas.append(int(t[3]))
    ritmo = t[5]
    ritmos.append(float(ritmo[0])/float(ritmo[2]))

#Estructura de una improvisacion(improvisacion implica que la persona ingresera solo unos valores y el compilador generara el resto)
def p_improv(t):
    'improv : IMPROVISATION LPAREN KCONST RPAREN COLON degreeLines'
    global tipo,tonalidad
    tipo = "improvisation"
    t = t[3]
    tonalidad = t[0]
    if len(t) == 3:
        if t[2] == '#':
            tonalidad += 'Sus'
        else:
            tonalidad += 'b'
    if t[1] == 'm':
        tonalidad += 'minor'
    if t[1] == 'M':
        tonalidad += 'Major'

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
    grados.append('-')
    valores.append('-')

#Grados musicales
def p_degrees(t):
    'degrees : degree degree'
    pass

def p_degrees2(t):
    'degrees : degree'
    pass

#Grado musical
def p_degree(t):
    'degree : ICONST'
    degree = t[1]
    grados.append(int(degree[0]))

#Estructura
def p_structureSong(t):
    'structureSong : STRUCTURE LBRACE repeatSong RBRACE'
    pass

def p_structureImprovisation(t):
    'structureImprovisation : STRUCTURE LBRACE repeatImprovisation RBRACE'
    pass

#Conjunto de valores a repetir
def p_repeatSong(t):
    'repeatSong : repeatValuesSong COMMA repeatSong'
    pass

def p_repeat2Song(t):
    'repeatSong : repeatValuesSong'
    pass

#Valor a repetir
def p_repeatValuesSong(t):
    'repeatValuesSong : ICONST LPAREN ICONST COMMA ICONST RPAREN'
    estructura1.append(int(t[1]))
    estructura2.append(int(t[3]))
    estructura3.append(int(t[5]))

#Conjunto de valores a repetir
def p_repeatImprovisation(t):
    'repeatImprovisation : repeatValuesImprovisation COMMA repeatImprovisation'
    pass

def p_repeat2Improvisation(t):
    'repeatImprovisation : repeatValuesImprovisation'
    pass

#Valor a repetir
def p_repeatValuesImprovisation(t):
    'repeatValuesImprovisation : ICONST LPAREN ICONST RPAREN'
    estructura1.append(int(t[1]))
    estructura3.append(int(t[3]))

def p_error(p):
    global error
    error = " Syntactic Error: Illegal expression '%s'" % p.value + " at line " + str(p.lineno - largoA)
    print (error)

def analisisSintactico(input):

    global error,notas,ritmos,octavas,grados,valores,estructura1,estructura2,estructura3,largoA
    largoA = input.count("\n")
    error = ""
    notas = []
    ritmos = []
    octavas = []
    grados = []
    valores = []
    estructura1 = []
    estructura2 = []
    estructura3 = []


    parser = yacc.yacc(method='LALR')
    try:
        parser.parse(input)
    except:
        pass
    return error
