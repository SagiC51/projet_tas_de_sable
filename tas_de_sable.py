#########################################
# groupe MPCI TD1
# CHRISTOPHE Passcal
# CHAKROUN Mohammed
# KALI-A-NGOUELE Gloire
# https://github.com/uvsq21918050/projet_tas_de_sable
#########################################

#------Import des modules------###
import tkinter as tk
<<<<<<< HEAD
import random
import numpy as np
=======
#-----------Constate-----------###
HEIGHT_CANVAS = WIDHT_CANVAS = 400
>>>>>>> 1e28f7add5944fe44c3616bdd092e6e85bffd138
#------Variables globales------###

#------Fonctions------###
def aleat():
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
bouton = tk.Button(text="aléatoire", height=10, width=30)
Canvas.grid(row=1, column=1, columnspan=1, rowspan=1)
bouton.grid(row=1, column=1, columnspan=1, rowspan=1)
racine.mainloop()