from flask import Flask, request
import base64

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    args = request.args
    with open("index.html") as f:
        html = f.read()
    sheet = base64.b64decode(args["abc"].encode("ascii")).decode("utf-8")
    html = html.replace("ABCDEF", sheet)
    return html
