import socket, subprocess, os

INSTANCES = 0

srv = socket.socket()
srv.bind(('', 3202))
srv.listen(3)

while 1:
    connection, address = srv.accept()
    data = int(connection.recv(1024))
    connection.close()

    if data == 0 and INSTANCES != 0:
        process.send_signal(2)
        INSTANCES = 0
    elif data == 1 and INSTANCES == 0:
        process = subprocess.Popen('python ~/python/backlight_mod.py', shell=True)
        INSTANCES = 1
