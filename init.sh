#!/bin/bash
# Fonction pour vérifier si Python 3.11 est installé
check_python_version() {
    PYTHON_VERSION=$(python3.11 --version 2>&1)
    if [[ $PYTHON_VERSION == *"Python 3.11"* ]]; then
        echo "Python 3.11 est déjà installé."
    else
        echo "Python 3.11 n'est pas installé. Installation..."
        install_python
    fi
}

# Fonction pour installer Python 3.11
install_python() {
    sudo apt update
    sudo apt install -y python3.11 python3.11-venv python3.11-dev
}

# Fonction pour installer pip pour Python 3.11
install_pip() {
    echo "Installation de pip pour Python 3.11..."
    wget https://bootstrap.pypa.io/get-pip.py
    sudo python3.11 get-pip.py --break-system-packages
}

# Fonction pour installer les dépendances Python
install_dependencies() {
    echo "Installation de Scapy avec apt..."
    sudo apt install -y python3-scapy

    echo "Installation de la bibliothèque Keyboard avec pip..."
    sudo python3.11 -m pip install keyboard --break-system-packages
}

# Fonction pour exécuter le script Python
run_python_script() {
    echo "Lancement du script Python..."
    sudo python3.11 /home/gonfiant/Bureau/Python-Exporter-flow/exporter-flow.py
}

# Vérification de la version de Python
check_python_version

# Installation de pip pour Python 3.11 si nécessaire
install_pip

# Installation des dépendances Python
install_dependencies

# Exécution du script Python
run_python_script
