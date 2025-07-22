# Gestion-Gaz-App

Gestion-Gaz-App est une application web pour la gestion avancée des détecteurs de gaz portables et fixes. Elle permet le suivi des équipements, la planification de la maintenance et la gestion de l'historique des interventions.

## Fonctionnalités clés
- **Gestion des équipements** : enregistrement des détecteurs avec marque, modèle, numéro de série et types de capteurs.
- **Historique des interventions** : suivi des maintenances réalisées pour chaque appareil.
- **Alertes d'obsolescence** : dates de fin de vie enregistrées avec commande de vérification.
- **Gestion des garanties** : suivi de la date de fin de garantie des équipements.
- **Suivi de la maintenance** : création d'enregistrements de maintenance avec dates et descriptions.
- **Administration** : interface d'administration Django pour gérer les appareils et les maintenances.
- **Authentification** : connexion des utilisateurs avec rôles (Admin, Technicien, Client, Manager).
- **Tableau de bord** : vue synthétique affichant le nombre d'équipements et de maintenances enregistrés.

## Démarrage rapide
1. Installez les dépendances : `pip install -r requirements.txt`.
2. Appliquez les migrations : `python manage.py migrate`.
3. Lancez le serveur de développement : `python manage.py runserver`.
4. Accédez au tableau de bord sur `http://localhost:8000/`.
5. Exécutez les tests : `pytest`.
6. Créez les rôles par défaut : `python manage.py create_roles`.
7. Vérifiez l'obsolescence des équipements : `python manage.py check_obsolescence`.

Ce dépôt fournit une base minimale destinée à être étendue avec des modules supplémentaires (gestion des stocks, planification, etc.).
