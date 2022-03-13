from cryptography.fernet import Fernet
key = Fernet.generate_key()
fernet = Fernet(key)


def ncrypt(*args):
    temp = []
    for n in args:
        temp.append(n)
    size = len(temp)

    newtemp = []
    if size > 1:

            temp1 = fernet.encrypt(temp[0].encode())
            newtemp.append(temp1)

            temp2 = fernet.encrypt(temp[1].encode())
            newtemp.append(temp2)

            """
            Just there for just in case there is a problem returning a whole list
            a = newtemp[0]
            b = newtemp[1]
            """
            return newtemp

    else:
        temp3 = fernet.encrypt(temp[0].encode())
        return temp3


def dcrypt(encMessage):
    decMessage = fernet.decrypt(encMessage).decode()
    return decMessage
