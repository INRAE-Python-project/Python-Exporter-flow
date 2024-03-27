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
# Fonction pour vérifier et installer pip pour Python 3.11 si nécessaire
install_pip() {
    if ! python3.11 -m pip --version &> /dev/null; then
        echo "pip pour Python 3.11 n'est pas installé. Installation..."
        wget -O get-pip.py https://bootstrap.pypa.io/get-pip.py
        sudo python3.11 get-pip.py --break-system-packages
        rm get-pip.py
    else
        echo "pip pour Python 3.11 est déjà installé."
    fi
}

# Fonction pour installer les dépendances Python si nécessaire
install_dependencies() {
    if ! python3.11 -c "import scapy" &> /dev/null; then
        echo "Installation de Scapy avec apt..."
        sudo apt install -y python3-scapy
    else
        echo "Scapy est déjà installé."
    fi

    if ! python3.11 -c "import keyboard" &> /dev/null; then
        echo "Installation de la bibliothèque Keyboard avec pip..."
        sudo python3.11 -m pip install keyboard --break-system-packages
    else
        echo "La bibliothèque Keyboard est déjà installée."
    fi
}

# Fonction pour exécuter le script Python
run_python_script() {
    echo "Lancement du script Python..."
    sudo python3.11 ./exporter-flow.py
}

# Vérification de la version de Python
check_python_version

# Installation de pip pour Python 3.11 si nécessaire
install_pip

# Installation des dépendances Python si nécessaire
install_dependencies

# Exécution du script Python
run_python_script
