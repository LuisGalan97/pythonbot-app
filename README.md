# Aplicacion pythonbot
Repositorio asociado a aplicacion desarrollada en lenguaje python para implementacion de bot en discord, diseñado para la gestion de informacion asociada a una lista de usuarios, asistencias y eventos registrados, esto mediante implementacion de controladores, modelos y servicios, estructurados para el correcto guardado de datos en una base de datos diseñada y desplegada en SQLite. La interaccion con el bot se permite mediante la habilitacion de comandos empleables en el chat de un servidor con los permisos apropiados, para la posterior lectura y escritura de datos en la base de datos.

## Instalacion
En esta seccion se explicarán los pasos para habilitar ___pythonbot-app___ con el fin de explorar todas sus funcionalidades.

### 1. Crear un servidor en discord
Como primer paso es necesario habilitar un servidor de discord que servirá de interfaz de usuario, para permitir la interaccion entre el usuario con __pythonbot-app__.

![Imagen GUI](https://github.com/LuisGalan97/pythonbot-app/blob/docs/docs/1.png)
![Imagen GUI](https://github.com/LuisGalan97/pythonbot-app/blob/docs/docs/2.png)

### 2. Registrar y configurar un bot en discord
Ahora debemos registrar un bot en la plataforma de desarrollo de discord, este funcionará como instancia fisica para __pythonbot-app__, para ello nos dirigirnos al enlace:

https://discord.com/developers/applications

Una vez allí, creamos una nueva aplicacion, especificando un nombre y un logo(opcional).

![Imagen GUI](https://github.com/LuisGalan97/pythonbot-app/blob/docs/docs/3.png)
![Imagen GUI](https://github.com/LuisGalan97/pythonbot-app/blob/docs/docs/4.png)
![Imagen GUI](https://github.com/LuisGalan97/pythonbot-app/blob/docs/docs/5.png)

Buscamos el apartado "bot" y pulsamos el boton ___Reset Token___ para generar un token para el acceso de __pythonbot-app__ a la instancia del bot que hemos registrado en discord. Es muy importante tener anotado pues lo usaremos mas adelante.

![Imagen GUI](https://github.com/LuisGalan97/pythonbot-app/blob/docs/docs/6.png)

Vamos a la seccion "Privileged Gateway Intents", activamos las tres opciones evidenciadas en la imagen y guardamos cambios.

![Imagen GUI](https://github.com/LuisGalan97/pythonbot-app/blob/docs/docs/7.png)

Nos dirigimos al apartado "OAuth2" y en la seccion "OAuth2 URL Generator", activamos las opciones mostradas en la imagen.

![Imagen GUI](https://github.com/LuisGalan97/pythonbot-app/blob/docs/docs/8.png)

En la seccion "BOT PERMISSIONS" activamos los siguientes permisos.

![Imagen GUI](https://github.com/LuisGalan97/pythonbot-app/blob/docs/docs/9.png)

Por ultimo vamos al apartado "GENERATED URL", y guardamos el enlace que esta dispuesto en el mismo, ya que lo utilizaremos mas adelante para poder añadir la instancia del bot a un servidor de discord.

![Imagen GUI](https://github.com/LuisGalan97/pythonbot-app/blob/docs/docs/10.png)

#### Agregar la aplicacion al servidor
En esta seccion enlazaremos la aplicacion/instancia del bot previamente configurada, al servidor que tambien creamos previamente en discord, para ello, del enlace que guardamos en la seccion anterior, lo copiamos y pegamos en el navegador. Al hacerlo, este nos dirigirá a nuestra sesion en discord si se encuentra abierta (en caso de no estarlo pedira iniciar sesion) y nos solicitará seleccionar el servidor al cual queremos enlazar el bot, para el cual escogemos el creado previamente en pasos anteriores y pulsamos en "continuar".

![Imagen GUI](https://github.com/LuisGalan97/pythonbot-app/blob/docs/docs/11.png)
![Imagen GUI](https://github.com/LuisGalan97/pythonbot-app/blob/docs/docs/12.png)

Posteriormente se nos pedirá confirmar si los permisos asignados al bot son los adecuados, no modificamos nada y pulsamos en "autorizar".

![Imagen GUI](https://github.com/LuisGalan97/pythonbot-app/blob/docs/docs/13.png)

Con lo anterior nuestra instancia del bot se habrá añadido satisfactoriamente al servidor de discord que tambien creamos previamente para este proyecto.

![Imagen GUI](https://github.com/LuisGalan97/pythonbot-app/blob/docs/docs/14.png)
![Imagen GUI](https://github.com/LuisGalan97/pythonbot-app/blob/docs/docs/15.png)

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
