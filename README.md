# Embebidos-Proyecto2
App Inicializacion se encarga de la inicializacion de la aplicacion de reconocimiento atravez de una conexion SSH y la copia de los datos resultantes del analisis de emociones. La aplicacion se ejecuta en el cmd y toma como entrada dos parametros; el tiempo de ejecucion para el app de reconocimiento y el tiempo de muestreo para el app de reconocimiento.

App Rec es un folder con dos scripts;
1) ConversionTF-Lite: realiza una conversion de una red neuronal ya entrenada con tensorflow para que utilice tensorflow-lite. Para esto se utiliza el model.h5 extraido de la red neuronal de reconocimiento de emociones ya entrenada "DeepFace", se vuelve a armar la red neuronal con los pesos del modelo y se utilizan las funciones de conversion TF-lite para generar el modelo convertido converted_model.tflite.

2) App Reconocimiento: Esta aplicacion toma como entrada dos parametros, el tiempo de ejecucion de la aplicacion y el tiempo de muestreo de la aplicacion y se encarga de utilizar el modelo pre entrenado y convertido a tflite converted_model.tflite, junto al modulo de vision por computador OpenCV para reconocer emociones atravez de una camara web y escribirlas en un archivo de texto Emociones.txt. 

El folder de recetas incluye las recetas generadas para la creacion de la imagen minimal incluyendo las recetas de meta-appreconocimiento, para incluir el appreconocimiento, converted_model y haarscade, y el localconf y bblayers general de la imagen que incluye los modulos a instalar en la imagen y los metas de donde buscar esos modulos. 
