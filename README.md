# Red-Neuronal-Generativa-para-Consulta-de-libros
Proyecto para la materia de Análisis de algoritmos en Centro Universitario de Ciencias Exactas e Ingenierías CUCEI. 

Integrantes:
-David Valadez Gutierrez
-Mariana Ruíz González
-Cristian Chávez Velasco


El proyecto se centra en implementar un chatbot que sea capaz de comprender
el lenguaje natural, extraer información relevante y generar respuestas
contextualmente adecuadas a partir de libros. Este chatbot busca abordar el
problema de la interacción natural entre humanos y sistemas de inteligencia
artificial, permitiendo a los usuarios realizar consultas, obtener información y
mantener conversaciones fluidas sobre una variedad de temas relacionados
con los libros con los que ha sido entrenado. Todo esto con la finalidad de que
los usuarios puedan consultar información específica en libros.
Herramientas a utilizar:
Large Language Models (LLM): son modelos de lenguaje estadísticos o
basados en aprendizaje automático que están diseñados para manejar
grandes cantidades de datos de texto y generar contenido coherente y
relevante.
Inretrieval augmented generation (RAG): una técnica para mejorar la
generación de texto mediante la incorporación de información externa, como
bases de conocimiento o documentos relacionados.
LangChain: sistema o arquitectura para procesar y comprender múltiples
idiomas
Albert small 2: modelo de transformers pre entrenado en un gran corpus de
datos en inglés de forma autosupervisada. Esto significa que fue entrenado
previamente sólo con los textos sin procesar, sin que ningún ser humano los
etiquete de ninguna manera (razón por la cual puede usar una gran cantidad
de datos disponibles públicamente) con un proceso automático para generar
entradas y etiquetas a partir de esos textos.
Transformer: tipo de arquitectura de red neuronal desarrollada inicialmente
para tareas de procesamiento de lenguaje natural (NLP). Se basa en un
mecanismo de atención que permite a la red aprender relaciones entre
diferentes partes de la secuencia de entrada sin depender de la distancia entre
ellas.
- Nombre del proyecto, finalidad, metas y objetivos del proyecto.
(aquí se incluye lo que sería la justificación del proyecto)
Nombre del Proyecto: AnswerBook

Finalidad del Proyecto: Desarrollar un chatbot con la capacidad de
comprensión del lenguaje natural, extracción de información relevante y
generación de respuestas contextualmente adecuadas basadas en libros. Se
busca facilitar la interacción entre humanos y un sistema de inteligencia
artificial, especialmente en el contexto de la exploración y comprensión de
contenido literario.
Metas del Proyecto:
- Implementar un sistema de procesamiento del lenguaje natural (NLP)
que permita al chatbot comprender las consultas de los usuarios de
manera efectiva.
- Hacer uso de una red neuronal generativa para mostrar al usuario las
respuestas a las preguntas.
- Implementar un modelo preentrenado para facilitar el desarrollo del
proyecto.
- Entrenar el modelo del chatbot con al menos un libro para mostrar el
funcionamiento del proyecto.
Objetivos del Proyecto:
- Facilitar la exploración y comprensión de libros mediante una interfaz de
usuario conversacional y amigable.
- Fomentar la lectura y el aprendizaje continuo al proporcionar
recomendaciones personalizadas y respuestas contextualmente
relevantes.
- Aprender sobre la implementación de una pequeña parte inteligencia
artificial en el ámbito de la comprensión del lenguaje natural y la
generación de respuestas coherentes y útiles.

- Las partes y sus funciones.
1. Procesamiento del Lenguaje Natural (NLP): Esta parte se encarga de
entender el lenguaje humano y procesar las consultas de los usuarios
para extraer su significado. Incluye tareas como tokenización, análisis
gramatical, reconocimiento de entidades y desambiguación de sentido.
2. Modelo de Generación de Respuestas: Basado en el contenido de los
libros previamente entrenados, este modelo genera respuestas
contextualmente adecuadas a partir de la información extraída. Puede
incluir técnicas de generación de lenguaje natural como modelos de
lenguaje autorregresivos o transformers.
3. Interfaz de Usuario (GUI): Interfaz a través de la cual los usuarios
interactúan con el chatbot. Permite enviar consultas, recibir respuestas
y realizar acciones dentro del sistema.
4. Base de Datos de Libros: O ente caso un sitio
web(https://gutenberg.org/) que contiene una colección de libros

clásicos en texto plano, que sirven como fuente de información para el
chatbot.
