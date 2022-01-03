Punto 1

Para ejecutar el proyecto es necesario lo siguiente:

- instalar NodeJS de la web https://nodejs.org/es/download/ (la versión LTS). La última versión da fallos.

- SI TIENES ANDROID PUEDES OBVIAR LOS SIGUIENTES PASOS HASTA EL PUNTO 2 YA QUE LO ÚNICO QUE NECESITARIAS ES DESCARGA LA APP EXPO. EL LOGO
ES UNA V INVERTIDA EN BLANCO Y NEGRO.

- instalamos Visual Studio para usar el simulador de Android (este es nuestro caso).

- Despues de instalar todo y abrirse el IDLE. Si no hemos abierto ningun proyecto hacemos clic en More
  actions y en AVD Manager. Esta opción tambien se encuentra en tools y AVD Manger.
  Entramos en Create Virtual Device y en los recomendados, seleccionamos alguno de los dispositivos que tengan Play Store.
  El símbolo aparece en la segunda columna. Seleccionamos uno de ellos y acto seguido elegimos la versión más reciente en
  mi caso R. Descargamos esa versión, y al finalizar la seleccionamos y le damos siguiente y luego finalizar.
  Aquí terminaría de instalar el simulador android. Pasamos a React Native.





Punto 2.

- Abrir cmd como administrador. Ejecutar los siguientes comandos:
  - yarn global add expo-cli

  - nos desplazamos al directorio donde queremos crear el proyecto de REACT NATIVE. En mi caso el escritorio. cd C:\Users\camilo\Desktop\

  - Introducimos el siguiente comando. expo init NombreProyecto

  - entramos dentro del directorio. cd NombreProyecto

  - usamos git clone para descargar el repositorio de GitHub. git clone https://reactnative.dev/docs/environment-setup .

  - Al descargar los directorios, crearemos un archivo en el directorio Android con nombre local.properties donde introduciremos la siguiente línea (incluyendo las doble \\),
    sdk.dir=C:\\Users\\camilo\\AppData\\Local\\Android\\Sdk
    El Sdk del final puede variar. Puede ser sdk. En nuestro caso, se puede ver que es con la primera mayúscula.

  - Nos dirigimos a la carpeta "editar las Variables del entorno del sistema" de forma gráfica, y hacemos clic en la parte inferior donde pone
    Variables del entorno. En el cuadrado de arriba donde hace referencia a tu usuario, hacemos clic en Path, y seleccionamos la opción de editar.
    Añadimos una línea con la siguiente información: C:\Users\jcami\AppData\Local\Android\Sdk
    Otra línea con: C:\Users\jcami\AppData\Local\Android\Sdk\platform-tools
    Aceptamos y Aceptamos. Saldremos de las ventanas que hemos abierto. Ahora a través del CMD iremos a nuestro proyecto. En mi caso, como dije
    anteriormente, introduzco cd C:\Users\camilo\Desktop\NombreProyecto

  - Introducimos el comando npm install

  - Introducimos el comando react-native start (ya debería de iniciarse la APP). En caso de abrirse una ventana con un logo esta casí todo correcto.
  Solo faltaría verificar que se conecte al dispositivo virtual android.

  - Sin cerrar el CMD, volvemos a android studio, al AVD Manager, y arrancamos nuestro dispositivo instalado haciendo clic en el icono de
  play en el apartado de actions.

  - Esperamos que cargue e inicie el dispositivo. Una vez finalice su carga, introducimos el comando react-native run-android

  - Ya debería de haberse iniciado el proceso de descarga y configuración. Al terminar de cargar, os dirigis al dispositivo virtual y veréis
  que ha cargado la App.
