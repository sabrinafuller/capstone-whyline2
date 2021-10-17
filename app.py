########  imports  ##########
from flask import Flask, jsonify, request, render_template, url_for, redirect
from debugger import debug
import hashlib

app = Flask(__name__)#############################
import os
s = '(139766743867456, <debugger.FrameStep.FrameStep object at 0x7f1dfb1e7730>), (139766743867456, <debugger.FrameStep.FrameStep object at 0x7f1dfb1e7880>), (35263200, <debugger.FrameStep.FrameStep object at 0x7f1dfb0cadc0>), (35263200, <debugger.FrameStep.FrameStep object at 0x7f1dfb0caee0>), (139766743882880, <debugger.FrameStep.FrameStep object at 0x7f1dfb087910>), (139766743882880, <debugger.FrameStep.FrameStep object at 0x7f1dfb087a60>)'
s1 = '(140712037691456, <debugger.FrameStep.FrameStep object at 0x7ffa1305a730>)<br>(140712037691456, <debugger.FrameStep.FrameStep object at 0x7ffa1305a880>)<br>(18167584, <debugger.FrameStep.FrameStep object at 0x7ffa12f3adc0>)<br>(18167584, <debugger.FrameStep.FrameStep object at 0x7ffa12f3aee0>)<br>(140712037706880, <debugger.FrameStep.FrameStep object at 0x7ffa12ef7910>)<br>(140712037706880, <debugger.FrameStep.FrameStep object at 0x7ffa12ef7a60>)<br>'
def get_file():
    file_upload_path = 'file_uploads'
    if len(os.listdir('file_uploads')) != 0:
            return os.listdir(file_upload_path)[0]   
    else:
        return ("Please upload file")


def run_debugger():
    file_name = get_file()
    try:
        debugger = debug.debug(file_name)
        debug_output = debugger.run()
        return debug_output
    except:
        return "Debugging failed"

@app.route("/", methods=['GET', 'POST'])
def get_homepage():
    print("hello world!")
    return render_template("main.html")


@app.route('/program_upload_response', methods=['POST'])
def upload_static_file():
    f = request.files['static_file']
    f.save("file_uploads/"+f.filename) 
    file_key = get_digest("file_uploads/"+f.filename)

    resp = {"success": True, "response": "file saved!", "file_name": f.filename, 'file_key': file_key}
    return jsonify(resp), 200


@app.route('/get_analysis', methods=['GET', "POST"])
def debug_response():
    if request.method == 'POST':
        result = run_debugger()
        with open('file.txt', 'w') as file:
            file.write(str(result))
        
        #jsonify({"success": True, "response": "Ready to view"}), 200
        
        return jsonify({"success": True, "response": "Ready to view"}), 200
    else:

        return jsonify({"success": False, "response": "Invalid request"}), 200

@app.route("/start_debug", methods=['GET', 'POST'])
def start_debug():
    with open("file.txt","r") as file:
        content = file.readlines()
    
    
    return render_template('analysis.html', result =  content)

@app.route('/whyline', methods=['GET'])
def get_whyline():
    # '<h1>These are my thoughts on </h1> <a href=blog/2020/dogs>dogs</a></h1>'
    return render_template('analysis.html' , input = run_debugger() )

@app.route('/code', methods = ['GET'])
def get_code():
    return render_template('code.html')




### below for set ups

@app.route('/getdata/<index_no>', methods=['GET','POST'])
def data_get(index_no):
    data = list(range(1,300,3))

    
    if request.method == 'POST': # POST request
        print(request.get_text())  # parse as text
        return 'OK', 200
    
    else: # GET request
        return 't_in = %s ; result: %s ;'%(index_no, data[int(index_no)])


@app.route('/test', methods=['GET', 'POST'])
def testfn():    # GET request
    if request.method == 'GET':
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200

def get_digest(file_path):
    h = hashlib.sha256()

    with open(file_path, 'rb') as file:
        while True:
            # Reading is buffered, so we can read smaller chunks.
            chunk = file.read(h.block_size)
            if not chunk:
                break
            h.update(chunk)

    return h.hexdigest()


app.run(debug=True)