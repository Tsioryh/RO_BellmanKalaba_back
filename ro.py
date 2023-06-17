from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/bellman', methods=['POST'])
def bellman_kalaba_inverse_api():
    # Récupération des données d'entrée depuis la requête
    data = request.get_json()
    noeuds = data['noeuds']
    liens = data['liens']
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

    # Appel de la fonction
    resultat_inverse = bellman_kalaba_inverse(noeuds, liens)

    chemin_minimal = []
    noeud_courant = None
    for noeud in noeuds:
            trouve = any(lien['to'] == noeud for lien in liens)
            if not trouve:
                noeud_courant = noeud
                break

    while noeud_courant is not None:
        chemin_minimal.insert(0, noeud_courant)
        noeud_courant = resultat_inverse[1][noeud_courant]

    resultat_json = jsonify(resultat_inverse, chemin_minimal)

    return resultat_json

if __name__ == '__main__':
    app.run()
