from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Multiplication endpoint
@app.route('/multiply', methods=['POST'])
def multiply():
    try:
        # Get data from the request
        data = request.get_json()
        
        # Extract and convert string inputs to integers
        num1 = int(data.get('num1'))
        num2 = int(data.get('num2'))
        num3 = int(data.get('num3'))

        # Perform multiplication
        result = num1 * num2 * num3

        # Return the result as a JSON response
        return jsonify({"result": result})
    
    except ValueError:
        return jsonify({"error": "Invalid input. Please provide integers."}), 400

# Division endpoint
@app.route('/divide', methods=['POST'])
def divide():
    try:
        # Get data from the request
        data = request.get_json()

        # Extract and convert string inputs to integers
        num1 = int(data.get('num1'))
        num2 = int(data.get('num2'))
        num3 = int(data.get('num3'))

        # Perform division
        if num2 == 0 or num3 == 0:
            return jsonify({"error": "Division by zero is not allowed."}), 400
        
        result = num1 / num2 / num3

        # Return the result as a JSON response
        return jsonify({"result": result})
    
    except ValueError:
        return jsonify({"error": "Invalid input. Please provide integers."}), 400

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
