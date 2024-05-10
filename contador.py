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

