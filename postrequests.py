import requests
import json

if __name__ == "__main__":

    #url = 'http://127.0.0.1:5000/postrequest'
    #url = 'http://10.71.160.33:5001/postrequest'
    url = 'http://172.24.136.144:5007/postrequest'
    #url = 'http://172.25.224.252:5001/postrequest'
    
    #myobj = {'message_key': 'message_val'}  ## Dump ไปที่ http://127.0.0.1:5000/postrequest ให้ testflask.py รับตัวแปรชื่อ myobj ไว้ 
    myobj = {'message': 'Hello !! How are you today'}
    #myobj = 'Kannika Wiratchawa'

    x = requests.post(url, data = json.dumps(myobj))

    print(x.text)
