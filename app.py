########  imports  ##########
from flask import Flask, jsonify, request, render_template, url_for, redirect
from debugger import debug
import hashlib

app = Flask(__name__)#############################
import os

## Get file grabs the most recent file from the folder
## gets the file path, checks to see if the folder is empty
def get_file():
    file_upload_path = 'file_uploads'
    if len(os.listdir('file_uploads')) != 0:
            return os.listdir(file_upload_path)[0]   
    else:
        return ("Please upload file")

#  Creates the debugger object and returns the program frames
# 
def run_debugger():
    file_name = get_file()
    try:
        debugger = debug.debug(file_name)
        debug_output = debugger.run()
        return debug_output
    except:
        return "Debugging failed None"
# main route of the app returns the index.html 
@app.route("/", methods=['GET', 'POST'])
def get_homepage():
    print("hello world!")
    return render_template("main.html")

# Uploads the file to the server
@app.route('/program_upload_response', methods=['POST'])
def upload_static_file():
    f = request.files['static_file']
    f.save("file_uploads/"+f.filename) 
    file_key = get_digest("file_uploads/"+f.filename)

    resp = {"success": True, "response": "file saved!", "file_name": f.filename, 'file_key': file_key}
    return jsonify(resp), 200

# calls the run_debugger() method
@app.route('/get_analysis', methods=['GET', "POST"])
def debug_response():
    if request.method == 'POST':
        result = run_debugger()
        with open('file.txt', 'w') as file:
            file.write(str(result))
        return jsonify({"success": True, "response": "Ready to view"}), 200
    else:
        return jsonify({"success": False, "response": "Invalid request"}), 200
# naviate to the debugger page
# reads the output of the debugger file, and renders the html
@app.route("/start_debug", methods=['GET', 'POST'])
def start_debug():
    with open("file.txt","r") as file:
        content = file.readlines()
    return render_template('analysis.html', result =  content)

# Does nothing currently
@app.route('/whyline', methods=['GET'])
def get_whyline():
    return render_template('analysis.html' , input = run_debugger() )
# This call does nothin
@app.route('/code', methods = ['GET'])
def get_code():
    return render_template('code.html')




### IGNORE below for set ups

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


def test_run_debugger():
    frame_steps= run_debugger() 
    frame_delta_adds= []
    frame_delta_subs= []
    frame_delta_updates= []


    for k in frame_steps:
        #print(list(k[1].deltas.items())[0][1].additions)
        frame_delta_adds.append(list(k[1].deltas.items())[0][1].additions)
        frame_delta_subs.append(list(k[1].deltas.items())[0][1].deletions)
        frame_delta_updates.append(list(k[1].deltas.items())[0][1].updates)

    for i in range(len(frame_delta_adds)):
        print("adds")
        print(frame_delta_adds[i])
        print("del")
        print(frame_delta_subs[i])
        print("updates")
        print(frame_delta_updates[i])



    


