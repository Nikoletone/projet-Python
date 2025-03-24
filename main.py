import regenerQRCode



print("Welcome to the QR Code Regenerator")
print("")
print("1. Create a QR code")
print("2. Regenerate a QR code")
print("3. Exit")
print("")
choice = input("Enter your choice: ")

if choice == "1":
    n = input("Enter the text or the URl you want to convert to a QR code: ")
    regenerQRCode.creationQRcode(n)