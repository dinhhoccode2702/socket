import socket
import threading

def handle_client(connectionSocket, addr):
    sentence = connectionSocket.recv(1024)
    capitalizedSentence = sentence.decode().upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()

serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)

while True:
    connectionSocket, addr = serverSocket.accept()
    thread = threading.Thread(target=handle_client, args=(connectionSocket, addr))
    thread.start()