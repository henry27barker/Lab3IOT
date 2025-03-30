from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    print("Temperature: "+str(request.args.get("temp"))+"\nHumidity: "+str(request.args.get("humid")))
    return "Temperature: "+str(request.args.get("temp"))+"\nHumidity: "+str(request.args.get("humid"))
