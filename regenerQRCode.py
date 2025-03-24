import qrcode

# Création d'un QR code

def creationQRcode(n):
    # creation du QR code 
    creationQRcode = qrcode.make(n)
    # sauvegarde du QR code
    nomQrCode = input("Quel nom voulez-vous donner à votre QR code ?")
    return creationQRcode.save(nomQrCode + ".png")

