from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Configuration de la base de données PostgreSQL
DB_HOST = '192.168.88.32'
DB_PORT = '5432'
DB_NAME = 'BaseNGLib'
DB_USER = 'postgres'
DB_PASSWORD = 'ait8lac9*'

# Route de l'API pour récupérer les catégories avec leurs sous-catégories en JSON
@app.route('/categories', methods=['GET'])
def get_categories():
    try:
        # Connexion à la base de données PostgreSQL
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )

        # Création d'un curseur pour exécuter des requêtes SQL
        cursor = conn.cursor()

        # Exécution d'une requête SQL pour récupérer les catégories avec leurs sous-catégories
        query = '''
        SELECT c.id, c.category_label, c.category_description, sc.sous_category_label
        FROM category c
        LEFT JOIN sous_category sc ON c.id = sc.category_id
        '''
        cursor.execute(query)

        # Récupération des résultats de la requête
        results = cursor.fetchall()

        # Fermeture du curseur et de la connexion à la base de données
        cursor.close()
        conn.close()

        # Conversion des résultats en format JSON
        data = []
        for row in results:
            category_id, category_label, category_description, sous_category_label = row
            category = {
                'id': category_id,
                'label': category_label,
                'description': category_description,
                'sous_categories': []
            }
            if sous_category_label:
                category['sous_categories'].append(sous_category_label)
            data.append(category)

        # Retour des catégories avec leurs sous-catégories en JSON
        return jsonify(data)

    except (psycopg2.Error, psycopg2.DatabaseError) as error:
        # Gestion des erreurs de connexion ou d'exécution de requêtes
        print(f"Erreur lors de la récupération des catégories : {error}")
        return jsonify({'error': 'Une erreur s\'est produite.'}), 500

# Lancement de l'API
if __name__ == '__main__':
    app.run()
