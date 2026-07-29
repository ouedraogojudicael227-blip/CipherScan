# 🔐 CipherScan

CipherScan est un scanner de ports TCP développé en Python dans un but d'apprentissage de la programmation réseau et de la cybersécurité.

## Fonctionnalités

- Scan TCP de ports
- Scan multithread (ThreadPoolExecutor)
- Résolution des noms de domaine (DNS)
- Détection des services connus
- Banner Grabbing
- Barre de progression (tqdm)
- Rapports TXT
- Rapports JSON
- Validation des entrées utilisateur
- Architecture modulaire

## Structure du projet

```
CipherScan/
│
├── main.py
├── scanner.py
├── network.py
├── ports.py
├── services.py
├── banner.py
├── report.py
├── config.py
├── utils.py
│
├── reports/
├── logs/
└── README.md
```

## Installation

Clonez le dépôt :

```bash
git clone https://github.com/ouedraogojudicael227@gmail-blip/CipherScan.git
```

Accédez au dossier :

```bash
cd CipherScan
```

Installez les dépendances :

```bash
pip install tqdm colorama
```

## Utilisation

### Mode interactif

```bash
python main.py
```

### Mode ligne de commande

```bash
python main.py -t scanme.nmap.org -p 20-100
```

## Exemple de sortie

```
========================================
CipherScan - Version 1.0
========================================

Target : scanme.nmap.org

[+] Port 22    OPEN    SSH
[+] Port 80    OPEN    HTTP
[+] Port 443   OPEN    HTTPS

Scan finished.

Ports scanned : 81
Open ports : 3
Duration : 0.42 seconds
```

## Rapports générés

Les rapports sont enregistrés dans le dossier `reports/` :

- TXT
- JSON

## Technologies utilisées

- Python 3
- socket
- concurrent.futures
- argparse
- tqdm
- colorama
- json

## Objectifs pédagogiques

Ce projet m'a permis d'apprendre :

- les sockets TCP
- le multithreading
- la programmation modulaire
- les fonctions Python
- la gestion des exceptions
- les fichiers JSON et TXT
- la cybersécurité réseau

## Avertissement

Cet outil est destiné uniquement à des fins éducatives et à l'analyse de systèmes pour lesquels vous disposez d'une autorisation. N'utilisez jamais CipherScan sur des systèmes ou des réseaux sans permission.

## Auteur

Développé par Judicaël Ouedraogo.
