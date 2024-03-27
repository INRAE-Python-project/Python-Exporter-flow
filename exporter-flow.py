import os
import sys
from threading import Timer, Thread
from scapy.all import sniff, get_if_list
from datetime import datetime
from multiprocessing import Process
import keyboard  # Nécessite 'pip install keyboard'

# Variables globales pour les processus et les timers
processus = []
timers = []

def afficher_interfaces():
    print("Interfaces réseau disponibles:")
    for interface in get_if_list():
        print(f"- {interface}")

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

def generer_chemin_log(interface, log_dossier_base):
    now = datetime.now()
    nom_fichier = f"{interface}-log-{now.strftime('%Y-%m-%d-%H-%M')}.txt"
    dossier_interface = os.path.join(log_dossier_base, interface)
    if not os.path.exists(dossier_interface):
        os.makedirs(dossier_interface)
    return os.path.join(dossier_interface, nom_fichier)

def traiter_paquet(paquet, log_path):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, "a") as f:
        f.write(f"{timestamp} - Paquet capturé: {paquet.summary()}\n")

def changer_log(interface, log_dossier_base):
    log_path = generer_chemin_log(interface, log_dossier_base)
    timer = Timer(300, changer_log, args=(interface, log_dossier_base))
    timer.start()
    timers.append(timer)
    return log_path

def demarrer_surveillance(interface, dossier_base):
    log_path = changer_log(interface, dossier_base)
    print(f"Surveillance de l'interface {interface} démarrée...")
    sniff(iface=interface, prn=lambda paquet: traiter_paquet(paquet, log_path), store=False)

def ecouter_stop():
    print("\nAppuyez sur 'z' pour arrêter le script proprement.")
    keyboard.wait('z')
    print("\nArrêt de tous les processus de surveillance...")
    for timer in timers:
        timer.cancel()
    for p in processus:
        p.terminate()
    sys.exit(0)

def main():
    afficher_interfaces()
    interfaces = choisir_interfaces()

    log_dossier_base = input("Entrez le chemin absolu pour stocker les dossiers de logs (laissez vide pour le répertoire par défaut): ")
    if not log_dossier_base:
        log_dossier_base = "./folder-log"
        if not os.path.exists(log_dossier_base):
            os.mkdir(log_dossier_base)


    stop_listener = Thread(target=ecouter_stop)
    stop_listener.start()
    for interface in interfaces:
        p = Process(target=demarrer_surveillance, args=(interface, log_dossier_base))
        processus.append(p)
        p.start()



    for p in processus:
        p.join()

if __name__ == "__main__":
    main()
