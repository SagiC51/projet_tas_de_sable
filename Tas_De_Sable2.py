#########################################
# groupe MPCI TD1
# CHRISTOPHE Passcal
# CHAKROUN Mohammed
# KALI-A-NGOUELE Gloire
# https://github.com/uvsq21918050/projet_tas_de_sable
#########################################

#------Import des modules------###
from re import L
import tkinter as tk
import random
#------Variables globales------###

#------Fonctions------###
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

#------Programme principale------###

racine = tk.Tk()
racine.title("Sandpiles")
#Canvas = tk.Canvas(bg='white', height=HEIGHT_CANVAS, width=WIDHT_CANVAS)
bouton = tk.Button(text="aléatoire", height=10, width=30)
aleat()
print (L)
#Canvas.grid(row=1, column=1, columnspan=1, rowspan=1)
bouton.grid(row=1, column=1, columnspan=1, rowspan=1)
racine.mainloop()