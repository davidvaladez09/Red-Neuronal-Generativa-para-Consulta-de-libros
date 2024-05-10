from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, ConversationalRetrievalChain, ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.schema import messages_from_dict, messages_to_dict
from langchain.memory.chat_message_histories.in_memory import ChatMessageHistory
from langchain.agents import Tool
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA
from langchain.chains import RetrievalQA
from nltk.translate.bleu_score import sentence_bleu
from nltk.tokenize import word_tokenize
from langchain.chains import RetrievalQA
from ipywidgets import widgets, Layout, VBox
from IPython.display import display
import time
import threading


cache_dir = "/content/"

import pandas as pd
pd.set_option('display.max_column', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_seq_items', None)
pd.set_option('display.max_colwidth', 500)
pd.set_option('expand_frame_repr', True)
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
import tempfile
from langchain.chains import RetrievalQA

from langchain.document_loaders import GutenbergLoader

loader = GutenbergLoader(
    "https://www.gutenberg.org/cache/epub/1268/pg1268.txt"
)

document = loader.load()

extrait = ' '.join(document[0].page_content.split()[:100])
display(extrait + " .......")

# Chunk sizes of 1024 and an overlap of 256 (this will take approx. 10mins with this model to build our vector database index)
text_splitter = CharacterTextSplitter(
    chunk_size=1024,
    chunk_overlap=256
)
texts = text_splitter.split_documents(document)

model_name = "sentence-transformers/all-MiniLM-L6-v2"

embeddings = HuggingFaceEmbeddings(
    model_name=model_name,
    cache_folder=cache_dir
)  # Use a pre-cached model

vectordb = Chroma.from_documents(
    texts,
    embeddings,
    persist_directory=cache_dir
)

# We want to make this a retriever, so we need to convert our index.
# This will create a wrapper around the functionality of our vector database
# so we can search for similar documents/chunks in the vectorstore and retrieve the results:
retriever = vectordb.as_retriever()

# This chain will be used to do QA on the document. We will need
# 1 - A LLM to do the language interpretation
# 2 - A vector database that can perform document retrieval
# 3 - Specification on how to deal with this data

hf_llm = HuggingFacePipeline.from_model_id(
    model_id="google/flan-t5-large",
    task="text2text-generation",
    model_kwargs={
#        "temperature": 0,
        "do_sample":True,
        "max_length": 2048,
        "cache_dir": cache_dir,
    },
)

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

# Función para actualizar el contador en tiempo real
def actualizar_contador():
    while True:
        if not input_text.disabled:
            tiempo_transcurrido = time.time() - tiempo_inicio
            tiempo_texto.value = f'Tiempo transcurrido: {round(tiempo_transcurrido, 2)} segundos'
        time.sleep(0.1)  # Actualizar cada 0.1 segundos

# Crear widgets de entrada y salida
input_text = widgets.Text(placeholder='Pregunta algo a AnswerBook...', layout=Layout(width='98%'))
output_text = widgets.Textarea(layout=Layout(width='98%', height='200px'), disabled=True)
tiempo_texto = widgets.Text(value='Tiempo transcurrido: 0 segundos', layout=Layout(width='98%'))

# Crear botón para enviar la pregunta
submit_button = widgets.Button(description='Preguntar', button_style='success', layout=Layout(width='20%'))
submit_button.on_click(ejecutar_consulta)

# Estilo de salida para que se vea más como un chat
output_text.style.description_width = 'initial'
output_text.style.font_weight = 'bold'
output_text.style.font_family = 'Arial, sans-serif'
output_text.style.color = 'black'

# Colocar widgets en una caja vertical
chat_box = VBox([output_text, HBox([input_text, submit_button], layout=Layout(width='98%')), tiempo_texto])

# Crear la ventana con título
accordion = widgets.Accordion(children=[chat_box], layout=Layout(width='35%'))
accordion.set_title(0, 'AnswerBook Chat')  # Establecer el título de la ventana

# Mostrar la ventana con título
display(accordion)

# Iniciar el contador de tiempo
tiempo_inicio = time.time()

# Iniciar el hilo para actualizar el contador en tiempo real
thread_contador = threading.Thread(target=actualizar_contador)
thread_contador.start()