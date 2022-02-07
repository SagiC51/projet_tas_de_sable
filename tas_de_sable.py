#########################################
# groupe MPCI TD1
# CHRISTOPHE Passcal
# CHAKROUN Mohammed
# KALI-A-NGOUELE Gloire
# https://github.com/uvsq21918050/projet_tas_de_sable
#########################################

#------Import des modules------###
import tkinter as tk
import random
import numpy as np
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
racine.geometry("720x720")
bouton = tk.Button(text="aléatoire")
bouton.grid(row=1, column=1, columnspan= 1, rowspan=1)
racine.mainloop()