from flask import send_from_directory, send_file
from flask_restplus import Namespace, reqparse
from flask_restplus import Resource
from enum import Enum, auto
from .multiple_choices import paises, coordinadores
from .helpers import build_url, generate_qr_code
from urllib.parse import urlparse, urlunparse


formulario_ns = Namespace(
    "api/entrada",
    description="Maneja la creacion de codigos QR para registrar\
     entradas y salidas del evento.",
)

### Input


arg_parser = reqparse.RequestParser()
arg_parser.add_argument(
    "nombre",
    type=str,
    location="args",
    default="Pepito Perez",
    required=True,
)
arg_parser.add_argument(
    "link_form",
    type=str,
    location="args",
    default="https://docs.google.com/forms/d/e/1FAIpQLSdlfW5bcOK6dS4fLVhRHH4K7BxirzkYUEDOZJmgHYzVHJRf9w",
    help='Enlace del cuestionario con "viewform" al final',
)
arg_parser.add_argument(
    "coordinador",
    type=str,
    choices=tuple(coordinadores),
    location="args",
    required=True,
)
arg_parser.add_argument(
    "pais", type=str, choices=tuple(paises), location="args", required=True
)

url_question_names = {
    "nombre": "entry.1420785332",
    "coordinador": "entry.532722888",
    "pais": "entry.277792291",
}


def get_filled_form_url(link_form: str, nombre, coordinador, pais) -> str:
    """Returns complete url to view google form with filled answers.
    Example input: {nombre:Daniel Pacheco,coordinador: Ana Milena Garces Garces, pais: Italia}
    Example output:"https://docs.google.com/forms/d/e/1FAIpQLSdlfW5bcOK6dS4fLVhRHH4K7BxirzkYUEDOZJmgHYzVHJRf9w/viewform?usp=pp_url&entry.1420785332=Daniel+Pacheco&entry.532722888=Ana+Milena+Garces+Garces&entry.277792291=Italia"""
    # Ex. values=
    if "viewform" not in link_form:
        link_form += "viewform" if link_form[-1] == "/" else "/viewform"
    query_dict = {"nombre": nombre, "coordinador": coordinador, "pais": pais}

    # map keys to url keys
    url_query = dict(
        (url_question_names[name], val)
        for name, val in query_dict.items()
        if name in url_question_names
    )
    url_query["usp"] = "pp_url"
    return build_url(link_form, args_dict=url_query)


### Resources
@formulario_ns.route("/")
class FormularioController(Resource):
    def __init__(self, api, *args, **kwargs):
        super().__init__(api=api, *args, **kwargs)

    @formulario_ns.expect(arg_parser)
    def get(self):
        args = arg_parser.parse_args()
        filled_questions_url = get_filled_form_url(**args)
        file_name = f"{args['nombre']}.PNG"
        img_as_bytes = generate_qr_code(file_name, filled_questions_url)
        return send_file(
            img_as_bytes,
            mimetype="image/png",
            as_attachment=True,
            attachment_filename=file_name,
        )
