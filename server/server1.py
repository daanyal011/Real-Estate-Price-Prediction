from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/hello') #exposing http endpoint 
def hello():
    return "Hi"

if __name__ == '__main__':
    print("Starting Python Flask Server for Home Price Prediction")
    app.run(host='0.0.0.0', port=8080) 