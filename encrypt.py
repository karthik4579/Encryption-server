from typing import NewType
from cryptography.fernet import Fernet
key = Fernet.generate_key()
fernet = Fernet(key)


def ncrypt(*args):
    temp = []
    for n in args:
        temp.append(n)
    ncrypt.size = len(temp)
    
    ncrypt.newtemp = []
    if ncrypt.size > 1:
    
            temp1 = fernet.encrypt(temp[0].encode())
            ncrypt.newtemp.append(temp1)
            
            temp2 = fernet.encrypt(temp[1].encode())
            ncrypt.newtemp.append(temp2)
            
            """
            Just there for just in case there is a problem returning a whole list
            a = ncrypt.newtemp[0]
            b = ncrypt.newtemp[1]
            """ 
            return ncrypt.newtemp
        
    else:
        ncrypt.temp3 = fernet.encrypt(temp[0].encode())
        return ncrypt.temp3
        
      
def dcrypt(encMessage):
    decMessage = fernet.decrypt(encMessage).decode()
    return decMessage






    

    



