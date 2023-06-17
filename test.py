tableau_X = [
    [0, 11, 2, 0, 0, 5],
    [9, 0, 23, 0, 0, 0],
    [0, 0, 3, 6, 5, 0],
    [0, 0, 0, 0, 9, 0]
]

def trouver_cellules_differentes(tableau):
    ligne = 2
    colonne = 5
    cellules_ligne_colonne = []
    cellules_colonne_ligne = []

    # Parcourir les cellules de même ligne que [1][5]
    for x in range(len(tableau[ligne])):
        if x != colonne and tableau[ligne][x] != 0:
            cellules_colonne = []
            for y in range(len(tableau)):
                if y != ligne and tableau[y][x] != 0:
                    cellules_colonne.append((y, x))
            cellules_ligne_colonne.append(((ligne, x), cellules_colonne))

    # Parcourir les cellules de même colonne que [1][5]
    for y in range(len(tableau)):
        if y != ligne and tableau[y][colonne] != 0:
            cellules_ligne = []
            for x in range(len(tableau[ligne])):
                if x != colonne and tableau[y][x] != 0:
                    cellules_ligne.append((y, x))
            cellules_colonne_ligne.append(((y, colonne), cellules_ligne))

    return cellules_ligne_colonne, cellules_colonne_ligne


cellules_ligne_colonne, cellules_colonne_ligne = trouver_cellules_differentes(tableau_X)

print("Cellules de même ligne avec des cellules de même colonne:")
for cellule, cellules_colonne in cellules_ligne_colonne:
    print("Cellule :", cellule)
    print("Cellules de même colonne :", cellules_colonne)

print("Cellules de même colonne avec des cellules de même ligne:")
for cellule, cellules_ligne in cellules_colonne_ligne:
    print("Cellule :", cellule)
    print("Cellules de même ligne :", cellules_ligne)
