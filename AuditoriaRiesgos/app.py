import os
import re
from openai import OpenAI
from flask import Flask, send_from_directory, request, jsonify, Response


app = Flask(__name__)

# Ruta para servir el index.html desde la carpeta dist
@app.route('/',  methods=["GET",'POST'])
def serve_index():
    return send_from_directory('dist', 'index.html')

# Ruta para servir los archivos estáticos generados
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('dist', path)

OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "http://localhost:11434/v1")
OPENAI_API_KEY  = os.getenv("OPENAI_API_KEY", "ollama")
MODEL_NAME      = os.getenv("MODEL_NAME", "ramiro:instruct")

client = OpenAI(base_url=OPENAI_BASE_URL, api_key=OPENAI_API_KEY)

@app.route('/analizar-riesgos', methods=['POST'])
def analizar_riesgos():
    data = request.get_json()  # Obtener datos JSON enviados al endpoint
    activo = data.get('activo')  # Extraer el valor del activo
    if not activo:
        return jsonify({"error": "El campo 'activo' es necesario"}), 400
    
    riesgos, impactos = obtener_riesgos(activo)  # Llamar a la función para obtener riesgos e impactos
    return jsonify({"activo": activo, "riesgos": riesgos, "impactos": impactos})

@app.route('/sugerir-tratamiento', methods=['POST'])
def sugerir_tratamiento():
    data = request.get_json()  # Obtener datos JSON enviados al endpoint
    activo = data.get('activo')  # Extraer el valor del activo
    riesgo = data.get('riesgo')  # Extraer el valor del riesgo
    impacto = data.get('impacto')  # Extraer el valor del impacto

    # Verificar que todos los campos necesarios están presentes
    if not activo or not riesgo or not impacto:
        return jsonify({"error": "Los campos 'activo', 'riesgo' e 'impacto' son necesarios"}), 400

    # Combinar riesgo e impacto para formar la entrada completa para obtener_tratamiento
    entrada_tratamiento = f"{activo};{riesgo};{impacto}"
    tratamiento = obtener_tratamiento(entrada_tratamiento)
    
    return jsonify({"activo": activo, "riesgo": riesgo, "impacto": impacto, "tratamiento": tratamiento})


def obtener_tratamiento(riesgo):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role":"system","content":"Responde en español..."},
                {"role":"user","content":riesgo}
            ]
        )
        answer = response.choices[0].message.content
        if not answer:
            raise ValueError("Respuesta vacía del modelo")
        return answer
    except Exception as e:
        # fallback simple si no hay modelo local
        # Elaborar un tratamiento corto basado en texto
        fallback = "Implementar control de acceso, cifrado y backup periódico; revisar logs y aplicar parcheo."
        return fallback

def obtener_riesgos(activo):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role":"system","content":"Responde en español... pide 5 riesgos en bullets"},
                {"role":"user","content":activo}
            ]
        )
        answer = response.choices[0].message.content
        # intenta parsear bullets con regex original; si falla, fallback:
        patron = r'\*\*\s*(.+?)\*\*:\s*(.+?)\.(?=\s*\n|\s*$)'
        resultados = re.findall(patron, answer)
        if resultados:
            riesgos = [r[0] for r in resultados]
            impactos = [r[1] for r in resultados]
        else:
            # fallback: lista simple
            riesgos = [
                "Acceso no autorizado",
                "Pérdida de datos",
                "Vulnerabilidades de software",
                "Conexiones inseguras",
                "Fallo de hardware"
            ]
            impactos = [
                "Revelación de datos",
                "Pérdida de información crítica",
                "Exposición a exploits",
                "Intercepción de datos",
                "Inoperatividad del servicio"
            ]
        return riesgos, impactos
    except Exception as e:
        # fallback genérico
        riesgos = ["Acceso no autorizado", "Pérdida de datos", "Vulnerabilidades", "Conexión insegura", "Fallos hardware"]
        impactos = ["Divulgación de datos", "Pérdida de servicio", "Compromiso", "Intercepción", "Inoperatividad"]
        return riesgos, impactos
    
    answer = response.choices[0].message.content
    patron = r'\*\*\s*(.+?)\*\*:\s*(.+?)\.(?=\s*\n|\s*$)'
    
    # Buscamos todos los patrones en la respuesta
    resultados = re.findall(patron, answer)
    
    # Separamos los resultados en dos listas: riesgos e impactos
    riesgos = [resultado[0] for resultado in resultados]
    impactos = [resultado[1] for resultado in resultados]
    
    return riesgos, impactos

#riesgos, impactos = obtener_riesgos("mi telefono movil")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5500")