from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta principal
@app.route('/')
def home():
    return "Economía Familiar - Daily Input 🚀"

# Ruta para agregar un gasto (simulado en memoria)
gastos = []

@app.route('/add', methods=['POST'])
def add_gasto():
    data = request.json
    gastos.append(data)
    return jsonify({"message": "Gasto agregado", "gasto": data}), 201

@app.route('/list', methods=['GET'])
def list_gastos():
    return jsonify(gastos)

if __name__ == '__main__':
    app.run(debug=True)

