from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/home',methods = ['POST', 'GET'])
def hello_world():
    return [{"name":"Daniel"},{"name":"Noga"}]



if __name__ == "__main__":
    app.run(debug=True)