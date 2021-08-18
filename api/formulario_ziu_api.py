from flask import send_from_directory, send_file
from flask_restplus import Namespace, reqparse
from flask_restplus import Resource
from enum import Enum, auto
from .multiple_choices import paises, coordinadores
from .helpers import build_url
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
    "link_formulario",
    type=str,
    location="args",
    default="https://docs.google.com/forms/d/e/1FAIpQLSdlfW5bcOK6dS4fLVhRHH4K7BxirzkYUEDOZJmgHYzVHJRf9w/viewform/",
    # values="https://docs.google.com/forms/d/e/1FAIpQLSdlfW5bcOK6dS4fLVhRHH4K7BxirzkYUEDOZJmgHYzVHJRf9w/viewform?usp=pp_url&entry.1420785332=Daniel+Pacheco&entry.532722888=Ana+Milena+Garces+Garces&entry.277792291=Italia&entry.201993311=Salida+Hotel+Sabado"
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

### Resources
@formulario_ns.route("/")
class FormularioController(Resource):
    def __init__(self, api, *args, **kwargs):
        super().__init__(api=api, *args, **kwargs)

    @formulario_ns.expect(arg_parser)
    def get(self):
        args = arg_parser.parse_args()
        base_link = args["link_formulario"]

        url_query = dict(
            (url_question_names[name], val)
            for name, val in args.items()
            if name in url_question_names
        )
        url_query["usp"] = "pp_url"

        filled_questions_url = build_url(base_link, args_dict=url_query)
        return filled_questions_url
