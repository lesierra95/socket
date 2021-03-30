import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 5636)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)


try:

    # Send data
    cuenta = str(input("Numero de Cuenta: "))
    sock.sendall(cuenta.encode())
    data = sock.recv(1024)
    print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()
