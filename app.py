from flask import Flask
from flask import request
import encrypt
app = Flask(__name__)


@app.route('/encrypt', methods=["POST"])
def Encrypt():
    value0 = str(request.form['activity'])
    if(value0 == "register"):
        valuer1 = str(request.form['password'])
        valuer2 = str(request.form['nfcpassword'])
        encrypt.ncrypt(valuer1, valuer2)
    elif(value0 == "nfcreset"):
        valuen1 = str(request.form['newnfcpassword'])
        encrypt.ncrypt(valuen1)
    elif(value0 == "userpassreset"):
        valueu1 = str(request.form['newuserpassword'])
        encrypt.ncrypt(valueu1)
        


@app.route('/dcrypt', methods=["POST"])
def Decrypt():
    value0 = str(request.form['device'])
    if(value0 == "app"):     #This is for login so this will take password decrypt it and return it
        valuel1 = str(request.form['password'])
        encrypt.dcrypt(valuel1)
        
    elif (value0 == "raspberrypi"):
        valuel1 = str(request.form['NFCpassword'])
        encrypt.dcrypt(valuel1)
        

if __name__ == '__main__':
    app.run(debug=True)
    
    
    