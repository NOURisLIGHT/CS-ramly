#install all the libraries needed (qrcode and Image)
#create a function that collects a text and converts it to qr code
#save the qr code as image
#run the function

#install all the libraries needed
import qrcode

def generate_code(text):
    
    qr = qrcode.QRCode (
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color = 'black', back_color = "red") # color of the shape and the background
    img.save("qrcode.png")  # Enter the name of your QRcode, make it refers to the thing it sends the user to.

url = input("Enter the link you want to convert into qrcode: ") # Enter the link it will send the user to
generate_code(url)  