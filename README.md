<h3><b>Aplicacion pythonbot</b></h3>

Repositorio asociado a aplicacion desarrollada en lenguaje python para implementacion de bot en discord, con el fin de permitir la gestion de informacion de usuarios y asistencia en eventos registrados, mediante implementacion de controlador, modelos y servicios, para el guardado de datos en base de datos SQLite, esto mediante la habilitacion de una lista de comandos
de lectura y escritura destinados para ser usados en el chat de discord una vez se encuentre activo.

**Consideraciones:**

- _Para obtener las instrucciones de interaccion con el bot de discord, deberemos ponerlo en funcionamiento para posteriormente en discord emplear el comando._<br />`$help` <- _Con esto encontraremos toda la informacion asociada a su modo de uso._

- _Para el funcionamiento de la aplicacion se recomienda importar el token del bot de discord, como variable de entorno bajo el nombre "TOKEN"._

- _Se utilizaron las librerias de discord para establecer el funcionamiento del bot, openpyxl para poder generar archivos en excel, con el fin de ser adjuntados a discord, coverage, pytest, y pytest-asyncio para permitir el analisis y testeo de la aplicacion._

- _Estas librerias se encuentran registradas en "requirements.txt", y son instalables desde este archivo mediante el comando:_ <br /> `pip install -r requirements.txt`

- _Para poder ejecutar los test, podemos hacerlo estando ubicados en la raiz del proyecto en la consola, empleando los comandos:_ <br /> `python3 -m pytest Test/test.py -v` <- _Cada parametro 'v' permite visualizar mas informacion._ <br /> `python3 -m pytest -s Test/test.py` <- _El parametro -s permite mostrar las impresiones en consola._

- _Si se desea revisar el coverage del proyecto, podemos emplear los comandos:_ <br /> `coverage run -m pytest Test/test.py -v` <br /> `coverage report` <- _Muestra el reporte general._ <br /> `coverage report --show-missing` <- _Muestra el reporte con indicaciones de las lineas de instruccion que no fueron utilizadas durante el test._

- _El archivo .coveragerc posee indicaciones de los directorios que coverage debe ignorar en su reporte._

Por: 
Ing. Luis Miguel Galán Salazar