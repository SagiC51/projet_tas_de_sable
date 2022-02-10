#########################################
# groupe MPCI TD1
# CHRISTOPHE Passcal
# CHAKROUN Mohammed
# KALI-A-NGOUELE Gloire
# https://github.com/uvsq21918050/projet_tas_de_sable
#########################################

# ------Import des modules------###
import tkinter as tk
import random as random

# ##-----Constantes------###
HEIGHT_CANVAS = WIDHT_CANVAS = 400
N = 3


# ##------Variables globales------###
L_aleat = []  # Configuration courante
Grille = []  # Grille


# ##------Fonction------###


def init():
    """
    Initialisation de notre grille et de la configuration Courante.
    """

    global L_aleat, Grille
    # i et j nous permettent de gérer les coordonnées des points délimitant le
    # canvas
    L_aleat = []  # Configuration courante
    Grille = []  # Grille
    for i in range(0, 3):
        intermediaire = []
        for j in range(1, 4):
            xh = i*HEIGHT_CANVAS/3
            yh = (j-1)*HEIGHT_CANVAS/3
            xb = (i+1)*HEIGHT_CANVAS/3
            yb = j*WIDHT_CANVAS/3
            intermediaire.append(Canvas.create_rectangle(xh, yh, xb, yb,
                                                         fill='black',
                                                         outline='white'))
        Grille.append(intermediaire)
    print(Grille, "Grille")


def listAleat(Liste_vide):
    """
    Prend en entrée une liste vide
    Renvoie une liste à deux dimensions de manières aléatoires
    """
    L1 = [0, 0, 0]
    for i in range(0, 3):
        for j in range(0, 3):
            aleat = random.randint(0, 4)
            L1[j] += aleat
        Liste_vide.append(L1)
        L1 = [0, 0, 0]
    print(Liste_vide, "liste vide")
    return Liste_vide


def maj(Liste):
    """
    Prend en entrée une liste, de taille 2, à deux dimension et renvoie les
    canvas correspondant à la liste
    """
    liste_couleur = ["black", "grey", "blue", "purple", "yellow", "orange",
                     "red"]
    # i et j nous permettent de gérer les coordonnées des points délimitant
    # le Canvas,
    # Chaque couleur corespond a une valeur de couleur.
    for i in range(0, 3):
        for k in range(1, 4):
            # On regarde à quelle couleur correspond notre chiffre puis dessine
            #  notre canvas
            for o in range(0, 8):
                if Liste[i][k-1] == o:
                    Canvas.itemconfigure(Grille[i][k-1], fill=liste_couleur[o],
                                         outline='white')

# ##------Programme principale------###


racine = tk.Tk()
racine.title("Sandpiles")
Canvas = tk.Canvas(bg='white', height=HEIGHT_CANVAS, width=WIDHT_CANVAS)
Bouton_init = tk.Button(text='Lancer la simulation', font=30, command=init)
bouton_maj = tk.Button(text="Génération", font=30, command=lambda:
                            maj(listAleat(L_aleat)))
Bouton_Calcul = tk.Button(text="Calcul", font=30)


# Placement des éléments

Canvas.grid(row=1, column=2, columnspan=1, rowspan=3)
Bouton_init.grid(row=1, column=1)
bouton_maj.grid(row=2, column=1)
Bouton_Calcul.grid(row=3, column=1)
racine.mainloop()
