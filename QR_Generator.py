import qrcode as qr

print("Welcome To QR Generator")

Website = input("Enter The Website's URL : ")
N = input("Enter The Name Of QR File : ")
Name = (N +'.png')

img = qr.make(Website)
img.save(Name)