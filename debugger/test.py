import time
from . import debug
from flask import Flask, request, jsonify


app = Flask(__name__)
users_seen = {}
@app.route('/whyline')
def hello():
    d = debug("test1")
    output = d.run()
    out = ""
    for i in output:
        out = out+str(i[1])+"\n"
    return(out)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)