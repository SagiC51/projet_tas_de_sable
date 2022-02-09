#########################################
# groupe MPCI TD1
# CHRISTOPHE Passcal
# CHAKROUN Mohammed
# KALI-A-NGOUELE Gloire
# https://github.com/uvsq21918050/projet_tas_de_sable
#########################################

# ------Import des modules------###
import tkinter as tk
import random

# ##-----Constantes------###
HEIGHT_CANVAS = WIDHT_CANVAS = 400


# ##------Variables globales------###
L_aleat = []

# ##------Fonction------###


def init():
    """
    Initialisation de notre grille
    """
    # i et j nous permettent de gérer les coordonnées des points délimitant le
    # canvas
    for i in range(0, 3):
        for j in range(1, 4):
            Canvas.create_rectangle(i*HEIGHT_CANVAS/3, (j-1)*HEIGHT_CANVAS/3,
                                    (i+1)*HEIGHT_CANVAS/3, j*WIDHT_CANVAS/3,
                                    fill='black', outline='white')


def listAleat(Liste_vide):
    """
    Prend en entrée une liste vide]
    Renvoie une liste à deux dimensions de manières aléatoires
    """
    L1 = [0, 0, 0]
    for i in range(0, 3):
        for j in range(0, 3):
            aleat = random.randint(0, 4)
            L1[j] += aleat
        Liste_vide.append(L1)
        L1 = [0, 0, 0]
    print(Liste_vide)
    return Liste_vide


def maj(Liste):
    """
    Prend en entrée une liste, de taille 2, à deux dimension et renvoie les
    canvas correspondant à la liste
    """
    liste_couleur = ["black", "grey", "blue", "purple", "yellow", "orange",
                     "red"]
    # i et j nous permettent de gérer les coordonnées des points délimitant
    # le Canvas
    for i in range(0, 3):
        for k in range(1, 4):
            # On regarde à quelle couleur correspond notre chiffre puis dessine
            #  notre canvas
            for o in range(0, 8):
                if Liste[i][k-1] == o:
                    Canvas.create_rectangle((k-1)*HEIGHT_CANVAS/3,
                                            i*HEIGHT_CANVAS/3,
                                            k*HEIGHT_CANVAS/3,
                                            (i+1)*WIDHT_CANVAS/3,
                                            fill=liste_couleur[o],
                                            outline='white')

# ##------Programme principale------###


racine = tk.Tk()
racine.title("Sandpiles")
Canvas = tk.Canvas(bg='white', height=HEIGHT_CANVAS, width=WIDHT_CANVAS)
bouton_maj = tk.Button(text="Génération", font=30, command=lambda:
                            maj(listAleat(L_aleat)))
init()
Canvas.grid(row=1, column=2, columnspan=1, rowspan=2)
bouton_maj.grid(row=1, column=1)
racine.mainloop()
