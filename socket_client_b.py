import socket

name = input("Enter your name: ")
print("Attempting to connect to server...")

# try except loop to protect against server not running
try:
    c = socket.socket()
    c.connect(('localhost', 10001))
    c.send(bytes(name, 'utf-8'))
    print("Connection successful.")
    print(c.recv(1024).decode())
    while True:
        # try except loop to protect against server disconnects
        try:
            message = input("Enter a message, or type '/d' to disconnect: ")
            c.send(bytes(message, 'utf-8'))
            if message == '/d':
                print("Closing connection")
                break
            print(c.recv(1024).decode())

        except ConnectionResetError:
            print("Server is not responding. Closing connection.")
            break
    c.close()

except ConnectionRefusedError:
    print("Server is not running. Contact the server administrator.")
    exit()
