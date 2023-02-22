## Test Flask
from flask import Flask, request, render_template, make_response 
import json
#import pandas as pd

app = Flask(__name__)

@app.route("/")  
def helloworld():
    return "Hello, World!"

@app.route("/name")  
def hellotohn():
    return "Hello, Tohn!"

##api get
#@app.route('/request',methods=['POST']) ##POST==Protocol ในการส่ง message 
@app.route('/getrequest',methods=['GET'])  ## วิธีเรียกใช้ ---> http://127.0.0.1:5000//getrequest?msg1=123
def get_request_detail():

    getmsg = request.args.get('msg1')
    print(getmsg)
    return "received"

##api post
@app.route('/postrequest',methods=['POST'])
def post_request_detail():

    payload = request.data.decode("utf-8") ##รับมาเก็บไว้ใน payload #Type == Json  
   #print(payload)
    inmessage = json.loads(payload) 

    print(inmessage)
    
    json_data = json.dumps({'y': 'received!'})
    return json_data

##webapp 
@app.route("/home")
def home():
    #print('we are in home2')
    # getting input with name = fname in HTML form
    #name = request.form['fav_language']
    #print(name)
    #return render_template("home.html",name = f"{first_name} {last_name}")

    return render_template("home.html", name='AI')
    

if __name__ == "__main__":
    app.run()#host='0.0.0.0',port=5001
    #app.run(host='0.0.0.0',debug=True, port=5007) 
