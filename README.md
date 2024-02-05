Repositorio asociado a implementacion de bot en discord, para gestion de informacion de usuarios y asistencia en eventos registrados, mediante implementacion de controlador, modelos y servicios, para el guardado de datos en base de datos SQLite, esto mediante la habilitacion de una lista de comandos
de lectura y escritura destinados para ser usados en el chat de discord una vez se encuentre activo.

Consideraciones:

- Para obtener las instrucciones de interaccion con el bot de discord, deberemos ponerlo en funcionamiento y en discord emplear el comando.
- `$help` <- Encontraremos toda la informacion necesaria con este comando.

- Para el funcionamiento de la aplicacion se recomienda importar el token del bot de discord, como variable de entorno bajo el nombre "TOKEN".

- Se utilizaron las librerias de discord para establecer el funcionamiento del bot, openpyxl para poder generar archivos en excel, con el fin de ser adjuntados a discord, coverage, pytest, y pytest-asyncio para permitir el analisis y testeo de la aplicacion.

- Estas librerias se encuentran registradas en "requirements.txt", y son instalables desde este archivo mediante el comando:

- `pip install -r requirements.txt`

- Para poder ejecutar los test, podemos hacerlo estando ubicados en la raiz del proyecto en la consola, empleando los comandos
- `python3 -m pytest Test/test.py -v` <- Cada parametro 'v' permite visualizar mas informacion
- `python3 -m pytest -s Test/test.py` <- El parametro -s permite mostrar las impresiones en consola

- Si se desea revisar el coverage del proyecto, podemos emplear los comandos:
- `coverage run -m pytest Test/test.py -v` 
- `coverage report` <- Muestra el reporte general.
- `coverage report --show-missing` <- Muestra el reporte con indicaciones de las lineas de instruccion que no fueron utilizadas durante el test.

- El archivo .coveragerc posee indicaciones de los directorios que coverage debe ignorar en su reporte.

Por: 
Ing. Luis Miguel Galán Salazar