# PiscineN2Webtech
Projet réalisé au cour de la "piscine" organisé en 2ème année

Pour creer la venv sur vos ordinateurs, 
    - Ouvrez un terminal 
    - Rendez-vous dans le dossier adéquat (racine)
    - Entrez la commande python -m venv env
Ensuite activez cette dernière : Windows : Il sera possible de devoir entrer la commande suivante en premier lieu :
                                                 Set-ExecutionPolicy Unrestricted -Scope Process
                                                 - Puis enfin activer l'environement avec : env\Scripts\activate
                               : Mac : source env/bin/activate
    - N'oubliez pas d'ouvrir votre env a chque fois que vous travaillez sur le projet

Installez Django (si vous avez deja python sinon installez python d'abord, pour savoir si vous l'avez entrez: python --version ), pour installer Django entrez pip install django

Pour creer un projet, rendez vous a la racine, entrez : django-admin startproject Nom_de_Projet
faites cd Nom_de_Projet

et entrez python manage.py runserver

Vous avez a présent un server en ligne (sur le port 8000)

dans le fichier settings.py n'oubliez pas d'ajouter votre application

Puis une fois cela fait faites les migrations avec les commandes :  python manage.py makemigrations
                                                                    python manage.py migrate
