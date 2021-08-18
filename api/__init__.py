from flask_restplus import Api
from .formulario_ziu_api import formulario_ns


api = Api(
    title="ZIU Codigo QR generador API",
    version="1.0",
    description="Esta API va a crear codigos QR para \
    las personas que asistan al seminario en Palexpo en 2021.",
)

api.add_namespace(formulario_ns)
