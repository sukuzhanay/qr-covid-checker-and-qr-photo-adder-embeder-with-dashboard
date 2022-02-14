# _**QrCovid**_
## Qr covid _checker & watermark_ photo with dashboard
_**QrCovid**_ comprueba si el qr del pasaporte covid es autentico, ademas crea un qr con la foto del titular evitando sacar el DNI y permite conocer, entre otros: el estado de vacunación, tiempo medio desde la ultima vacunación, vacunas mas usadas.

![Design](https://github.com/sukuzhanay/qr-covid-checker-and-qr-photo-adder-embeder-with-dashboard/blob/main/qrcovid.drawio.png)

[![Run on Repl.it](https://repl.it/badge/github/sukuzhanay/chat_using_sockets)](https://repl.it/github/sukuzhanay/chat_using_sockets)

### Proyecto final de la asignatura de Programación Concurrente y Distribuida .  
Prof.: **Christian Vladimir Sucuzhanay Arevalo** 

Repositorio que alberga el proyecto de programación concurrente y distribuida, contará con las funcionalidades siguientes:
![Logo of the project](https://github.com/sukuzhanay/qr-covid-checker-and-qr-photo-adder-embeder-with-dashboard/blob/main/uem%20logo.jpeg)


1. **Comprueba** que el **Qr** de un pasaporte Covid sea válido
2. **Genera** un nuevo **Qr** con la **foto** del titular, evitando tener que sacar **DNI** ( matricula de honor )
3. **Dashboard** interactivo del estado del vacunación de la Universidad Europea

### Autores
1. **Christian Vladimir Sucuzhanay Arevalo** ( Profesor )
2. **Carlos Moreno** ( jefe, grupo 1 ) **_Datos del Dashboard_**
3. **Camilo Quiroz** (jefe, grupo 2) **_Pathcheck/ nodejs_**
3. **Jolie Alain** ( jefe, grupo 3 ) **QrPhoto / embeber / UI / Auth**
4. **Maria Rodriguez** ( jefe, grupo 4 )**DDBB design / Guardado y sanitizar DDBB / Check already user**
5. **Santiago Barreiro** ( jefe grupo 5 ) **HC1 to endpoint**

### Estructura y tecnologías usadas en _**QrCovid**_

**FrontEnd**

1. Streamlit
2. Python
3. Dashboard Plotly 
4. JavaScript
5. Github
6. ![](www.google.es "Figma")

**Backend**

1. Firebase
2. Base de datos NoSql ( realtime database )
3. Storage ( almacenamiento de Qrs)
4. Autentificacion (auth)
5. Dashboard Plotly 
6. Python
7. Javascript
8. Github
9. Figma

**API`s**

[Pathcheck](https://github.pathcheck.org/verify.html#processed  "Verifica tu Qr")



![Logo of the project](https://github.com/sukuzhanay/qr-covid-checker-and-qr-photo-adder-embeder-with-dashboard/blob/main/uem%20logo.jpeg)


###Como hacer funcionar el programa

Para hacer funcionar el programa solo es necesario los siguientes 5 archivos:
·prueba.py
·main.py
·crearQr.py
·camara2.py
·hc1_decode.py

Los demas archivos pueden crear conflicto en el funcionamiento del programa pero sirven para mostrar el desarrollo llevado a cabo para lograr su creacion.

Una vez aislados los siguientes archivos, se ejecuta el archivo **prueba.py**. Al utilizarse la libreria streamlit, para ejecutar el archivo sera necesario por terminal escribir lo siguiente: **streamlit run [ PATH de prueba.py ]**. Una vez hecho esto, al abrirse el navegador se mostrara en un sidebar el login. En caso de no estar registrado, seleccione la opcion de registrarse y si ya esta registrado, seleccione la opcion de login y una vez introduzca los datos correctos podra visualizar el dashboard automaticamente.

**IMPORTANTE:** Es necesario tener descargadas todas las librerias necesarias para los 5 archivos en el interpretador de Python que vaya a utilizar. Consultar _imports_ de los ficheros.