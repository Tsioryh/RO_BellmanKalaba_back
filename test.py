
# Récupération des données d'entrée depuis la requête
# data = request.get_json()
# noeuds = data['noeuds']
# liens = data['liens']
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
    {'from': 'A', 'to': 'B', 'value':'3'},
    {'from': 'A', 'to': 'C', 'value':'4'},
    {'from': 'A', 'to': 'D', 'value':'5'},
    {'from': 'B', 'to': 'D', 'value':'2'},
    {'from': 'C', 'to': 'D', 'value':'2'},
]
fin = None

# Algorithme de Bellman-Kalaba inverse
def bellman_kalaba_inverse(noeuds, liens):
    # Initialisation
    infini = float('inf')
    distances = {noeud: infini for noeud in noeuds}
    predecesseurs = {noeud: None for noeud in noeuds}

    for noeud in noeuds:
        trouve = any(lien['from'] == noeud for lien in liens)
        if not trouve:
            fin = noeud
            break

    if fin is not None:
        distances[fin] = 0


    # Itérations de relaxation
    for _ in range(len(noeuds) - 1):
        for lien in liens:
            de = lien['to']
            vers = lien['from']
            valeur = int(lien['value'])
            if distances[de] + valeur < distances[vers]:
                distances[vers] = distances[de] + valeur
                predecesseurs[vers] = de

    # Vérification des cycles de poids négatifs
    for lien in liens:
        de = lien['to']
        vers = lien['from']
        valeur = int(lien['value'])
        if distances[de] + valeur < distances[vers]:
            raise ValueError("Le graphe contient un cycle de poids négatif")

    return distances, predecesseurs

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

debut = None
for noeud in noeuds:
        trouve = any(lien['to'] == noeud for lien in liens)
        if not trouve:
            debut = noeud
            break

for noeud in noeuds:
    trouve = any(lien['from'] == noeud for lien in liens)
    if not trouve:
        fin = noeud
        break
    
# Appel de la fonction
resultat_inverse = bellman_kalaba_inverse(noeuds, liens)
print('noeuds : ' , noeuds)
print('distances : ', resultat_inverse[0])
print('liens : ', liens)
print('debut : ', debut)
print('fin : ', fin)
chemin_minimal = trouver_chemins_minimaux(noeuds, resultat_inverse[0], liens, debut, fin)

resultat_json = ({'Distances :' : resultat_inverse[0], 'Chemin minimal' :chemin_minimal})

print (resultat_json)
