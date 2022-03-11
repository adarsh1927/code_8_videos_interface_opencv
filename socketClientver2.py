import socket
#ip = "10.15.21.205"
ip = "127.0.0.1"
port = 3535
def getfromserver():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip,port))
        print("connected successfully")
        sock.sendall(b'hello world')
        data = sock.recv(1024).decode('utf-8')
        print (type(data))
        return data

#sclicing 
def crane31():
    data = getfromserver()
    #slicing
    id = data[14:16]
    qual = data[16:19]
    lt = data[19:22]
    ct = data[22:25]
    print("crane 31 data ", id, qual, lt, ct)
    return ct,lt   
    

def crane32():
    data = getfromserver()
    #slicing
    id = data[25:27]
    qual = data[27:30]
    lt = data[30:33]
    ct = data[33:36]
    print("crane 32 data ", id, qual, lt, ct)
    return ct,lt   


def crane33():
    data = getfromserver()
    #slicing
    id = data[36:38]
    qual = data[38:41]
    lt = data[41:44]
    ct = data[44:47]
    print("crane 33 data ", id, qual, lt, ct)
    return ct,lt   


def crane34():
    data = getfromserver()
    #slicing
    id = data[47:49]
    qual = data[49:52]
    lt = data[52:55]
    ct = data[55:58]
    print("crane 34 data ", id, qual, lt, ct)
    return ct,lt   


def crane11():
    data = getfromserver()
    #slicing
    id = data[58:60]
    qual = data[60:63]
    lt = data[63:66]
    ct = data[66:69]
    print("crane 11 data ", id, qual, lt, ct)
    return ct,lt   


def crane12():
    data = getfromserver()
    #slicing
    id = data[69:71]
    qual = data[71:74]
    lt = data[74:77]
    ct = data[77:80]
    print("crane 12 data ", id, qual, lt, ct)
    return ct,lt   


def crane14():
    data = getfromserver()
    #slicing
    id = data[80:82]
    qual = data[82:85]
    lt = data[85:88]
    ct = data[88:91]
    print("crane 14 data ", id, qual, lt, ct)
    return ct,lt   


def crane15():
    data = getfromserver()
    #slicing
    id = data[91:93]
    qual = data[93:96]
    lt = data[96:99]
    ct = data[99:102]
    print("crane 15 data ", id, qual, lt, ct)
    return ct,lt   



if __name__ == '__main__':
    crane31()
    crane32()
    crane33()
    crane34()
    crane11()
    crane12()   
    crane14()
    crane15()