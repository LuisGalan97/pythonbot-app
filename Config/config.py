import os

class Config:
    TOKEN = os.environ.get("TOKEN")

#Es necesario añadir el TOKEN de discord como variable de entorno
#o en su defecto reemplazar la instruccion 'os.environ.get("TOKEN")'
#por el token en cuestion, pero no se recomienda esto ultimo.
