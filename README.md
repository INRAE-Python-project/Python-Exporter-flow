# Application exporteur de flux d'un réseau

## Objectif

Cette application a pour but de surveiller le trafic réseau sur une ou plusieurs interfaces spécifiées, d'enregistrer les détails des paquets dans des fichiers de log et de fournir une méthode d'arrêt propre de la surveillance à travers une interaction utilisateur.

## Fonctionnement

L'application lance une surveillance réseau sur les interfaces sélectionnées par l'utilisateur. Pour chaque interface, elle crée des fichiers de log dans un dossier spécifié (ou un dossier par défaut si aucun chemin n'est donné) avec une rotation toutes les 5 minutes pour éviter la surcharge des fichiers uniques. Les utilisateurs peuvent arrêter la surveillance en appuyant sur la touche 'z', ce qui termine proprement tous les processus et threads en cours d'exécution.

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
