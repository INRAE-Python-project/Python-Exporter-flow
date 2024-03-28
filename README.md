# Application exporteur de flux d'un réseau

## Objectif

Cette application vise à simuler la fonctionnalité d'un exportateur NetFlow en surveillant le trafic réseau sur des interfaces spécifiées par l'utilisateur. Elle enregistre les détails des paquets de données dans un format structuré pour faciliter l'analyse ultérieure, similaire à ce qu'un système NetFlow ferait dans un environnement réseau professionnel. En plus de la collecte de données, l'application offre également une méthode d'arrêt propre pour la surveillance, permettant une gestion efficace des ressources système et des données collectées.

## Fonctionnement

L'application lance une surveillance réseau sur les interfaces sélectionnées par l'utilisateur. Pour chaque interface, elle crée des fichiers de log dans un dossier spécifié (ou un dossier par défaut si aucun chemin n'est donné) avec une rotation toutes les 5 minutes pour éviter la surcharge des fichiers uniques. Les utilisateurs peuvent arrêter la surveillance en appuyant sur la touche 'q', ce qui termine proprement tous les processus et threads en cours d'exécution.

## Liste des actions du script

- **Affichage des interfaces réseau disponibles** : Le script commence par énumérer et afficher toutes les interfaces réseau disponibles sur la machine, permettant à l'utilisateur de choisir celles qu'il souhaite surveiller.

- **Sélection des interfaces pour la surveillance** : L'utilisateur est invité à entrer les interfaces réseau qu'il souhaite surveiller, séparées par des virgules. Le script vérifie que les interfaces entrées sont valides et disponibles.

- **Génération des chemins de fichiers de log** : Pour chaque interface sélectionnée, le script crée un chemin de fichier de log unique basé sur le nom de l'interface et l'horodatage actuel, assurant que les données sont enregistrées de manière organisée.

- **Capture et traitement des paquets** : Le script utilise Scapy pour capturer les paquets réseau sur les interfaces sélectionnées. Pour chaque paquet capturé, il extrait des informations telles que les adresses IP source et destination, les ports, le protocole et la taille du paquet.

- **Enregistrement des données de flux** : Les informations extraites de chaque paquet sont structurées en un format de données JSON et enregistrées dans les fichiers de log correspondants aux interfaces. Cela facilite l'analyse ultérieure des données de flux.

- **Mécanisme d'arrêt propre** : L'utilisateur peut arrêter la surveillance à tout moment de manière propre en appuyant sur la touche 'q'. Cette action déclenche l'arrêt de la capture des paquets et la fermeture des fichiers de log.

- **Gestion de la concurrence** : Le script lance la surveillance de chaque interface dans son propre thread, permettant la capture simultanée des paquets sur plusieurs interfaces sans blocage.

- **Création du dossier de logs** : Si le chemin spécifié pour stocker les fichiers de log n'existe pas, le script crée le dossier nécessaire, garantissant que les fichiers de log peuvent être correctement enregistrés.

## Prérequis

- Être administrateur sur la machine cible.
- Système d'exploitation : Ubuntu (version native, non WSL).

## Installation et lancement

### Utilisation du Script d'Initialisation

Pour faciliter l'installation de Python, des dépendances nécessaires et du lancement de l'application, un script d'initialisation init.sh est fourni. Pour l'utiliser :

1. Ouvrez un terminal
2. Naviguez jusqu'au dossier contenant le script `init.sh`.
3. Assurez-vous que le script a les droits d'exécution. Si nécessaire, accordez ces droits en exécutant : ``chmod +x init.sh``
4. Lancez le script d'initialisation en administrateur : ``sudo ./init.sh``

Ce script s'occupera d'installer Python 3.11 (si ce n'est pas déjà fait), ainsi que toutes les bibliothèques nécessaires. Ensuite, il lancera automatiquement l'application.

## Sélection des Interfaces et Chemin des Logs

- Une fois le script lancé, suivez les instructions affichées pour sélectionner les interfaces réseau à surveiller.

- Spécifiez le chemin où vous souhaitez stocker les fichiers de logs. Si vous laissez cette option vide, un dossier par défaut sera utilisé.

## Arrêt de la Surveillance

- Pour arrêter la surveillance, suivez la procédure indiquée dans le terminal (généralement, cela implique d'appuyer sur une touche spécifique).

## Aide et Support

En cas de difficulté ou pour toute question, veuillez vous référer à cette documentation ou contacter l'auteur.

## Auteur

Gaëtan GONFIANTINI
