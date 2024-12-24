# Aplicacion pythonbot
Repositorio asociado a aplicacion desarrollada en lenguaje python para implementacion de bot en discord, diseñado para la gestion de informacion asociada a una lista de usuarios, asistencias y eventos registrados, esto mediante implementacion de controladores, modelos y servicios, estructurados para el correcto guardado de datos en una base de datos diseñada y desplegada en SQLite. La interaccion con el bot se permite mediante la habilitacion de comandos empleables en el chat de un servidor con los permisos apropiados, para la posterior lectura y escritura de datos en la base de datos.

## Instalacion
En esta seccion se explicarán una serie de pasos para habilitar el funcionamiento de ___pythonbot-app___ con el fin de explorar todas sus funcionalidades.

### Crear un servidor en discord
Como primer paso es necesario habilitar un servidor de discord cuyo proposito será el de servir de interfaz de usuario, para permitir la interaccion entre el usuario con __pythonbot-app__.

![Imagen GUI](https://github.com/LuisGalan97/pythonbot-app/blob/docs/docs/1.png)
![Imagen GUI](https://github.com/LuisGalan97/pythonbot-app/blob/docs/docs/2.png)

### Registrar y configurar una aplicacion en discord
Ahora deberemos registrar la aplicacion en la plataforma de desarrollo de discord, esta funcionará como instancia fisica para __pythonbot-app__, para ello deberemos dirigirnos al enlace:

https://discord.com/developers/applications

Una vez allí, creamos una nueva aplicacion, especificando un nombre y un logo(opcional).

![Imagen GUI](https://github.com/LuisGalan97/pythonbot-app/blob/docs/docs/3.png)
![Imagen GUI](https://github.com/LuisGalan97/pythonbot-app/blob/docs/docs/4.png)
![Imagen GUI](https://github.com/LuisGalan97/pythonbot-app/blob/docs/docs/5.png)


#### Agregar la aplicacion al servidor
#### Configurar _pythonbot-app_ en un entorno
#### Ejecutar _pythonbot-app_ y explorar sus funcionalidades


### Consideraciones:

- _Para obtener las instrucciones de interaccion con el bot de discord, deberemos ponerlo en funcionamiento para posteriormente en el chat del servidor habilitado, emplear el comando_:<br />`$help` <- _Al hacerlo podremos encontrar toda la informacion asociada a su modo de uso._

- _Para el funcionamiento de la aplicacion se recomienda importar el token del bot de discord, como variable de entorno bajo el nombre "TOKEN"._

- _Se utilizaron las librerias de discord para establecer el funcionamiento del bot, openpyxl para poder generar archivos en excel, con el fin de ser adjuntados a discord, coverage, pytest, y pytest-asyncio para permitir el analisis y testeo de la aplicacion._

- _Estas librerias se encuentran registradas en "requirements.txt", y son instalables desde este archivo mediante el comando:_ <br /> `pip install -r requirements.txt`

- _Para poder ejecutar los test, podemos hacerlo estando ubicados en la raiz del proyecto en la consola, empleando los comandos:_ <br /> `python3 -m pytest Test/test.py -v` <- _Cada parametro 'v' permite visualizar mas informacion._ <br /> `python3 -m pytest -s Test/test.py` <- _El parametro -s permite mostrar las impresiones en consola._

- _Si se desea revisar el coverage del proyecto, podemos emplear los comandos:_ <br /> `coverage run -m pytest Test/test.py -v` <br /> `coverage report` <- _Muestra el reporte general._ <br /> `coverage report --show-missing` <- _Muestra el reporte con indicaciones de las lineas de instruccion que no fueron utilizadas durante el test._

- _El archivo .coveragerc posee indicaciones de los directorios que coverage debe ignorar en su reporte._

**Por:** <br />
Ing. Luis Miguel Galán Salazar <br />
**Ingeniero Mecatronico.**
