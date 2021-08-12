# DSC-Entel-2021

## Descripción del reto
El reto consiste en desarrollar un algoritmo que estime el tiempo y distancia de acuerdo a la ubicación del técnico y de la ubicación de los lugares donde ocurren los problemas o fallas, sin usar herramientas, aplicaciones y/o API de paga, la solución nos permitirá obtener el tiempo y la distancia estimada y con ello asignar el técnico mas cercano al lugar del problema, y además de no generar gastos. Es muy importante no hacer uso de API de paga, ya que en la evaluación final se revisara el código

## Target
Se pide determinar la ruta entre el origen y destino y estimar la distancia y el tiempo que le tomaría al personal en recorrer dicha ruta, el calculo de la distancia y tiempo para la data de entrenamiento(train) se ha estimado con una API de paga, y lo que se desea es aproximar la distancia y el tiempo con técnicas y/o herramientas que NO involucren algún tipo de pago a corto o largo plazo.

## Archivos
- train.csv - Contiene datos de las coordenadas de origen y destino, además de la distancia y el tiempo estimado para avaluar el algoritmo o técnica que estén - desarrollando.
      - ID: identificador del problema
      - FECHA: fecha en que ocurrió el problema
      - LATITUD_ORIGEN: latitud del personal técnico
      - LONGITUD_ORIGEN: longitud del personal técnico
      - LATITUD_DESTINO: latitud donde ocurre el problema
      - LONGITUD_DESTINO: Longitud donde ocurre el problema
      - DISTANCIA: distancia entre ambas coordenadas (metros)
      - TIEMPO: tiempo estimado en recorrer ambas coordenadas (segundos)
- test.csv - Contiene datos para evaluar su solución, se debe calcular la distancia y el tiempo.
      - ID: identificador del problema
      - FECHA: fecha en que ocurrió el problema
      - LATITUD_ORIGEN: latitud del personal técnico
      - LONGITUD_ORIGEN: longitud del personal técnico
      - LATITUD_DESTINO: latitud donde ocurre el problema
      - LONGITUD_DESTINO: Longitud donde ocurre el problema
      
- sampleSubmission.csv - Un archivo de envío de muestra en el formato correcto
