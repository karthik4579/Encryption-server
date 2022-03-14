from flask import Flask
from flask import request
from encrypt import ncrypt, dcrypt
app = Flask(__name__)


@app.route('/encrypt', methods=["POST"])
def Encrypt():
    value0 = str(request.form['activity'])
    value1 = str(request.form['task'])
    if(value0 == "register"):
        if(value1 == "password"):
            valuer1 = str(request.form['password'])
            a = ncrypt(valuer1)
            return a
        
        elif(value1 == "nfcpassword"):
            valuer2 = str(request.form['nfcpassword'])
            b = ncrypt(valuer2)
            return e
        
    elif(value0 == "nfcreset"):
        valuen1 = str(request.form['newnfcpassword'])
        b = ncrypt(valuen1)
        return b

    elif(value0 == "userpassreset"):
        valueu1 = str(request.form['newuserpassword'])
        c = ncrypt(valueu1)
        return c



@app.route('/dcrypt', methods=["POST"])
#This is for login so this will take password decrypt it and return it
def Decrypt(): 
        valuel1 = str(request.form['password'])
        d = dcrypt(valuel1)
        return d
