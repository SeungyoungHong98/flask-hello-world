from flask import Flask
app = Flask(__name__)

@app.route('/hi',methods=['POST'])
def hi():
    return "Hi!"

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
