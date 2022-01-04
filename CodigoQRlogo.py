import os
import qrcode
from PIL import Image


def make_qrcode(data, save_path='./qrcode.png', border=5, image_size=(300, 300), icon_path='', factor=3.5):
    # Generar cuerpo de código QR
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, border=border)
    qr.add_data(data)  # Escribir datos en código QR
    qr.make()
    qrcode_image = qr.make_image().resize(image_size, Image.ANTIALIAS).convert('RGBA')

    if icon_path:  # Pega un ícono en medio del código QR
        icon_size = int(image_size[0] / factor), int(image_size[1] / factor)
        icon = Image.open(icon_path).resize(icon_size, Image.ANTIALIAS).convert('RGBA')
        icon_margin = int((image_size[0] - icon_size[0]) / 2), int((image_size[1] - icon_size[1]) / 2)
        mask = Image.new('RGBA', icon_size, color='white')
        qrcode_image.paste(mask, icon_margin, mask)
        qrcode_image.paste(icon, icon_margin, icon)

    # Guarde el código QR como un archivo
    if not os.path.isdir(os.path.dirname(save_path)):
        os.makedirs(os.path.dirname(save_path))
    qrcode_image.save(save_path)


if __name__ == '__main__':
    url = 'https://github.com/alextruck10'
    make_qrcode(data=url, save_path='./xxxxxx.png', icon_path='per.png')