import tkinter as tki,AnalizadorLexico,AnalizadorSintactico
from tkinter import filedialog

def new():
    txt.delete('1.0',"end-1c")
    global filename
    filename = ""

def openf():
    txt.delete('1.0', "end-1c")
    filen = filedialog.askopenfilename()
    file = open(filen)
    input = file.readlines()
    for line in input:
        txt.insert("end-1c",line)
    global filename
    filename = filen

def save():
    output = txt.get('1.0', "end-1c")
    efile = open(filename, 'w+')
    efile.write(output)


def saveas():
    filen = filedialog.asksaveasfilename()
    output = txt.get('1.0',"end-1c")
    efile = open(filen, 'w+')
    efile.write(output)
    global filename
    filename = filen

def midi():
    filewin = tki.Toplevel(root)
    button = tki.Button(filewin, text="Do nothing button")
    button.pack()

root = tki.Tk()

root.state("zoomed")

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

filemenu.add_separator()

filemenu.add_command(label="Generate MIDI", command=midi)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()