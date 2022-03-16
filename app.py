from flask import Flask
from flask import request
from encrypt import ncrypt, dcrypt
app = Flask(__name__)


@app.route('/encrypt', methods=["POST"])
def Encrypt():
    value0 = str(request.form['activity'])
    value1 = str(request.form['task'])
    if(value0 == "register"):
        valuer1 = str(request.form['password'])
        valuer2 = str(request.form['nfcpassword'])
        a = str(ncrypt(valuer1))
        e = str(ncrypt(valuer2))
        f = f"{a}, {e}"
        return f
        
    elif(value0 == "nfcreset"):
        valuen1 = str(request.form['newnfcpassword'])
        b = str(ncrypt(valuen1))
        return b

    elif(value0 == "userpassreset"):
        valueu1 = str(request.form['newuserpassword'])
        c = str(ncrypt(valueu1))
        return c



@app.route('/dcrypt', methods=["POST"])
#This is for login so this will take password decrypt it and return it
def Decrypt(): 
        valuel1 = str(request.form['password'])
        d = str(dcrypt(valuel1))
        return d
