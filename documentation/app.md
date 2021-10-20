







`app.py`
Contains the flask server set up 

`app.route("/")` 
Returns the    `main.html` main page


`@app.route('/program_upload_response` 
Call to upload the file from the user

`@app.route('/get_analysis'` 
Navigate to `analysis.html` with is the main debugger page

`@app.route("/start_debug"` 
Reads the output of the debgger output and displays to `analysis.html` 

`get_file()` 
Get the most recent file uploaded on the server 

`run_dugger()` 
Creates the debugger object and returns the program frames 

`get_digest()` 
Todo: creates a hash of file, and serves analysis for that file 






