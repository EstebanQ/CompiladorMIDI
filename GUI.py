# ----------------------------------------------------------------------
# Autores: Esteban Quiros y Yohel Muñoz
#
# Editor para archivos con compilador integrado
# ----------------------------------------------------------------------

import tkinter as tki,AnalizadorLexico,AnalizadorSintactico,stk
from tkinter import filedialog,messagebox

#Metodo que genera un nuevo archivo
def new():
    txt.delete('1.0',"end-1c")
    global filename
    filename = ""
    filemenu.entryconfig(2, state=tki.DISABLED)

#Metodo que abre un archivo preexistente
def openf():
    txt.delete('1.0', "end-1c")
    filen = filedialog.askopenfilename()
    file = open(filen)
    input = file.readlines()
    for line in input:
        txt.insert("end-1c",line)
    global filename
    filename = filen
    filemenu.entryconfig(2, state="normal")

#Metodo que guarda un archivo con su nombre
def save():
    output = txt.get('1.0', "end-1c")
    efile = open(filename, 'w+')
    efile.write(output)

#Metodo que guarda un nuevo archivo
def saveas():
    filen = filedialog.asksaveasfilename(defaultextension = '.txt',filetypes=[("Text files","*.txt")])
    output = txt.get('1.0',"end-1c")
    efile = open(filen, 'w+')
    efile.write(output)
    global filename
    filename = filen
    filemenu.entryconfig(2, state="normal")

#Metodo que genera el archivo MIDI
def midi():
    if txt.get('1.0',"end-1c") == "":
        tki.messagebox._show("Error","Cannot generate Midi from empty file.")

    else:
        error = AnalizadorLexico.analisisLexico(txt.get('1.0',"end-1c"))
        if error != "":
            tki.messagebox._show("Lexical error", error)
            return
        error = AnalizadorSintactico.analisisSintactico(txt.get('1.0', "end-1c"))
        if error == "":
            filen = filedialog.asksaveasfilename(initialfile = AnalizadorSintactico.titulo,filetypes = [("Midi files", "*.mid")],defaultextension = '.mid')
            stk.funcion(filen)
            tki.messagebox._show("Success","Midi generated.")
            return
        else:
            tki.messagebox._show("Syntactic error", error)
            return

root = tki.Tk()

root.iconbitmap("icon.ico")
root.state("zoomed")
root.title("MIDI Compiler")

filename = ""

txt_frm = tki.Frame(root, width=1000, height=700)
txt_frm.pack(fill="both", expand=True)
txt_frm.grid_propagate(False)
txt_frm.grid_rowconfigure(0, weight=1)
txt_frm.grid_columnconfigure(0, weight=1)

txt = tki.Text(txt_frm, borderwidth=3, relief="sunken")
txt.config(font=("consolas", 12), undo=True, wrap='word')
txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

scrollb = tki.Scrollbar(txt_frm, command=txt.yview)
scrollb.grid(row=0, column=1, sticky='nsew')
txt['yscrollcommand'] = scrollb.set

menubar = tki.Menu(root)
filemenu = tki.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Open", command=openf)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Save as...", command=saveas)
filemenu.entryconfig(2,state=tki.DISABLED)

filemenu.add_separator()

filemenu.add_command(label="Generate MIDI", command=midi)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()