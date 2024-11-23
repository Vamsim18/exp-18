from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/nth-odd', methods=['GET'])
def nth_odd():
    try:
        n = int(request.args.get('n'))
        if n < 1:
            raise ValueError
        result = 2 * n - 1
        return jsonify({"nth_odd": result})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input. Provide a positive integer."}), 400

if __name__ == '__main__':
    app.run(debug=True)
