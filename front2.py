# Crear botón para enviar la pregunta
submit_button = widgets.Button(description='>', button_style='success', layout=Layout(width='20%'))
submit_button.on_click(ejecutar_consulta)

# Estilo de salida para que se vea más como un chat
output_text.style.description_width = 'initial'
output_text.style.font_weight = 'bold'
output_text.style.font_family = 'Arial, sans-serif'
output_text.style.color = 'black'

# Colocar widgets en una caja vertical
chat_box = VBox([output_text, HBox([input_text, submit_button], layout=Layout(width='98%')), tiempo_texto])

# Crear la ventana con título centrado
accordion = widgets.Accordion(children=[chat_box], layout=Layout(width='35%', align_items='center'))
accordion.set_title(0, 'AnswerBook Chat')  # Establecer el título de la ventana

# Mostrar la ventana con título
display(accordion)

# Iniciar el contador de tiempo
tiempo_inicio = time.time()

# Iniciar el hilo para actualizar el contador en tiempo real
thread_contador = threading.Thread(target=actualizar_contador)
thread_contador.start()
