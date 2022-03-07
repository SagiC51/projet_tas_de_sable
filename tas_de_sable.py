#########################################
# groupe MPCI TD1
# CHRISTOPHE Passcal
# CHAKROUN Mohammed
# KALI-A-NGOUELE Gloire
# https://github.com/uvsq21918050/projet_tas_de_sable
#########################################

###------Import des modules------###
import tkinter as tk
import random as random

###-----Constantes------###
HEIGHT_CANVAS = WIDHT_CANVAS = 400
N = 10  #grid_size = 3
# ##------Variables globales------###
L_aleat = []  # Configuration courante
Grille = []  # Grille
event = False
config = 0

###------Fonctions------###
def init():
    """
    Initialisation de notre grille et de la configuration Courante.
    """
    global L_aleat, Grille
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
                                                         outline='white'))
        Grille.append(intermediaire)
    print(Grille, "Grille")


def listAleat(Liste_vide, taille):
    """
    Prend en entrée une liste vide
    Renvoie une liste à deux dimensions de manières aléatoires
    """
    L1 = taille * [0]
    for i in range(0, len(L1)):
        for j in range(0, len(L1)):
            aleat = random.randint(0, 4)
            L1[j] += aleat
        Liste_vide.append(L1)
        L1 = taille * [0]
    print(Liste_vide, "liste vide")
    return Liste_vide


def maj(Liste):
    """
    Prend en entrée une liste, de taille 2, à deux dimension et renvoie les
    canvas correspondant à la liste
    """
    liste_couleur = ["black", "yellow", "green", "blue", "purple", "yellow", "orange",
                     "red"]
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
    """
    Renvoie une Liste d'entier dont les valeur ont été modifié de manière aléatoire :
    chaque int reçoit une valeur comprise entre 0 et 3
    On met à jour notre interface en fonction des valeurs obtenues  
    """
    for i in range(0, len(L_aleat)):
        for k in range(0, len(L_aleat)):
            l = random.randint(0, len(L_aleat))
            L_aleat[i][k] += l
    maj(L_aleat)
    return

def first_stab(L):
    """
    renvoie une première étape de stabilisation
    """
    L2 = listAleat([], len(L))
    for i in range(0, len(L)):
        for j in range(0, len(L)):
            L2[i][j] = 0
            L2[i][j] += L[i][j]

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
    print("liste l2:",L2)
    return L2

def stabilization(Liste):
    """
    On recommence la stabilisation jusqu'à ce que la configuration soit stable
    """
    global event
    event = False
    i = 0
    j = 0
    while i != len(Liste)-1 and j != len(Liste)-1:
        if Liste[i][j] >= 4 and event == False:
            Liste = first_stab(Liste) 
            j = 0
            i = 0
        else:
            j+=1
            if j == len(Liste)-1:
                j=0
                i+=1
    return Liste

def interuption():
    event = True

def num_config(n):
    """
    attribut un int n à config
    """
    global config
    config = n
    return config

def addition():
    """
    Renvoie la configuration qui est la somme case par case
    des deux configurations
    """ 
    L1 = configuration_random()
    L2 = configuration_pile(3) 
    L3 = max_stable() 
    L4 = identity()
    win = tk.Toplevel(racine)
    win.geometry("150x100")
    win.title("addition")
    Bouton_configuration_aleat = tk.Button(win, text="aleatoire", font=30, command=lambda:num_config(0))
    Bouton_configuration_pile = tk.Button(win, text="pile", font=30, command=lambda:num_config(1))
    Bouton_configuration_max_stable = tk.Button(win, text="max-stable", font=30, command=lambda:num_config(2))
    Bouton_configuration_identity = tk.Button(win, text="identity", font=30, command=lambda:num_config(3))
   
    Bouton_configuration_aleat.grid(row=2, column=2)
    Bouton_configuration_pile.grid(row=4, column=2)
    Bouton_configuration_max_stable.grid(row=2, column=4)
    Bouton_configuration_identity.grid(row=4, column=4)

    L_config = [L1,L2,L3,L4]
    for i in range(0,len(L_aleat)):
        for j in range(0, len(L_aleat)):
            print(L_config[config][i][j] , 'hahhahaha')
            L_aleat[i][j] += L_config[config][i][j]
            print(L_config[config][i][j] , 'hahhahaha')
            print(config)
            maj(L_aleat)
            print(L_aleat)
    

def soustraction():
    """
    Renvoie la configuration qui est la soustraction case par case
    des deux configurations
    """
    win = tk.Toplevel(racine)
    win.geometry("150x100")
    win.title("addition")
    
    Bouton_configuration_aleat = tk.Button(win, text="aleatoire", font=30, command=lambda:configuration_random())
    Bouton_configuration_pile = tk.Button(win, text="pile", font=30, command=lambda:configuration_pile(7))
    Bouton_configuration_max_stable = tk.Button(win, text="max-stable", font=30, command=lambda:max_stable())
    Bouton_configuration_identity = tk.Button(win, text="identity", font=30, command=lambda:identity())
   
    Bouton_configuration_aleat.grid(row=2, column=2)
    Bouton_configuration_pile.grid(row=4, column=2)
    Bouton_configuration_max_stable.grid(row=2, column=4)
    Bouton_configuration_identity.grid(row=4, column=4)

    # for i in range(0,len(L_aleat)):
    #     for j in range(0, len(L_aleat)):
    #         L_aleat[i][j] -= L_config[int(n)][i][j]
    #         if L_aleat[i][j] < 0 :
    #             L_aleat[i][j] = 0
    #         maj(L_aleat)
    #         print(L_aleat)

def configuration_random():
    """
    géneration d'une configuration aléatoire
    """
    L=[]
    for k in range(0, len(L_aleat)):
        L1=[]
        for i in range(0, len(L_aleat)):
            L1.append(random.randint(0,3))
        L+=[L1]
    maj(L)
    return

def configuration_pile(nombre):
    """
    N grains de sables à la case du milieu et 0 aux autres
    """
    L = listAleat([], len(L_aleat))
    if len(L)%2 == 0:
        print("impossible de crée la configuration pile")
    else:
        for i in range(0,len(L)):
            for j in range(0,len(L)):
                if i == (len(L)-1)/2 and j == (len(L)-1)/2:
                   L[i][j] = nombre
                else: 
                    L[i][j] = 0
    maj(L)
    return L

def max_stable():
    """
    Attribue 3 grains de sable à chaque case
    """
    L = listAleat([], len(L_aleat))
    for i in range(0,len(L)):
            for j in range(0,len(L)):
                L[i][j] = 3
    maj(L)
    return L 

def doublemaxstable():
    """
    Attribue 6 grains de sable à chaque case
    """
    L = listAleat([], len(L_aleat))
    for i in range(0,len(L)):
            for j in range(0,len(L)):
                L[i][j] = 6
    return L

def identity():
    doublemax = doublemaxstable()
    stabilisation = stabilization(doublemax)
    for i in range(0,len(L_aleat)):
        for j in range(0,len(L_aleat)):
            doublemax[i][j] -= stabilisation[i][j]
    identity = stabilization(doublemax)
    maj(identity)
    return identity
    
# ##------Programme principale------###
racine = tk.Tk()
racine.title("Sandpiles")
Canvas = tk.Canvas(bg='white', height=HEIGHT_CANVAS, width=WIDHT_CANVAS)  

Bouton_init = tk.Button(text='Lancer la simulation', font=30, command=init)
Bouton_maj = tk.Button(text="Génération", font=30, command=lambda:
                            maj(listAleat(L_aleat, N)))
Bouton_Calcul = tk.Button(text="Calcul", font=30, command=lambda:calcul())
Bouton_stabilisation = tk.Button(text="stabilisation", font=30, command=lambda:maj(stabilization(L_aleat)))
Bouton_addition = tk.Button(text="addition", font=30, command=lambda:addition())
Bouton_soustraction = tk.Button(text="soustraction", font=30, command=lambda:soustraction())
Bouton_configuration_aleat = tk.Button(text="aleat", font=30, command=lambda:configuration_random())
Bouton_configuration_pile = tk.Button(text="pile", font=30, command=lambda:configuration_pile(7))
Bouton_configuration_max_stable = tk.Button(text="max-stable", font=30, command=lambda:max_stable())
Bouton_configuration_identity = tk.Button(text="identity", font=30, command=lambda:identity())
Bouton_STOP = tk.Button(text="STOP", font=30, command=lambda:interuption())

# Placement des éléments
Canvas.grid(row=1, column=2, columnspan=1, rowspan=3)
Bouton_init.grid(row=1, column=1)
Bouton_maj.grid(row=2, column=1)
Bouton_Calcul.grid(row=3, column=1)
Bouton_stabilisation.grid(row=4, column=1)
Bouton_addition.grid(row=5, column=1)
Bouton_soustraction.grid(row=6, column=1)
Bouton_configuration_aleat.grid(row=7, column=1)
Bouton_configuration_pile.grid(row=8, column=1)
Bouton_configuration_max_stable.grid(row=9, column=1)
Bouton_configuration_identity.grid(row=10, column=1)
Bouton_STOP.grid(row=11, column=1)
racine.mainloop()