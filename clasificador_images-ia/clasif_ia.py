import tensorflow as tf
import tensorflow_datasets as tfds
import math

datos, metadatos=tfds.load('fashion_mnist', as_supervised=True, with_info=True)
datos_entrenamiento, datos_pruebas =datos['train'], datos['test']
nombres_clases=metadatos.features['label'].names


#Normalizar los datos(Pasar de 0-255 a 0-1)
def normalizar(imagenes,etiquetas):
  imagenes=tf.cast(imagenes, tf.float32)
  imagenes /=255 #Aqui pasa lo de 0-255 a 0-1
  return imagenes, etiquetas

# Normalizar los datos  de entrenamiento y pruebas de la función que hicimos
datos_entrenamiento=datos_entrenamiento.map( normalizar)
datos_pruebas=datos_pruebas.map(normalizar)

#Agregar a cache (usar mem#Mostrar una imagen  de los datos de pruebas  , de momento mostremos la primera
for imagen, etiqueta in datos_entrenamiento.take(1):
  break

imagen=imagen.numpy().reshape((28,28)) #Redimensionar , cosas de tensores, lo veremos después

import matplotlib.pyplot as plt 
#Dibujar dibujar
plt.figure()
plt.imshow(imagen, cmap=plt.cm.binary)
plt.colorbar()
plt.grid(False)
plt.show( )


plt.figure(figsize=(10,10))
for i, (imagen, etiqueta) in enumerate(datos_entrenamiento.take(25) ):
  imagen=imagen.numpy().reshape((28,28))
  plt.subplot(5,5,i+1)
  plt.xticks([])
  plt.yticks([])
  plt.grid(False)
  plt.imshow(imagen, cmap=plt.cm.binary)
  plt.xlabel(nombres_clases[etiqueta])
plt.show()

#Crear el modelo
modelo=tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28, 1)), #1- Blanco y Negro
    tf.keras.layers.Dense(50, activation=tf.nn.relu),
    tf.keras.layers.Dense(50, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax) #Para redes de clasificación 
])

#Compilar el modelo
modelo.compile(
    optimizer='adam',
    loss=tf.keras.losses.SparseCategoricalCrossentropy(),
    metrics=['acuraccy']
)

num_ej_entrenamiento=metadatos.splits["train"].num_examples
num_ej_pruebas=metadatos.splits["test"].num_examples

TAMANO_LOTE=32
datos_entrenamiento=datos_entrenamiento.repeat().shuffle(num_ej_entrenamiento).batch(TAMANO_LOTE)
datos_pruebas=datos_pruebas.batch(TAMANO_LOTE)



#Entrenar
historial= modelo.fit(datos_entrenamiento, epochs=5, steps_per_epoch=math.ceil(num_ej_entrenamiento/TAMANO_LOTE))