import os
import signal
import sys
from threading import Timer
from scapy.all import sniff, get_if_list
from datetime import datetime
from multiprocessing import Process, current_process

# Affiche toutes les interfaces réseau disponibles
def afficher_interfaces():
    print("Interfaces réseau disponibles:")
    for interface in get_if_list():
        print(f"- {interface}")

# Demande à l'utilisateur de choisir les interfaces à surveiller
def choisir_interfaces():
    interfaces = input("Entrez les interfaces à surveiller (séparées par une virgule): ")
    interfaces_saisies = [intf.strip() for intf in interfaces.split(",")]
    interfaces_valides = []

    for interface in interfaces_saisies:
        if interface in get_if_list():
            interfaces_valides.append(interface)
        else:
            print(f"L'interface : {interface} n'existe pas.")

    return interfaces_valides

# Générer le chemin du fichier log basé sur l'heure actuelle
def generer_chemin_log(interface, log_dossier_base):
    now = datetime.now()
    nom_fichier = f"{interface}-log-{now.strftime('%Y-%m-%d-%H-%M')}.txt"
    dossier_interface = os.path.join(log_dossier_base, interface)
    if not os.path.exists(dossier_interface):
        os.makedirs(dossier_interface)
    return os.path.join(dossier_interface, nom_fichier)

# Fonction de callback pour le traitement de chaque paquet capturé
def traiter_paquet(paquet):
    global log_path
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, "a") as f:
        f.write(f"{timestamp} - Paquet capturé: {paquet.summary()}\n")

# Fonction pour changer le fichier de log toutes les 5 minutes
def changer_log():
    global log_path
    log_path = generer_chemin_log(current_interface, log_dossier_base)
    Timer(300, changer_log).start()  # Réinitialiser le timer toutes les 5 minutes

# Fonction pour démarrer la capture de paquets sur une interface
def demarrer_surveillance(interface, dossier_base):
    global log_dossier_base, current_interface, log_path
    log_dossier_base = dossier_base
    current_interface = interface
    log_path = generer_chemin_log(interface, log_dossier_base)
    changer_log()  # Initialise le premier fichier de log et le timer
    print(f"Surveillance de l'interface {interface} démarrée...")
    sniff(iface=interface, prn=traiter_paquet, store=False)

# Fonction pour gérer l'interruption du programme principal
def signal_handler(sig, frame):
    print("Arrêt de tous les processus de surveillance...")
    for p in processus:
        p.terminate()
    sys.exit(0)

# Programme principal
def main():
    global processus
    processus = []

    afficher_interfaces()
    interfaces = choisir_interfaces()

    log_dossier_base = input("Entrez le chemin absolu pour stocker les dossiers de logs (laissez vide pour le répertoire par défaut): ")
    if not log_dossier_base:
        log_dossier_base = "./folder-log"
        if not os.path.exists(log_dossier_base):
            os.mkdir(log_dossier_base)

    signal.signal(signal.SIGINT, signal_handler)

    for interface in interfaces:
        p = Process(target=demarrer_surveillance, args=(interface, log_dossier_base))
        processus.append(p)
        p.start()

    for p in processus:
        p.join()

if __name__ == "__main__":
    main()
