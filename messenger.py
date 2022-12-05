#For Hotline button and Faq button
def Hotline():
    rw_op = open("./Hotline.txt","r")
    x = rw_op.read()
    rw_op.close()
    return x

def faq():
    rw_op = open("./FAQ.txt","r")
    x =rw_op.read()
    rw_op.close()
    return x