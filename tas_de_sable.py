#########################################
# groupe MPCI TD1
# CHRISTOPHE Passcal
# CHAKROUN Mohammed
# KALI-A-NGOUELE Gloire
# https://github.com/uvsq21918050/projet_tas_de_sable
#########################################

#------Import des modules------###
import tkinter as tk
#-----------Constate-----------###
HEIGHT_CANVAS = WIDHT_CANVAS = 400
#------Variables globales------###

#------Fonctions------###
def aleat():
    pass
#------Programme principale------###

racine = tk.Tk()
racine.title("Sandpiles")
Canvas = tk.Canvas(bg='white', height=HEIGHT_CANVAS, width=WIDHT_CANVAS)
bouton = tk.Button(text="aléatoire")
Canvas.grid(row=1, column=1, columnspan=1, rowspan=1)
bouton.grid(row=1, column=1, columnspan=1, rowspan=1)
racine.mainloop()