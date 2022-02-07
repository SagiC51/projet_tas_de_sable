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
#-----------Constate-----------#

HEIGHT_CANVAS = WIDHT_CANVAS = 400
#------Variables globales------#

#------Fonctions------##

import random
import numpy as np
#-----------Constate-----------###
HEIGHT_CANVAS = WIDHT_CANVAS = 400
#------Variables globales------###
def aleat():
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

racine = tk.Tk()
racine.title("Sandpiles")
Canvas = tk.Canvas(bg='white', height=HEIGHT_CANVAS, width=WIDHT_CANVAS)
bouton = tk.Button(text="aléatoire", font=30,)
Init()
Canvas.grid(row=1, column=2, columnspan=1, rowspan=2)
bouton.grid(row=1, column=1)
racine.mainloop()
