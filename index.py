import qrcode
obj = qrcode.make( "http://www.youtube.com/c/Byspel?sub_confirmation=1")
imgQr = open( "qr.png", "wb")
obj.save( imgQr)
imgQr.close()