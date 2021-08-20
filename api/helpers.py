import urllib
import qrcode
from PIL import Image
from io import BytesIO


def build_url(base_url, args_dict=None):
    """Returns a url with query arguments"""
    url_parts = list(urllib.parse.urlparse(base_url))
    if args_dict is not None:
        url_parts[4] = urllib.parse.urlencode(args_dict)
    return urllib.parse.urlunparse(url_parts)


def generate_qr_code(filename, data: str) -> BytesIO:
    """Returns a byte array with a qr code image"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make()
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    img_byte_array = convert_to_byte_array(img)
    return img_byte_array


def convert_to_byte_array(img: Image):
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format="PNG")
    img_byte_arr.seek(0)
    return img_byte_arr
