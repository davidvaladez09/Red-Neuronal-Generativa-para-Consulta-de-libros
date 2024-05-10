# Todos
from langchain.chains import RetrievalQA
from ipywidgets import widgets, Layout, VBox, HBox
from IPython.display import display
import time
import threading

# Función para manejar la consulta del usuario y ejecutarla
def ejecutar_consulta(b):
    query = input_text.value
    if query.lower() == "!salir" or query.lower() == "!SALIR" or query.lower() == "!Salir":
        output_text.value += "\nANSWERBOOK Dice ADIOS..."
    else:
        input_text.disabled = True  # Desactivar el widget de entrada mientras se procesa la consulta
        output_text.value += "\n\nANSWERBOOK: Generando respuesta más adecuada..."
        start_time = time.time() # Iniciar contador de tiempo
        qa = RetrievalQA.from_chain_type(llm=hf_llm, chain_type="refine", retriever=retriever)
        query_results = qa.run(query)
        end_time = time.time() # Finalizar contador de tiempo
        tiempo_respuesta = round(end_time - start_time, 2) # Calcular tiempo de respuesta
        output_text.value += "\n\nYOU: " + f"{query} \n" + "\nANSWERBOOK: " + str(query_results) + f"\n\nANSWERBOOK: ¿Quieres saber algo más? Realiza otra pregunta...\n"
        input_text.disabled = False  # Reactivar el widget de entrada después de recibir la respuesta
        # Limpiar el widget de pregunta después de mostrar la respuesta
        input_text.value = ""

