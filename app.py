from flask import Flask, render_template, request, jsonify, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = "clave_secreta_para_guardar_datos"

# --- RESPUESTAS PERSONALIZADAS ---
respuestas = {
    "tamaños": "Tenemos frascos de 30ml, 50ml y 100ml según tu preferencia.",
    "precios": "Por 20 mil llevas 30ml, por 40 mil llevas 50ml y por 75 mil llevas 100ml. A mayor tamaño, más economía.",
    "métodos de pago": " el numero para pagos es 3138094678, nequi,daviplata .",
    "pureza": "Nuestras fragancias tienen una pureza del 90% en esencias originales.",
    "envases": "Usamos envases de vidrio importado con atomizador resistente.",
    "marcas y referencias": "Tenemos más de 300 referencias de las mejores marcas internacionales.",
    "recomendadas": "Las más pedidas son: Good Girl, Invictus, Sauvage y La Vie Est Belle.",
    "ofertas": "¡Por registrar tus datos obtienes 10% de descuento en tu próxima compra! 🌸",
    "link de la tienda": "Puedes visitar nuestra tienda en línea en: https://jhondainerarias.github.io/A/"
}


# --- LÓGICA DEL CHATBOT ---
def obtener_respuesta(mensaje):
    mensaje = mensaje.lower()
    nombre = session.get("nombre")

    # SALUDO INICIAL
    if "hola" in mensaje or "buenas" in mensaje or "hey" in mensaje:
        if not nombre:
            session["esperando_nombre"] = True
            return "¡Hola! 😊 Soy tu asistente virtual de Mis Fragancias Jhon Arias. ¿Cuál es tu nombre?"
        else:
            return f"¡Hola de nuevo, {nombre}! 🌸 ¿Deseas conocer nuestras ofertas o fragancias recomendadas?"

    # CAPTURAR NOMBRE
    if session.get("esperando_nombre"):
        session["nombre"] = mensaje.capitalize()
        session.pop("esperando_nombre", None)
        return f"¡Encantado de conocerte, {session['nombre']}! 💐 ¿Quieres conocer nuestras ofertas, precios o tamaños disponibles?"

    # RESPUESTAS PROGRAMADAS
    for clave, valor in respuestas.items():
        if clave in mensaje:
            return f"{valor} {f'{nombre},' if nombre else ''} ¿puedo ayudarte con  algo más?"

    # HORA
    if "hora" in mensaje:
        return f"La hora actual es {datetime.now().strftime('%H:%M:%S')} ⏰."

    # DESPEDIDA
    if "gracias" in mensaje or "adios" in mensaje or "chao" in mensaje:
        return f"¡Fue un placer atenderte, {nombre if nombre else 'amigo'}! 🌹 Vuelve pronto a Mis Fragancias Jhon Arias."

    # RESPUESTA GENERAL
    return f"No tengo información exacta sobre eso 🤔, {nombre if nombre else 'amigo'}. Pero puedo ayudarte con tamaños, pureza, precios u ofertas actuales."


# --- RUTA PRINCIPAL ---
@app.route('/')
def index():
    session.clear()
    return render_template('index.html')


# --- API DEL CHAT ---
@app.route('/enviar', methods=['POST'])
def enviar():
    data = request.get_json()
    mensaje_usuario = data.get("mensaje", "")
    respuesta = obtener_respuesta(mensaje_usuario)
    return jsonify({"respuesta": respuesta})


if __name__ == '__main__':
    app.run(debug=True)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    app.run(debug=True)