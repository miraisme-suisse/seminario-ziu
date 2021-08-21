from flask_restplus import Api
from flask import url_for
from .formulario_ziu_api import formulario_ns
import os

if not os.environ.get("ENV"):

    @property
    def specs_url(self):
        return url_for(self.endpoint("specs"), _external=True, _scheme="https")

    Api.specs_url = specs_url

api = Api(
    title="ZIU Codigo QR generador API",
    version="1.0",
    description="Esta API va a crear codigos QR para \
    las personas que asistan al seminario de ZIU en Palexpo en 2021.",
)

api.add_namespace(formulario_ns)
