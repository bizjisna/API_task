from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/multiply', methods=['POST'])
def multiply():
    try:
        data = request.get_json()
        numbers = data.get('numbers')
        print(numbers)

        if not numbers or len(numbers) <= 1:
            return jsonify({"error": "Please provide more than one number."}), 400
        
        # Convert all inputs to float
        numbers = [float(num) for num in numbers]

        # Compute the multiplication of all numbers
        result = 1
        for number in numbers:
            result *= number

        return jsonify({"result": round(result,2)})
    except ValueError:
        return jsonify({"error": "Invalid input. Please provide integers."}), 400

@app.route('/divide', methods=['POST'])
def divide():
    try:
        data = request.get_json()
        numbers = data.get('numbers')

        if not numbers or len(numbers) <= 1:
            return jsonify({"error": "Please provide more than one number."}), 400
        
        # Convert all inputs to float
        numbers = [float(num) for num in numbers]

        # Check for division by zero
        if 0 in numbers[1:]:
            return jsonify({"error": "Division by zero is not allowed."}), 400

        # Compute the division sequentially
        result = numbers[0]
        for number in numbers[1:]:
            result /= number

        return jsonify({"result": round(result,2)})
    except ValueError:
        return jsonify({"error": "Invalid input. Please provide integers."}), 400

if __name__ == '__main__':
    app.run(debug=True)
