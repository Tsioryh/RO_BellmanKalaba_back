def find_common_cell(tableau, ligne_cells, colonne_cells):
    for row, col in ligne_cells:
        for r, c in colonne_cells:
            if tableau[row][c] != 0 and tableau[r][col] != 0:
                return (row, c)
    return None


def create_cell_list(tableau):
    cell_list = []
    start_row, start_col = 1, 5
    reference_value = tableau[start_row][start_col]

    ligne_cells = []
    colonne_cells = []

    # Recherche des cellules sur la même ligne
    for col in range(len(tableau[0])):
        if col != start_col and tableau[start_row][col] != 0:
            ligne_cells.append((start_row, col))

    # Recherche des cellules sur la même colonne
    for row in range(len(tableau)):
        if row != start_row and tableau[row][start_col] != 0:
            colonne_cells.append((row, start_col))

    # Recherche de la cellule commune
    common_cell = find_common_cell(tableau, ligne_cells, colonne_cells)

    cell_list.append({'ligne_cells': ligne_cells})
    cell_list.append({'colonne_cells': colonne_cells})
    cell_list.append({'common_cell': common_cell})

    return cell_list


tableau_X = [
    [0, 11, 2, 0, 0, 5],
    [9, 0, 23, 0, 0, 0],
    [0, 0, 3, 6, 5, 0],
    [0, 0, 0, 0, 9, 0]
]

cell_list = create_cell_list(tableau_X)
ligne_cells = cell_list[0]['ligne_cells']
colonne_cells = cell_list[1]['colonne_cells']
common_cell = cell_list[2]['common_cell']

print("ligne_cells:", ligne_cells)
print("colonne_cells:", colonne_cells)
print("common_cell:", common_cell)
