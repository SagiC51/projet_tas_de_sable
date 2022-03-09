#####################################################################
# Docstring
#
# groupe MPCI TD1
# CHRISTOPHE Passcal
# CHAKROUN Mohammed
# KALI-A-NGOUELE Gloire
# https://github.com/uvsq21918050/projet_tas_de_sable
#########################################


# ------------------------- Bibliothèques ------------------------- #
import tkinter as tk
import random as random
import copy
import time

# --------------------------- Constante --------------------------- #
HEIGHT_CANVAS = WIDHT_CANVAS = 400
N = 5  # grid_size = 3

# ----------------------- Varaibles Globale ----------------------- #
L_aleat = []  # Configuration courante
Grille = []  # Grille
run = False
config = 0
Case = 1

# ------------------------ Partie Fonction ------------------------ #


def init():
    # Initialisation de notre grille et de la configuration Courante.
    global L_aleat, Grille, run, Case
    if run is True:
        Bouton_STOP['text'] = "STOP"
        run = False

    # i et j nous permettent de gérer les coordonnées des points délimitants le
    # canvas
    L_aleat = []  # Configuration courante
    Grille = []  # Grille
    for i in range(0, N):
        intermediaire = []
        for j in range(1, N+1):
            xh = (j-1)*HEIGHT_CANVAS/N
            yh = i*HEIGHT_CANVAS/N
            xb = j*HEIGHT_CANVAS/N
            yb = (i+1)*WIDHT_CANVAS/N
            intermediaire.append(Canvas.create_rectangle(xh, yh, xb, yb,
                                                         fill='black',
                                                         outline='white',
                                                         tags=("Case_ " +
                                                                 str(Case))))
            Case += 1
        Grille.append(intermediaire)
    print(Grille, "Grille")
    print(Case)


def listAleat(Liste_vide, taille):
    # Prend en entrée une liste vide
    # Renvoie une liste à deux dimensions de manières aléatoires

    L1 = taille * [0]
    for i in range(0, len(L1)):
        for j in range(0, len(L1)):
            aleat = random.randint(0, 4)
            L1[j] += aleat
        Liste_vide.append(L1)
        L1 = taille * [0]
    print(Liste_vide)
    return Liste_vide


def maj(Liste):
    # Prend en entrée une liste, de taille 2, à deux dimension et renvoie les
    # canvas correspondant à la liste
    
    liste_couleur = ["black", "yellow", "green", "blue", "purple", "yellow",
                     "orange", "red"]
    # i et j nous permettent de gérer les coordonnées des points délimitant
    # le Canvas,
    # Chaque couleur corespond a une valeur de couleur.
    for i in range(0, len(Liste)):
        for j in range(1, len(Liste)+1):
            # On regarde à quelle couleur correspond notre chiffre puis dessine
            #  notre canvas
            for k in range(0, 8):
                if Liste[i][j-1] == k:
                    Canvas.itemconfigure(Grille[i][j-1], fill=liste_couleur[k],
                                         outline='white')


def calcul():
    # Renvoie une Liste d'entier dont les valeur ont été modifié de manière
    # aléatoire :
    # chaque int reçoit une valeur comprise entre 0 et 3
    # On met à jour notre interface en fonction des valeurs obtenues

    for i in range(0, len(L_aleat)):
        for k in range(0, len(L_aleat)):
            a = random.randint(0, len(L_aleat))
            L_aleat[i][k] += a
    maj(L_aleat)
    return


def first_stab(L):
    # renvoie une première étape de stabilisation

    L2 = copy.deepcopy(L)
    for i in range(0, len(L)):
        for j in range(0, len(L)):
            if L2[i][j] >= 4:
                L2[i][j] -= 4
                # On modifie les carré qui ne sont pas aux bords
                if i != 0 and j != 0 and i != len(L)-1 and j != len(L)-1:
                    L2[i][j-1] += 1
                    L2[i][j+1] += 1
                    L2[i+1][j] += 1
                    L2[i-1][j] += 1
                # On modifie le coins sup gauche
                if i == 0 and j == 0:
                    L2[i][j+1] += 1
                    L2[i+1][j] += 1
                # On modifie le coins inf gauche
                if i == len(L)-1 and j == 0:
                    L2[i][j+1] += 1
                    L2[i-1][j] += 1
                # On modifie le coins inf droit
                if i == len(L)-1 and j == len(L)-1:
                    L2[i][j-1] += 1
                    L2[i-1][j] += 1
                # On modifie le coins sup droit
                if i == 0 and j == len(L)-1:
                    L2[i][j-1] += 1
                    L2[i+1][j] += 1
                # On modifie la 1ere ligne
                if i == 0 and len(L)-1 > j >= 1:
                    L2[i][j+1] += 1
                    L2[i+1][j] += 1
                    L2[i][j-1] += 1
                # On modifie la 1ere colonne
                if len(L)-1 > i >= 1 and j == 0:
                    L2[i+1][j] += 1
                    L2[i-1][j] += 1
                    L2[i][j+1] += 1
                # On modifie la dernière ligne
                if i == len(L) - 1 and len(L)-1 > j >= 1:
                    L2[i][j-1] += 1
                    L2[i-1][j] += 1
                    L2[i][j+1] += 1
                # On modifie la dernière colonne
                if len(L)-1 > i >= 1 and j == len(L) - 1:
                    L2[i][j-1] += 1
                    L2[i+1][j] += 1
                    L2[i-1][j] += 1
            maj(L2)
    print(L2)
    return L2


def stabilization(Liste):
    # On recommence la stabilisation jusqu'à ce que la configuration soit
    # stable

    global run, Liste2
    run = False
    i = 0
    j = 0
    while i != len(Liste)-1 and j != len(Liste)-1:
        if run is False:
            if Liste[i][j] >= 4:
                Liste = first_stab(Liste)
                maj(Liste)
                Canvas.update()
                time.sleep(0.5)
                j = 0
                i = 0
                print(run)
            else:
                j += 1
                if j == len(Liste)-1:
                    i += 1
                    j = 0
        else:
            Liste2 = copy.deepcopy(Liste)
            break
    return Liste


def On_off():
    global run, Liste2
    if run is False:
        Bouton_STOP['text'] = "GO"
        run = True
    else:
        Bouton_STOP['text'] = "STOP"
        run = False
        stabilization(Liste2)


def num_config(n):
    # attribut un int n à config

    global config
    config = n
    print("config: ", config)
    return config


def addition():
    # Renvoie la configuration qui est la somme case par case
    # des deux configurations

    L_config = [configuration_random(), configuration_pile(3), max_stable(),
                identity()]
    for i in range(0, len(L_aleat)):
        for j in range(0, len(L_aleat)):
            print(L_config[config][i][j])
            L_aleat[i][j] += L_config[config][i][j]
            # print(L_config[config][i][j])
            print("config: ", config)
            maj(L_aleat)
            print(L_aleat)


def soustraction():
    # Renvoie la configuration qui est la soustraction case par case
    # des deux configurations

    L_config = [configuration_random(), configuration_pile(3), max_stable(),
                identity()]
    for i in range(0, len(L_aleat)):
        for j in range(0, len(L_aleat)):
            L_aleat[i][j] -= L_config[config][i][j]
            if L_aleat[i][j] < 0:
                L_aleat[i][j] = 0
            maj(L_aleat)
            print(L_aleat)


def configuration_random():
    # géneration d'une configuration aléatoire

    L = []
    for k in range(0, len(L_aleat)):
        L1 = []
        for i in range(0, len(L_aleat)):
            L1.append(random.randint(0, 3))
        L += [L1]
    maj(L)
    return


def configuration_pile(nombre):
    # N grains de sables à la case du milieu et 0 aux autres

    L = listAleat([], len(L_aleat))
    if len(L) % 2 == 0:
        print("impossible de crée la configuration pile")
    else:
        for i in range(0, len(L)):
            for j in range(0, len(L)):
                if i == (len(L)-1)/2 and j == (len(L)-1)/2:
                    L[i][j] = nombre
                else:
                    L[i][j] = 0
    maj(L)
    return L


def max_stable():
    # Attribue 3 grains de sable à chaque case

    L = listAleat([], len(L_aleat))
    for i in range(0, len(L)):
        for j in range(0, len(L)):
            L[i][j] = 3
    maj(L)
    return L


def doublemaxstable():
    # Attribue 6 grains de sable à chaque case

    L = listAleat([], len(L_aleat))
    for i in range(0, len(L)):
        for j in range(0, len(L)):
            L[i][j] = 6
    return L


def identity():
    global L_aleat, Grille
    doublemax = doublemaxstable()
    stabilisation = stabilization(doublemax)
    for i in range(0, len(L_aleat)):
        for j in range(0, len(L_aleat)):
            doublemax[i][j] -= stabilisation[i][j]
    identity = stabilization(doublemax)
    maj(identity)
    return identity


def clic(event):
    global Case
    print("click")
    x = event.x
    y = event.y
    objet = Canvas.scan_mark(x, y)
    Brick = int(objet[0])
    if Brick <= Case:
        Canvas.itemconfigure(Brick, state="hidden")
        Case -= 1

# ------------------------ Code Principale ------------------------ #

# Parrametre de la racine et Canvas


racine = tk.Tk()
racine.title("Sandpiles")
Canvas = tk.Canvas(bg='white', height=HEIGHT_CANVAS, width=WIDHT_CANVAS)
# élémente de la fênetre
Bouton_init = tk.Button(text='Lancer la simulation', font=30, command=init)
Bouton_maj = tk.Button(text="Génération", font=30, command=lambda:
                            maj(listAleat(L_aleat, N)))
Bouton_Calcul = tk.Button(text="Calcul", font=30, command=lambda: calcul())
Bouton_stabilisation = tk.Button(text="stabilisation", font=30, command=lambda:
                                 stabilization(L_aleat))
Bouton_addition = tk.Button(text="addition", font=30, command=lambda:
                            addition())
Bouton_soustraction = tk.Button(text="soustraction", font=30, command=lambda:
                                soustraction())
Bouton_STOP = tk.Button(text="STOP", font=30, command=lambda: On_off())
Canvas.bind("<Button-1>", clic)

# menu liste
mon_menu = tk.Menu(racine)
racine['menu'] = mon_menu
# menu partie menu general
party = tk.Menu(mon_menu, tearoff=0)
party_2 = tk.Menu(mon_menu, tearoff=0)
party_3 = tk.Menu(mon_menu, tearoff=0)

party.add_cascade(label="Addition \Soutraction", menu=party_2)
party.add_command(label="aleat", font=30, command=lambda:
                  configuration_random())
party.add_command(label="pile", font=30, command=lambda:
                  configuration_pile(7))
party.add_command(label="max-stable", font=30,
                  command=lambda: max_stable())
mon_menu.add_cascade(label="Menu", menu=party)

# menu partie menu addition
party_2.add_command(label="configuration_random", command=lambda: num_config(0)
                    )
party_2.add_command(label="configuration_pile", command=lambda: num_config(1))
party_2.add_command(label="max_stable", command=lambda: num_config(2))
party_2.add_command(label="identity", command=lambda: num_config(3))

# Placement des éléments
Canvas.grid(row=1, column=2, columnspan=1, rowspan=7)
Bouton_init.grid(row=1, column=1)
Bouton_maj.grid(row=2, column=1)
Bouton_Calcul.grid(row=3, column=1)
Bouton_stabilisation.grid(row=4, column=1)
Bouton_addition.grid(row=5, column=1)
Bouton_soustraction.grid(row=6, column=1)
Bouton_STOP.grid(row=7, column=1)
racine.mainloop()

# ----------------------- Fin du programme  ----------------------- #
