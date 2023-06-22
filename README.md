# Llaves

Este repo contiene las pistas y la información relevante que hemos ido recolectando para encontrar los 3 temas que Jaloner encriptó dentro de su tema [llaves](https://www.youtube.com/watch?v=AJAC-WRFcns).

A día de hoy 2 de los 3 temas encriptados ya se han averiguado:

- [llave 1](https://www.youtube.com/watch?v=EN0-iGtKD7I): El hash del vídeo de YT estaba en la portada de *Llaves*.

  **Descripción**: No tiene

- [llave 2](https://www.youtube.com/watch?v=sBRUuJZIO9Y): El link del vídeo de YT estaba en un
fotograma del vídeo de la llave 1.

  **Descripción**: La última llave se podrá conseguir a través del siguiente canal de telegram [](https://t.me/+bsIzOWziGRA5MWFk) a las 13:47h (hora española) el día 1 de junio de 2023.


En el canal de telegram que aparece en la descripción del segundo vídeo aparecieron las 3
imágenes del poema *El pez* de Chantal Maillard (las imágenes están en la carpeta `images/` y la letra del poema en `Chantal_Maillard_EL_PEZ.txt`) y el código que se encuentra en ``llave3_codigo_telegram.txt``.

Hasta ahora la hipótesis más razonable es que el código de Telegram es el resultado de encriptar AES el link (o el hash) del vídeo de YT de la 3ra llave. La clave de desencriptación debe ser de 16, 24 ó 32 caracteres y guardar relación con el resto de piezas del puzzle (sino, vaya gracia).

Adicionalmente podría ser necesaria la semilla de inicialización del algoritmo, que no tiene limitación de caracteres pero cuya longitud suele ser similar a la de la clave.


## Ideas / Divagaciones

Aparte de las letras de los temas, hemos:

- Revisado las imágenes en busca de algún efecto. La primera de ellas parece estar manipulada (ocupa distinto a las otras 2 y en número de página está editado). Pero no se ha encontrado nada relevante.

- El poema que se transparenta en la tercera foto es *Sin* del mismo libro *Hilos* al que pertenece *El pez* (la letra está en `Chantal_Maillard_SIN.txt`).

- Pensamos que en la frase de la llave 1: "el secreto y la clave están en la dosis
pero lo que lleva la dosis es una clave secreta" la dosis es ASCII. Vendría a decir que ambas (el mensaje y la clave) están en ASCII y que para desencriptar el código se requiere una clave.

- El propio Jaloner publicó en Twitter el 21 de junio de 2023 a las 10:01:

  ```
  ¿Corté el hilo
  o simplemente lo solté?
  ¡Se sueltan tantas cosas!
  Y ¡hace tanto tiempo! El aire
  se entumeció. ¿O fue la mano?
  Quedó en suspenso, creo, suspendida.
  No sé si lo recuerdo.  ¡Inventamos
  tantas cosas!

  Chantal Maillard (Hilos)
  ```

- Se pensó que 13:47 podía ser una referencia a un pasaje bíblico, se encontró:

  > Mateo 13:47
  >
  > Asimismo el reino de los cielos es semejante a una red, que echada en el mar,
  > recoge de toda clase de peces;

  Y ya de paso:

  > Mateo 13:55
  >
  > ¿No es este el hijo del carpintero? ¿No se llama su madre María, y sus
  > hermanos, Jacobo, José, Simón y Judas?
