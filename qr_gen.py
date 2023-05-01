import argparse
import qrcode
from PIL import Image

# Define the function generate qr
def generate_qr(input_str):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(input_str)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    return img

# Define the function save qr
def save_qr(input_str, filename):
    img = generate_qr(input_str)
    img.save(filename)

# Define the function show qr
def show_qr(input_str):
    img = generate_qr(input_str)
    img.show()

# define main function
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_str', help='input string', required=True)
    parser.add_argument('-f', '--filename', help='filename', required=True)
    args = parser.parse_args()
    input_str = args.input_str
    filename = args.filename
    save_qr(input_str, filename)

if __name__ == '__main__':
    main()