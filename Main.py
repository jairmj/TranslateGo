from tkinter import *
import random as r


def center_window(w=300, h=200):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y-80))


def InitComponents():
    root.title("TranslateGo")
    root.iconbitmap("idioma.ico")
    center_window(600, 500)
    root.configure(background=bg)
    root.resizable(False,False)
    root.frame
    return {"por lo tanto": "therefore","sin embargo": "however","por lo cual": "whereby"},["por lo tanto", "sin embargo", "por lo cual",]
# {"risita": "giggle","tartamudear": "stutter","traicionar": "betray", "superficial": "shallow","sediento": "thirsty","enredo": "tangle","por lo tanto": "therefore",
#             "avivado": "stoked", "sin embargo": "however","hito": "milestone","por lo cual": "whereby","imaginando": "envisioning","desvelar": "lie awake",
#             "chupetón": "hickey", "recelo": "misgiving", "ladrón":"thief", "volcar":"tip off", "desventaja": "handicap","estafador":["scammer", "swindler"],"mimar":"spoil", "botín":"spoil",
#             "acertijo": "riddle","en efecto": "indeed"},\
#            ["risita", "tartamudear", "traicionar", "superficial", "sediento", "enredo", "por lo tanto", "avivado", "sin embargo", "hito", "por lo cual", "imaginando", "desvelar","chupetón","recelo","ladrón","volcar","desventaja",
#             "estafador","mimar","botín","acertijo","en efecto"]



def setNewWord():
    rand.set(r.randint(0, len(Palabras)-1))
    while Palabras[rand.get()] == PreviousWord.get():
        rand.set(r.randint(0, len(Palabras)-1))
    lblPalabra.config(text=Palabras[rand.get()].capitalize())
    PreviousWord.set(Palabras[rand.get()])
    txtWord.delete(0, 'end')
    lblError.config(text = "")
    txtWord.config(fg='black')
    hint.set("")

def CheckWord(event):
    if isinstance(Diccionario[PreviousWord.get().lower()], str):
        if txtpalabra.get() == Diccionario[PreviousWord.get().lower()]:
            setNewWord()
        else:
            txtWord.config(fg='red')
    else:
        if txtpalabra.get().lower() in Diccionario[PreviousWord.get().lower()]:
            setNewWord()

def CheckWord1():
    if isinstance(Diccionario[PreviousWord.get().lower()], str):
        if txtpalabra.get() == Diccionario[PreviousWord.get().lower()]:
            setNewWord()
        else:
            txtWord.config(fg='red')
    else:
        if txtpalabra.get().lower() in Diccionario[PreviousWord.get().lower()]:
            setNewWord()


def Hint():
    cantidad = len(Diccionario[PreviousWord.get().lower()])
    try:
        hint.set(hint.get() + Diccionario[PreviousWord.get().lower()][len(hint.get())])
        lblError.config(text = hint.get())
    except:
        pass







root = Tk()
bg = "#81D8D0"
Diccionario, Palabras = InitComponents()

hint = StringVar()
txtpalabra = StringVar()
PreviousWord = StringVar()
rand = IntVar()
rand.set(r.randint(0,len(Palabras)-1))


PreviousWord.set(Palabras[rand.get()].capitalize())





####################################           ETIQUETAS             ##################################

lblPalabra = Label(root, text = Palabras[rand.get()].capitalize(), bg = bg,font = ("Franklin Gothic",30))
lblPalabra.pack(pady = 40)

lblError = Label(root, text = "", bg = bg,font = ("Franklin Gothic",30), width = 26, anchor = CENTER)
lblError.pack()
lblError.place(x = 0, y = 300)

txtWord = Entry(root, textvariable = txtpalabra, width = 30, font = "Arial 20", justify = CENTER)
txtWord.place( x = 70, y =160)





send = PhotoImage(file="send1.png")
btnGo = Button(root, text = 'Enviar', command = CheckWord1, borderwidth = 4, width = 20, image = send)
btnGo.pack()
btnGo.place( x =  70, y = 210)


btnGo = Button(root, text = 'Pista', command = Hint, borderwidth = 4, width = 10)
btnGo.pack()
btnGo.place( x =  440, y = 210)


root.bind('<Return>', CheckWord)


root.mainloop()