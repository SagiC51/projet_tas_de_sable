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
#-----------Constate-----------###
HEIGHT_CANVAS = WIDHT_CANVAS = 500
#------Variables globales------###
def aleat():
    """
    Entrée: 
    Sortie: Liste de liste aléatoire
    """
    L = []
    L1 = [0,0,0]
    for i in range(0,3):
        for j in range (0,3):
            aleat = random.randint(0, 9)
            L1[j]+=aleat
        L.append(L1)
        L1=[0,0,0]
    return L


def Init():
    xh = yh = 0
    xb = yb = 100
    Canvas.create_rectangle(xh, yh, xb, yb, fill='black', outline='white')
    while yb != HEIGHT_CANVAS:
        if xb == WIDHT_CANVAS:
            xh = 0
            xb = 100
            yh = yb
            yb += 100
            Canvas.create_rectangle(xh, yh, xb, yb, fill='black', outline='white')
        while xb != WIDHT_CANVAS:
            xh = xb
            xb += 100
            Canvas.create_rectangle(xh, yh, xb, yb, fill='black', outline='white')

#------Programme principale------###

racine = tk.Tk()
racine.title("Sandpiles")
Canvas = tk.Canvas(bg='white', height=HEIGHT_CANVAS, width=WIDHT_CANVAS)
bouton = tk.Button(text="aléatoire", font=30,command= aleat)
Init()
Canvas.grid(row=1, column=2, columnspan=1, rowspan=2)
bouton.grid(row=1, column=1)
racine.mainloop()
