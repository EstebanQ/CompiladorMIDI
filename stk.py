from midiutil.MidiFile import MIDIFile

import random,AnalizadorSintactico as As

indice = 0

# NOTAS
aBem = 56 #Bem = bemol
a = 57
aSus = 58 #Sus = sostenido
bBem = 58
b = 59
cBem = 59
bSus = 60
c = 60
cSus = 61
dBem = 61
d = 62
dSus = 63
eBem = 63
e = 64
fBem = 64
eSus = 65
f = 65
fSus = 66
gBem = 66
g = 67
gSus = 68


# GRADOS DE LAS ESCALAS
MajorKey = ["I", "ii", "iii", "IV", "V", "vi", "viid"] #informativo
minorKey = ["i", "iid", "III", "iv", "v", "VI", "VII"] #informativo

# TONICAS DE LAS TONALIDADES (arreglos de notas a partir de los cuales se construyen los acordes de cada tonalidad)
CMajor = [c,d,e,f,g,a,b]
DMajor = [d,e,fSus,g,a,b,cSus]
EMajor = [e,fSus,gSus,a,b,cSus,dSus]
FMajor = [f,g,a,bBem,c,d,e]
GMajor = [g,a,b,c,d,e,fSus]
AMajor = [a,b,cSus,d,e,fSus,gSus]
BMajor = [b,cSus,dSus,e,fSus,gSus,aSus]
CbMajor = [cBem,dBem,eBem,fBem,gBem,aBem,bBem]
GbMajor = [gBem,aBem,bBem,cBem,dBem,eBem,f]
DbMajor = [dBem,eBem,f,gBem,aBem,bBem,c,dBem]
AbMajor = [aBem,bBem,c,dBem,eBem,f,g]
EbMajor = [eBem,f,g,aBem,bBem,c,d]
BbMajor = [bBem,c,d,eBem,f,g,a]
FsusMajor = [fSus,gSus,aSus,b,cSus,dSus,eSus]
CsusMajor = [cSus,dSus,eSus,fSus,gSus,aSus,bSus]
Abminor = [aBem,bBem,cBem,dBem,eBem,fBem,gBem]
Ebminor = [eBem,f,gBem,aBem,bBem,cBem,dBem]
Bbminor = [bBem,c,dBem,eBem,f,gBem,aBem]
Fminor = [f,g,aBem,bBem,c,dBem,eBem]
Cminor = [c,d,eBem,f,g,aBem,bBem,c]
Gminor = [g,a,bBem,c,d,eBem,f]
Dminor = [d,e,f,g,a,bBem,c]
Aminor = [a,b,c,d,e,f,g]
Eminor = [e,fSus,g,a,b,c,d]
Bminor = [b,cSus,d,e,fSus,g,a]
FSusminor =[fSus,gSus,a,b,cSus,d,e]
CSusminor = [cSus,dSus,e,fSus,gSus,a,b]
GSusminor = [gSus,aSus,b,cSus,dSus,e,fSus]
DSusminor = [dSus,eSus,fSus,gSus,aSus,b,cSus]
ASusminor = [aSus,bSus,cSus,dSus,eSus,fSus,gSus]

# GRADOS SIGUIENTES
sig1 = [1,2,3,4,5,6,7] #grados siguientes del 1er grado
sig2 = [1,2,5,6] #grados siguientes del 2do grado
sig3 = [3,6,4,7] #grados siguientes del 3er grado
sig4 = [1,4,5,7,6,2] #grados siguientes del 4to grado
sig5 = [1,5,6,2,4] #grados siguientes del 5to grado
sig6 = [6,2,5,4,7] #grados siguientes del 6to grado
sig7 = [1,2,4,5,6] #grados siguientes del 7mo grado

#Variables
progresion = []

mf = MIDIFile(1)  # only 1 track

arregloNotas = []

arregloOctavas = []

arregloRitmos = []

arregloVelocidades = []

arregloVolumenes = []

arregloGrados = []

arregloValores = []

#busca los siguientes para cada grado basado en los arreglos de SIGUIENTES
def siguientes(grade):
    if (grade == 1):
        sig = sig1
    if (grade == 2):
        sig = sig2
    if (grade == 3):
        sig = sig3
    if (grade == 4):
        sig = sig4
    if (grade == 5):
        sig = sig5
    if (grade == 6):
        sig = sig6
    if (grade == 7):
        sig = sig7
    return sig

#método recursivo para improvisation
def rec_improvisation(key,grade,grados,sigui,contador):
    #if (key == "CMajor"):
    tipoTonalidad = tonalidad(key)
    if (grados[0] in sigui):
        #sgte = siguientes(grados[0])
        contador = contador + 1.5
        note3 = asignarNota(key,grados[0]-1)
        #play3 = Major(note3, contador)
        play3 = tipoGrado(tipoTonalidad,grados[0],note3,contador)
        progresion.append(grados[0])
        # grados.remove(grados[0])
        End(key, grados[0], sigui, contador)
        #return
    else:
        next = random.choice(sigui)
        sigui = siguientes(next)
        contador = contador + 1.5
        note4 = asignarNota(key,next-1)
        #play4 = Major(note4, contador)
        play4 = tipoGrado(tipoTonalidad,next,note4,contador)
        progresion.append(next)
        rec_improvisation(key, grados[0], grados, sigui, contador)

    return

#método usado en improvisation para buscar la finalización de una progresión
def End(key, grade, sgte, contador): #terminar progresión
    tipoTonalidad = tonalidad(key)
    if(5 in sgte): # buscar el quinto grado para luego ir al primero y terminar
        quinto = asignarNota(key,4)
        contador = contador + 1.5
        #play = Major(quinto, contador)
        play = tipoGrado(tipoTonalidad,5,quinto,contador)
        progresion.append(5)

        primero = asignarNota(key,0)
        contador = contador + 1.5
        #play2 = Major(primero,contador)
        play2 = tipoGrado(tipoTonalidad,1,primero,contador)
        progresion.append(1)

    else:
        next = random.choice(sgte)
        sigui = siguientes(next)
        contador = contador + 1.5
        note5 = asignarNota(key,next-1)
        #play5 = Major(note5, contador)
        play5 = tipoGrado(tipoTonalidad,next,note5,contador)
        progresion.append(next)
        End(key, next, sigui, contador)
    return

#método que busca la calidad del grado(mayor, menor, aumentado o disminuido) dependiendo de si la tonalidad es Mayor o menor
def tipoGrado (tipoTonalidad,grado,nota,contador):
    if (tipoTonalidad == "Major"): #si la tonalidad es mayor
        if (grado == 1):
            Major(nota,contador)
        elif (grado == 2):
            minor(nota,contador)
        elif (grado == 3):
            minor(nota,contador)
        elif (grado == 4):
            Major(nota,contador)
        elif (grado == 5):
            Major(nota,contador)
        elif (grado == 6):
            minor(nota,contador)
        elif (grado == 7):
            diminished(nota,contador)
    elif (tipoTonalidad == "minor"): #si la tonalidad es menor
        if (grado == 1):
            minor(nota,contador)
        elif (grado == 2):
            diminished(nota,contador)
        elif (grado == 3):
            Major(nota,contador)
        elif (grado == 4):
            minor(nota,contador)
        elif (grado == 5):
            minor(nota,contador)
        elif (grado == 6):
            Major(nota,contador)
        elif (grado == 7):
            Major(nota,contador)
    return

#método que busca si la tonalidad ingresada por el usuario es Mayor o menor
def tonalidad(key):
    if "Major" in key:
        tipoTonalidad = "Major"
    elif "minor" in key:
        tipoTonalidad = "minor"
    return tipoTonalidad

#método principal para cuando el usuario ingresa una improvisation
def improvisation(key, grade1, grade2):
    global count
    grados = [grade1,grade2]
    tipoTonalidad = tonalidad(key)
    #if (key == "CMajor"):
    if (grade1 != 1 & grade2 != 1):
        if (grade1 == grade2):
            grades = [2, 3, 4, 5, 6, 7]
            grades.remove(grade1)
            grade1 = random.choice(grades)
            improvisation(key, grade1, grade2)
        else:
            primero = asignarNota(key,0)
            #play = Major(primero, count)
            play = tipoGrado(tipoTonalidad,1,primero,count)
            progresion.append(1)

            second = random.choice(grados)
            grados.remove(second)
            note2 = asignarNota(key,second-1)
            next2 = siguientes(second)
            count = count + 1.5
            #play1 = Major(note2,count)
            play1 = tipoGrado(tipoTonalidad,second,note2,count)
            progresion.append(second)
            rec_improvisation(key,grados[0],grados,next2,count)
    elif (grade1 == 1 & grade2 != 1):
        grades =[2,3,4,5,6,7]
        grades.remove(grade2)
        first = random.choice(grades)
        improvisation(key,first,grade2)
    elif (grade1 != 1 & grade2 == 1):
        grades = [2, 3, 4, 5, 6, 7]
        grades.remove(grade1)
        second = random.choice(grades)
        improvisation(key, grade1, second)
    elif (grade1 == 1 & grade2 == 1):
        grades = [2, 3, 4, 5, 6, 7]
        first = random.choice(grades)
        grades.remove(first)
        second = random.choice(grades)
        improvisation(key, first, second)

    llenar(arrNotas,arrRitmos,arrDuraciones)
    return

#llena los arreglos de notas, ritmos y duraciones provenientes del método improvisation, en el archivo midi
def llenar(arrNotas,arrRitmos,arrDuraciones):
    channel = 0 #canal del midi
    i = 0 #indice
    for elemento in arrNotas:
        volume = arregloVolumenes[indice] #volumen del midi
        #tempo = arregloVelocidades[indice] #velocidad
        mf.addProgramChange(track, channel, arrRitmos[i], int(As.instrumento))
        #mf.addTempo(track, arrRitmos[i], tempo)
        mf.addNote(track, channel, arrNotas[i], arrRitmos[i], arrDuraciones[i], volume)
        i = i+1
    return

#se llenan los arreglos con las notas base para cada grado
def asignarNota(key, nota):
    if (key == "CMajor"):
        nota = CMajor[nota]
    elif (key == "DMajor"):
        nota = DMajor[nota]
    elif (key == "EMajor"):
        nota = EMajor[nota]
    elif (key == "FMajor"):
        nota = FMajor[nota]
    elif (key == "GMajor"):
        nota = GMajor[nota]
    elif (key == "AMajor"):
        nota = AMajor[nota]
    elif (key == "BMajor"):
        nota = BMajor[nota]
    elif (key == "CbMajor"):
        nota = CbMajor[nota]
    elif (key == "GbMajor"):
        nota = GbMajor[nota]
    elif (key == "DbMajor"):
        nota = DbMajor[nota]
    elif (key == "AbMajor"):
        nota = AbMajor[nota]
    elif (key == "EbMajor"):
        nota = EbMajor[nota]
    elif (key == "BbMajor"):
        nota = BbMajor[nota]
    elif (key == "FsusMajor"):
        nota = FsusMajor[nota]
    elif (key == "CsusMajor"):
        nota = CsusMajor[nota]
    elif (key == "Abminor"):
        nota = Abminor[nota]
    elif (key == "Ebminor"):
        nota = Ebminor[nota]
    elif (key == "Bbminor"):
        nota = Bbminor[nota]
    elif (key == "Fminor"):
        nota = Fminor[nota]
    elif (key == "Cminor"):
        nota = Cminor[nota]
    elif (key == "Gminor"):
        nota = Gminor[nota]
    elif (key == "Dminor"):
        nota = Dminor[nota]
    elif (key == "Aminor"):
        nota = Aminor[nota]
    elif (key == "Eminor"):
        nota = Eminor[nota]
    elif (key == "Bminor"):
        nota = Bminor[nota]
    elif (key == "FSusminor"):
        nota = FSusminor[nota]
    elif (key == "CSusminor"):
        nota = CSusminor[nota]
    elif (key == "GSusminor"):
        nota = GSusminor[nota]
    elif (key == "DSusminor"):
        nota = DSusminor[nota]
    elif (key == "ASusminor"):
        nota = ASusminor[nota]
    return nota

#método que construye un grado si es Mayor
def Major(note, where):
    global count
    tonic = note
    mediant = note + 4
    dominant = note + 7
    list = [tonic, mediant, dominant]
    #beats = [where + 0.25, where + 0.5, where + 0.75, where + 1, where + 1.25]
    #random.shuffle(beats)
    # add some notes
    channel = 0
    volume = 100
    pitch = list[0]  # C4 (middle C)
    count = where  # start on beat 4
    duration = 1  # 1 beat long
    arrNotas.append(pitch)
    arrDuraciones.append(duration)
    arrRitmos.append(count)

    pitch = list[1]  # E4
    count = where  # start on beat 4
    duration = 1  # 1 beat long
    arrNotas.append(pitch)
    arrDuraciones.append(duration)
    arrRitmos.append(count)

    pitch = list[2]  # G4
    count = where  # start on beat 4
    duration = 1  # 1 beat long
    arrNotas.append(pitch)
    arrDuraciones.append(duration)
    arrRitmos.append(count)
    return

#método que construye un grado si es menor
def minor(note, where):
    global count
    tonic = note
    mediant = note+3
    dominant = note+7
    list = [tonic, mediant, dominant]
    beats = [where+0.25, where+0.5, where+0.75, where+1, where+1.25]
    #random.shuffle(beats)

    # add some notes
    channel = 0
    volume = 100
    pitch = list[0]  # C4 (middle C)
    count = where  # start on beat 4
    duration = 1  # 1 beat long
    arrNotas.append(pitch)
    arrDuraciones.append(duration)
    arrRitmos.append(count)

    pitch = list[1]  # E4
    count = where  # start on beat 4
    duration = 1  # 1 beat long
    arrNotas.append(pitch)
    arrDuraciones.append(duration)
    arrRitmos.append(count)

    pitch = list[2]  # G4
    count = where  # start on beat 4
    duration = 1  # 1 beat long
    arrNotas.append(pitch)
    arrDuraciones.append(duration)
    arrRitmos.append(count)
    return

#método que construye un grado si es aumentado
def augmented(note, where):
    global count
    tonic = note
    mediant = note+4
    dominant = note+8
    list = [tonic, mediant, dominant]
    beats = [where+0.25, where+0.5, where+0.75, where+1, where+1.25]
    # random.shuffle(beats)

    # add some notes
    channel = 0
    volume = 100
    pitch = list[0]  # C4 (middle C)
    count = where  # start on beat 4
    duration = 1  # 1 beat long
    arrNotas.append(pitch)
    arrDuraciones.append(duration)
    arrRitmos.append(count)

    pitch = list[1]  # E4
    count = where  # start on beat 4
    duration = 1  # 1 beat long
    arrNotas.append(pitch)
    arrDuraciones.append(duration)
    arrRitmos.append(count)

    pitch = list[2]  # G4
    count = where  # start on beat 4
    duration = 1  # 1 beat long
    arrNotas.append(pitch)
    arrDuraciones.append(duration)
    arrRitmos.append(count)
    return

#método que construye un grado si es disminuido
def diminished(note, where):
    global count
    tonic = note
    mediant = note+3
    dominant = note+6
    list = [tonic, mediant, dominant]
    beats = [where+0.25, where+0.5, where+0.75, where+1, where+1.25]
    # random.shuffle(beats)

    # add some notes
    channel = 0
    volume = 100
    pitch = list[0]  # C4 (middle C)
    count = where  # start on beat 4
    duration = 1  # 1 beat long
    arrNotas.append(pitch)
    arrDuraciones.append(duration)
    arrRitmos.append(count)

    pitch = list[1]  # E4
    count = where  # start on beat 4
    duration = 1  # 1 beat long
    arrNotas.append(pitch)
    arrDuraciones.append(duration)
    arrRitmos.append(count)

    pitch = list[2]  # G4
    count = where  # start on beat 4
    duration = 1  # 1 beat long
    arrNotas.append(pitch)
    arrDuraciones.append(duration)
    arrRitmos.append(count)
    return

#actualiza el arreglo de notas (para song) con base en los registros ingresados por el usuario(qué tan aguda o grave desea una nota)
def octava(arrNotas,arrRegistros):
    index = 0
    for nota in arrNotas:
        if (arrRegistros[index] == 1 ):
            arrNotas[index] = arrNotas[index]-24
        elif (arrRegistros[index] == 2):
            arrNotas[index] = arrNotas[index]-12
        elif (arrRegistros[index] == 4):
            arrNotas[index] = arrNotas[index]+12
        elif (arrRegistros[index] == 5):
            arrNotas[index] = arrNotas[index]+24
        index = index+1
    return

# estrellitaNotas = [a,a,e,e,fSus,fSus,e,d,d,cSus,cSus,b,b,a]
# estrellitaRitmos = [1,1,1,1,1,1,2,1,1,1,1,1,1,2]
#starWarsNotas = [a,e,d,cSus,b,a,e,d,cSus,b,a,e,d,cSus,d,b]
#starWarsRitmos = [2,3,1/4,1/4,1/2,2,1,1/4,1/4,1/2,2,1,1/4,1/4,1/2,4]
#starWarsOctavas = [3,3,3,3,3,4,3,3,3,3,4,3,3,3,3,3]

arrNotas = []
arrRitmos = []
arrDuraciones = []

#método para construir una canción a partir de las notas y demás datos ingresados por el usuario
def song(notas,ritmos,registros): # recibe un arreglo de notas, un arreglo de ritmos y uno de registros(octavas)
    convertirArreglo(notas)
    index = 0
    time = 0
    duration = 0
    track = 0  # the only track
    octava(notas,registros)
    mf.addTrackName(track, time, "Sample Track")
    for nota in notas:
        channel = 0
        #volume = 100
        volume = arregloVolumenes[index]
        tempo = arregloVelocidades[index]
        pitch = nota  # C4 (middle C)
        time = time+duration  # start on
        if (index < len(notas)):
            duration = ritmos[index]  # beat long
        #mf.addTempo(track, time, 180)
        mf.addProgramChange(track,channel,time,int(As.instrumento))
        mf.addTempo(track, time, tempo)
        mf.addNote(track, channel, pitch, time, duration, volume)
        index = index+1
    return

#convierte los componentes del arreglo de string a int
def convertirArreglo(arreglo):
    i = 0
    for var in arreglo:
        if (var == "aBem"):
            arreglo[i] = aBem
        elif (var == "a"):
            arreglo[i] = a
        elif (var == "aSus"):
            arreglo[i] = aSus
        elif (var == "bBem"):
            arreglo[i] = bBem
        elif (var == "b"):
            arreglo[i] = b
        elif (var == "bSus"):
            arreglo[i] = bSus
        elif (var == "cBem"):
            arreglo[i] = cBem
        elif (var == "c"):
            arreglo[i] = c
        elif (var == "cSus"):
            arreglo[i] = cSus
        elif (var == "dBem"):
            arreglo[i] = dBem
        elif (var == "d"):
            arreglo[i] = d
        elif (var == "dSus"):
            arreglo[i] = dSus
        elif (var == "eBem"):
            arreglo[i] = eBem
        elif (var == "e"):
            arreglo[i] = e
        elif (var == "eSus"):
            arreglo[i] = eSus
        elif (var == "fBem"):
            arreglo[i] = fBem
        elif (var == "f"):
            arreglo[i] = f
        elif (var == "fSus"):
            arreglo[i] = fSus
        elif (var == "gBem"):
            arreglo[i] = gBem
        elif (var == "g"):
            arreglo[i] = g
        elif (var == "gSus"):
            arreglo[i] = gSus
        i = i+1

#mf.addTrackName(track, time, "Sample Track")
#mf.addTempo(track, time, 180)
#mf.addTempo(track, 10, 90)

#imp1 = improvisation("Gminor",1,4)
#song(arrNotas,arrRitmos)
#song(starWarsNotas,starWarsRitmos,starWarsOctavas)
track = 0
count = 0
titulo = ""

#main
def funcion(filen):
    global indice,count,titulo,arregloNotas,arregloOctavas,arregloRitmos,arregloVelocidades,arregloVolumenes,arregloGrados,mf
    indice = 0
    count = 0
    titulo = As.titulo
    arregloNotas = []
    arregloOctavas = []
    arregloRitmos = []
    arregloVelocidades = []
    arregloVolumenes = []
    arregloGrados = []

    mf = MIDIFile(1)

    if As.tipo == "song":
        #Se acomodan todos los valores en un solo arreglo de cada tipo(arreglo de notas, octavas, ritmos, etc.)
        posiciones = [0]
        x = 0
        for y in As.notas:
            if y == '-':
                posiciones.append(x+1)
            x += 1

        x = 0
        for y in As.estructura1:
            for i in range(posiciones[y-1],posiciones[y]-1):
                arregloNotas.append(As.notas[i])
                arregloOctavas.append(As.octavas[i])
                arregloRitmos.append(As.ritmos[i])
                arregloVelocidades.append(As.estructura2[x])
                arregloVolumenes.append(As.estructura3[x])
            x += 1

        mf.addTrackName(track, count, "Sample Track")

        song(arregloNotas,arregloRitmos,arregloOctavas)

        try:
            with open(filen, 'wb') as outf:
                mf.writeFile(outf)
            return 0
        except:
            -1

    else:
        # Se acomodan todos los valores en un solo arreglo de cada tipo(arreglo de notas, octavas, ritmos, etc.)
        posiciones = [0]
        x = 0
        for y in As.grados:
            if y == '-':
                posiciones.append(x + 1)
            x += 1

        x = 0
        print(As.estructura3)
        for y in As.estructura1:
            for i in range(posiciones[y - 1], posiciones[y] - 1):
                arregloGrados.append(As.grados[i])
                arregloVolumenes.append(As.estructura3[x])
            x += 1

        mf.addTrackName(track, count, "Sample Track")
        mf.addTempo(track, 0, 80)

        print(arregloGrados,arregloVolumenes)
        for i in range(0,len(arregloGrados),2):
            indice = i
            improvisation(As.tonalidad,arregloGrados[i],arregloGrados[i+1])

        try:
            with open(filen, 'wb+') as outf:
                mf.writeFile(outf)
            return 0
        except:
            -1