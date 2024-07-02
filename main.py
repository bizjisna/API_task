from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/multiply', methods=['POST'])
def multiply():
    try:
        data = request.get_json()
        num1 = int(data.get('num1'))
        num2 = int(data.get('num2'))
        num3 = int(data.get('num3'))
        result = num1 * num2 * num3
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Invalid input. Please provide integers."}), 400

@app.route('/divide', methods=['POST'])
def divide():
    try:
        data = request.get_json()
        num1 = int(data.get('num1'))
        num2 = int(data.get('num2'))
        num3 = int(data.get('num3'))
        if num2 == 0 or num3 == 0:
            return jsonify({"error": "Division by zero is not allowed."}), 400
        result = num1 / num2 / num3
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Invalid input. Please provide integers."}), 400

if __name__ == '__main__':
    app.run(debug=True)
