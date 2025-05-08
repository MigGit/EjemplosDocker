from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/saludo')
def saludo():
    return jsonify({"mensaje": "¡Hola desde el contenedor de la API!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
