from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/sum/<int:a>/<int:b>')
def sum(a,b):
    result = {
        "Input Numbers":[a,b],
        "Sum of Numbers": a+b

    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)