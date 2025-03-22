from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading
import hashlib

# Initialize client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

client_key = RSA.generate(2048)

# Receive server public key and send client's public key
server_public_key = RSA.import_key(client_socket.recv(2048))
client_socket.send(client_key.publickey().export_key(format='PEM'))

# Receive the encrypted AES key and decrypt it
encrypted_aes_key = client_socket.recv(2048)
cipher_rsa = PKCS1_OAEP.new(client_key)
aes_key = cipher_rsa.decrypt(encrypted_aes_key)

def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext

def decrypt_message(key, encrypted_message):
    iv = encrypted_message[:AES.block_size]
    ciphertext = encrypted_message[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message.decode()

def receive_messages():
    while True:
        encrypted_message = client_socket.recv(4096)
        if encrypted_message:
            decrypted_message = decrypt_message(aes_key, encrypted_message)
            print("Received: ", decrypted_message)

def send_messages():
    while True:
        message = input("Enter message ('exit' to quit): ")
        encrypted_message = encrypt_message(aes_key, message)
        client_socket.send(encrypted_message)
        if message == "exit":
            break

# Start receiving messages in a separate thread
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Send messages in the main thread
send_messages()

# Close the socket once done
client_socket.close()
