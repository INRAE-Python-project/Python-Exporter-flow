# Application exporteur de flux d'un réseau

## Objectif

Cette application a pour but de surveiller le trafic réseau sur une ou plusieurs interfaces spécifiées, d'enregistrer les détails des paquets dans des fichiers de log et de fournir une méthode d'arrêt propre de la surveillance à travers une interaction utilisateur.

## Fonctionnement

L'application lance une surveillance réseau sur les interfaces sélectionnées par l'utilisateur. Pour chaque interface, elle crée des fichiers de log dans un dossier spécifié (ou un dossier par défaut si aucun chemin n'est donné) avec une rotation toutes les 5 minutes pour éviter la surcharge des fichiers uniques. Les utilisateurs peuvent arrêter la surveillance en appuyant sur la touche 'z', ce qui termine proprement tous les processus et threads en cours d'exécution.

## Prérequis

- Posséder les droits d'administrateur sur la machine.
- Python 3.11
- Bibliotheques Python : `os`, `sys`, `threading`, `scapy`, `datetime`, `multiprocessing`, `keyboard`.

## Installation

- Installez Python 3.11 si ce n'est pas déjà fait.
- Installez la bibliothèque Scapy en utilisant pip : `pip install scapy` sur windows sinon `pip install scapy --break-system-packages` sur une distribution linux.
- Installez la bibliothèque Keyboard : `pip install keyboard` sur windows sinon `pip install keyboard --break-system-packages` sur linux.
- Clonez ou téléchargez le script de l'application depuis son dépôt.

## Lancement du script

- Ouvrez un terminal ou une invite de commande.
- Naviguez jusqu'au dossier contenant le script.
- Lancez le script en utilisant la commande : python <nom_du_script>.py.
- Suivez les instructions à l'écran pour sélectionner les interfaces à surveiller et spécifier le chemin pour les fichiers de log.
- Une fois la surveillance démarrée, vous pouvez la terminer à tout moment en appuyant sur la touche 'z'.

## Aide

Pour vous aidez à installer python et les dépendances, vous pouvez exécuter le script "init.sh" qui est à la racine du projet
qui va installer python et les dépendances nécessaires.

### Exécution du script d'initialisation



## Auteur

Gaëtan GONFIANTINI