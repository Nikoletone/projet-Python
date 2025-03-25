import regenerQRCode
import lireQRcode
import webbrowser



print("Welcome to the QR Code Regenerator")
print("")
print("1. Create a QR code")
print("2. Lire QR code")
print("3. Exit")
print("")
choice = input("Enter your choice: ")

if choice == "1":
    n = input("Enter the text or the URl you want to convert to a QR code: ")
    regenerQRCode.creationQRcode(n)
elif choice == "2":
    n = input("Enter le nom su qr code que vous voulez lire : ")
    webbrowser.open(lireQRcode.read_qr_code(n))
