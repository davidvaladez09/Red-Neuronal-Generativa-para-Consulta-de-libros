# Cristian
from langchain.chains import RetrievalQA

# Suponiendo que tienes las variables `hf_llm` y `retriever` definidas anteriormente

while True:
    # Crear una instancia de RetrievalQA
    qa = RetrievalQA.from_chain_type(
        llm=hf_llm,
        chain_type="refine",
        retriever=retriever
    )

    # Pedir al usuario la consulta
    query = input("Ingrese su pregunta (o escriba 'salir' para terminar): ")

    # Verificar si el usuario quiere salir del programa
    if query.lower() == "salir":
        print("Saliendo del programa...")
        break

    # Ejecutar la consulta
    query_results_venice = qa.run(query)

    # Imprimir los resultados
    print("#" * 12)
    print(query_results_venice)