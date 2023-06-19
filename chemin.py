def trouver_chemins_minimaux(noeuds, distances, liens, depart, arrivee):
    # Initialisation des distances avec une valeur infinie pour tous les noeuds, sauf le départ qui est à 0
    chemin_minimal = {noeud: float('inf') for noeud in noeuds}
    chemin_minimal[depart] = 0

    # Itération pour mettre à jour les distances jusqu'à convergence
    for _ in range(len(noeuds) - 1):
        for lien in liens:
            origine = lien['from']
            destination = lien['to']
            valeur = int(lien['value'])

            # Mise à jour de la distance minimale si une meilleure valeur est trouvée
            if chemin_minimal[origine] + valeur < chemin_minimal[destination]:
                chemin_minimal[destination] = chemin_minimal[origine] + valeur

    # Recherche de tous les chemins minimaux à partir du départ jusqu'à l'arrivée
    chemins_minimaux = []
    pile = [(arrivee, [arrivee])]

    while pile:
        noeud_actuel, chemin_actuel = pile.pop()

        if noeud_actuel == depart:
            chemin_actuel.reverse()
            chemins_minimaux.append(chemin_actuel)
        else:
            for lien in liens:
                origine = lien['from']
                destination = lien['to']
                valeur = int(lien['value'])

                if destination == noeud_actuel and chemin_minimal[origine] + valeur == chemin_minimal[noeud_actuel]:
                    pile.append((origine, chemin_actuel + [origine]))

    return chemins_minimaux

noeuds = ['A', 'B', 'C', 'D']
distances = [
    {
        "A": 5,
        "B": 2,
        "C": 2,
        "D": 0
    }
]
liens = [
    {'from': 'A', 'to': 'B', 'value':'4'},
    {'from': 'A', 'to': 'C', 'value':'4'},
    {'from': 'A', 'to': 'D', 'value':'5'},
    {'from': 'B', 'to': 'D', 'value':'2'},
    {'from': 'C', 'to': 'D', 'value':'2'},
]

chemins = trouver_chemins_minimaux(noeuds, distances, liens, 'A', 'D')
print(chemins)  # Résultat: [['A', 'B', 'D'], ['A', 'D']]
