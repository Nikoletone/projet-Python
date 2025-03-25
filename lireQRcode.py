import PIL.Image
import pyzbar.pyzbar



def read_qr_code(filename):
    image = PIL.Image.open(filename)
    codes = pyzbar.pyzbar.decode(image)
    return codes[0].data.decode() if codes else None



