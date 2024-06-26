import os
import sys
from threading import Timer, Thread
from scapy.all import sniff, get_if_list, IP, TCP, UDP
from datetime import datetime
import json
import keyboard  # Assurez-vous que la bibliothèque keyboard est installée

# Cette fonction affiche les interfaces réseau disponibles
def afficher_interfaces():
    print("Interfaces réseau disponibles:")
    for interface in get_if_list():
        print(f"- {interface}")

# Cette fonction permet à l'utilisateur de choisir les interfaces à surveiller
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

# Cette fonction génère le chemin du fichier de log
def generer_chemin_log(interface, log_dossier_base):
    now = datetime.now()
    nom_fichier = f"{interface}-netflow-{now.strftime('%d-%m-%Y-%H-%M')}.json"
    dossier_interface = os.path.join(log_dossier_base, interface)
    if not os.path.exists(dossier_interface):
        os.makedirs(dossier_interface)
    return os.path.join(dossier_interface, nom_fichier)

# Cette fonction traite les paquets capturés et les écrit dans un fichier de log
def traiter_paquet(paquet, log_path):
    if IP in paquet:
        flux_info = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'src_ip': paquet[IP].src,
            'dst_ip': paquet[IP].dst,
            'src_port': paquet[TCP].sport if TCP in paquet else paquet[UDP].sport if UDP in paquet else None,
            'dst_port': paquet[TCP].dport if TCP in paquet else paquet[UDP].dport if UDP in paquet else None,
            'protocol': paquet.sprintf("%IP.proto%"),
            'length': len(paquet)
        }

        # Extraire et enregistrer les flags TCP si le paquet est un paquet TCP
        if TCP in paquet:
            flags = paquet[TCP].flags
            flag_str = ''
            if flags & 0x01: flag_str += 'F'
            if flags & 0x02: flag_str += 'S'
            if flags & 0x04: flag_str += 'R'
            if flags & 0x08: flag_str += 'P'
            if flags & 0x10: flag_str += 'A'
            if flags & 0x20: flag_str += 'U'
            flux_info['tcp_flags'] = flag_str

        with open(log_path, "a") as log_file:
            log_file.write(json.dumps(flux_info) + "\n")


# Cette fonction démarre la surveillance de l'interface spécifiée
def demarrer_surveillance(interface, log_dossier_base):
    log_path = generer_chemin_log(interface, log_dossier_base)
    print(f"Surveillance de l'interface {interface} démarrée...")
    sniff(iface=interface, prn=lambda paquet: traiter_paquet(paquet, log_path), store=False)

# Cette fonction arrête la surveillance des interfaces
def stop_surveillance():
    print("\nArrêt de la surveillance des interfaces...")
    os._exit(0)  # Arrête tous les threads et termine le programme

def main():
    afficher_interfaces()
    interfaces = choisir_interfaces()

    log_dossier_base = input("Entrez le chemin absolu pour stocker les dossiers de logs (laissez vide pour le répertoire par défaut): ")
    if not log_dossier_base:
        log_dossier_base = "./netflow-logs"
        if not os.path.exists(log_dossier_base):
            os.mkdir(log_dossier_base)

    surveillance_threads = []
    for interface in interfaces:
        t = Thread(target=demarrer_surveillance, args=(interface, log_dossier_base))
        t.start()
        surveillance_threads.append(t)

    print("\nAppuyez sur 'q' pour arrêter la surveillance.")
    keyboard.wait('q')
    stop_surveillance()

    for t in surveillance_threads:
        t.join()

if __name__ == "__main__":
    main()
