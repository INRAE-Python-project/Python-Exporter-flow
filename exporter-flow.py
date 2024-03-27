import os
import sys
from scapy.all import sniff, get_if_list
from datetime import datetime

# Affiche toutes les interfaces réseau disponibles
def afficher_interfaces():
    print("Interfaces réseau disponibles:")
    for interface in get_if_list():
        print(f"- {interface}")

# Demande à l'utilisateur de choisir les interfaces à surveiller
def choisir_interfaces():
    interfaces = input("Entrez les interfaces à surveiller (séparées par une virgule): ")
    interfaces_choisies = [intf.strip() for intf in interfaces.split(",")]
    return interfaces_choisies

# Fonction de callback pour le traitement de chaque paquet capturé
def traiter_paquet(paquet):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, "a") as f:
        # Ici, vous pourriez formater les données capturées de manière similaire à NetFlow
        f.write(f"{timestamp} - Paquet capturé: {paquet.summary()}\n")

# Demande à l'utilisateur le chemin pour stocker les logs
def demander_chemin_log():
    chemin = input("Entrez le chemin absolu pour stocker les fichiers log (laissez vide pour le répertoire par défaut): ")
    if not chemin:
        chemin = "./folder-log"
        if not os.path.exists(chemin):
            os.mkdir(chemin)
    return chemin

# Programme principal
def main():

    afficher_interfaces()
    interfaces = choisir_interfaces()

    """
    log_dossier = demander_chemin_log()
    log_path = os.path.join(log_dossier, "netflow_log.txt")

    try:
        for interface in interfaces:
            print(f"Surveillance de l'interface {interface}...")
            # La fonction sniff de Scapy est bloquante, envisagez d'exécuter chaque capture dans son propre thread pour les interfaces multiples
            sniff(iface=interface, prn=traiter_paquet, store=False)
    except KeyboardInterrupt:
        print("Arrêt de la capture de paquets.")
    except Exception as e:
        print(f"Erreur: {e}")
        sys.exit(1)
    """

if __name__ == "__main__":
    main()

