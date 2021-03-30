import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 5636)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(5)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                account = data.decode().split(",")
                if len(account) == 1:
                    cuenta = account[0]
                    with open("data.txt", "r") as f:
                        for line in f:
                            c, v = line.split(",")
                            if c == cuenta:
                                connection.sendall(v.strip().encode())
                                break
                        else:
                            connection.sendall(b"LA CUENTA NO EXISTE")
                elif len(account) == 2:
                    cuenta, valor = account
                    try:
                        cuenta = int(cuenta)
                        valor = int(valor)
                        with open("data.txt", "a") as f:
                            f.write("{}\n".format(data.decode("utf8")))
                        connection.sendall(b"OK")
                    except ValueError:
                        connection.sendall(b"NO-OK")
                else:
                    connection.sendall(b"error")

            else:
                print('no data from', client_address)
                break
    except ConnectionResetError:
        print("connection restarting")
    finally:
        # Clean up the connection
        connection.close()
