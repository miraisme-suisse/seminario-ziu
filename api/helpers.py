import urllib
import qrcode


def build_url(base_url, args_dict=None):
    # Returns a list in the structure of urlparse.ParseResult
    url_parts = list(urllib.parse.urlparse(base_url))
    if args_dict is not None:
        url_parts[4] = urllib.parse.urlencode(args_dict)
    return urllib.parse.urlunparse(url_parts)


def generate_qr_code(filename, data: str) -> str:
    """Returns a path location for"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    img = qr.make()
    img_path = f"./images/{filename}"
    img.save(img_path)
    return img_path
