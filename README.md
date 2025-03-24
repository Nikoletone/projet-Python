# projet-Python
# Projet Python : Générateur et Lecteur de QR Code

## Description
Ce projet consiste à développer une application Python permettant de générer et de lire des QR codes à partir d’une interface graphique. L'application utilise plusieurs bibliothèques Python pour offrir des fonctionnalités complètes, notamment la génération, la lecture et l'affichage des QR codes.

## Fonctionnalités
- **Génération de QR codes** : Créez des QR codes à partir de texte ou d'URL.
- **Lecture de QR codes** : Scannez et extrayez le contenu des QR codes à partir d'images.
- **Interface graphique** : Une interface utilisateur simple et intuitive grâce à Tkinter.

## Prérequis
Assurez-vous d'avoir Python installé sur votre machine. Les bibliothèques suivantes doivent être installées :

- `qrcode`
- `Pillow`
- `opencv-python`
- `tkinter` (inclus par défaut avec Python)

Pour installer les dépendances, exécutez la commande suivante dans un terminal :
```bash
pip install qrcode[pil] opencv-python pillow