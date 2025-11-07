from flask import Flask, render_template_string
import os

app = Flask(__name__)

# Definición de la ruta principal
@app.route('/')
def home():
    # Usamos HTML básico para mostrar el mensaje
    html_content = """
    <!doctype html>
    <html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Taller Docker Daniela</title>
    </head>
    <body>
        <h1>=========================================</h1>
        <h1>  TALLER DE CONTENEDORES CON DANIELA</h1>
        <h1>=========================================</h1>
        <p>¡La aplicación Flask se ha ejecutado con éxito DENTRO del contenedor Docker!</p>
        <p>La imagen fue creada por daniela-cardenas.</p>
        <p>Directorio de trabajo actual: {{ cwd }}</p>
    </body>
    </html>
    """
    return render_template_string(html_content, cwd=os.getcwd())

# El código que ejecuta la aplicación
if __name__ == '__main__':
    # Flask se ejecutará en todas las interfaces de red (0.0.0.0) y en el puerto 8080
    app.run(host='0.0.0.0', port=8080)