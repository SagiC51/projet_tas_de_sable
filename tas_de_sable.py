#########################################
# groupe MPCI TD1
# CHRISTOPHE Passcal
# CHAKROUN Mohammed
# KALI-A-NGOUELE Gloire
# https://github.com/uvsq21918050/projet_tas_de_sable
#########################################

#------Import des modules------##
#
import tkinter as tk
<<<<<<< HEAD
#-----------Constate-----------#

HEIGHT_CANVAS = WIDHT_CANVAS = 400
#------Variables globales------#

#------Fonctions------##

=======
<<<<<<< HEAD
import random
import numpy as np
=======
#-----------Constate-----------###
HEIGHT_CANVAS = WIDHT_CANVAS = 400
>>>>>>> 1e28f7add5944fe44c3616bdd092e6e85bffd138
#------Variables globales------###
>>>>>>> 0c82359a42534697b8305ba6872b386e74db5951

def aleat():
<<<<<<< HEAD
    pass


def Init():
    xh = yh = 0
    xb = yb = HEIGHT_CANVAS/5
    Canvas.create_rectangle(xh, yh, xb, yb, fill='black', outline='white')
    while yb != HEIGHT_CANVAS:
        if xb == WIDHT_CANVAS:
            xh = 0
            xb = 50
            yh = yb
            yb += HEIGHT_CANVAS/5
            Canvas.create_rectangle(xh, yh, xb, yb, fill='black', outline='white')
        while xb != WIDHT_CANVAS:
            xh = xb
            xb += HEIGHT_CANVAS/5
            Canvas.create_rectangle(xh, yh, xb, yb, fill='black', outline='white')


#------Programme principale------##
#
=======
    """
    Entrée:
    Sortie:
    """
    L = []
    for i in range (0,5):
        L1 = []
        aleat = random.randint(0, 10)
        L1+=aleat
        if len(L1) > 3:
            L+=L1
            L1=[]

#------Programme principale------###
>>>>>>> 0c82359a42534697b8305ba6872b386e74db5951

racine = tk.Tk()
racine.title("Sandpiles")
Canvas = tk.Canvas(bg='white', height=HEIGHT_CANVAS, width=WIDHT_CANVAS)
bouton = tk.Button(text="aléatoire", font=30,)
Init()
Canvas.grid(row=1, column=2, columnspan=1, rowspan=2)
bouton.grid(row=1, column=1)
racine.mainloop()
