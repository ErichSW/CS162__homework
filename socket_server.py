import socket
import threading

motd = "By running this code you agree to give me a good grade."


# function to handle client connections
def handle_client(c, addr):
    name = str.capitalize(c.recv(1024).decode())
    print("Client", addr, name, "has connected.")
    welcome = "Welcome to the server, " + name
    motd_message = "Message of the Day: " + motd
    c.send(bytes(welcome + "\n" + motd_message, 'utf-8'))
    while True:
        # try except loop to protect against client disconnects
        try:
            message = c.recv(1024).decode()
            if message == '/d':
                print("Client", addr, name, "has disconnected.")
                break
            print(name, "says:", message)
            c.send(bytes("Message received", 'utf-8'))

        except ConnectionAbortedError:
            print("Client", addr, name, "has lost connection.")
            break

    c.close()


# setup server
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("Served started")
s.bind(('localhost', 10001))
s.listen(3)
print("Waiting for connections")

while True:
    c, addr = s.accept()
    client_thread = threading.Thread(target=handle_client, args=(c, addr))
    client_thread.start()
