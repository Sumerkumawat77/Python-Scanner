import pyqrcode
import png
from PIL import Image
link = input("Enter anything to generate QR : ")
qr_code = pyqrcode.create(link)
qr_code.png("QRCode.png", scale=20)
img = Image.open("QRCode.png")
img.show()