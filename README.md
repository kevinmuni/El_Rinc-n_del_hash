## El Rincón del Hash

El Rincón del Hash es una aplicación web educativa que ayuda a los estudiantes a entender cómo funcionan los hashes (como MD5, SHA-1 y SHA-256). Los usuarios pueden convertir texto, archivos o imágenes en hashes y aprender sobre el proceso detrás de su generación. 

//Te falta otro hash incluye el que falta 

## Tecnologías usadas

- *Frontend*:
  - *HTML*: Para la estructura de la página.
  - *CSS*: Para el diseño y estilo.
  - *JavaScript: Para la interacción del usuario y la generación de hashes usando **CryptoJS*.

- *Backend*:
  - *Python*: Para la lógica en el servidor.
  - *Flask*: Framework para manejar las solicitudes y responder con los datos.

- *Base de datos*:
  - *MongoDB*: Para almacenar los hashes generados. // esta mal estamos usando formato csv

## Funciones principales

- *Generación de Hashes: Los usuarios pueden generar hashes a partir de texto o archivos usando algoritmos como **MD5, **SHA-1* y *SHA-256*.
- *Explicaciones*: La aplicación muestra cómo se genera cada hash y en qué situaciones se usan.
- *Almacenamiento*: Los hashes generados se pueden almacenar para ser consultados más tarde.
- *Interactividad*: La interfaz es fácil de usar y permite realizar las acciones de manera sencilla.

## Instalación

### Requisitos

- *Python *  
- *MongoDB*  // esta mal, se esta ocupando archivos csv
- *Node.js* (si deseas modificar el frontend o instalar dependencias de JavaScript)