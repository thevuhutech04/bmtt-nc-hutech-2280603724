from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import os

def generate_client_key_pair(parameters):
    # Generate the client's private and public key pair based on the provided parameters
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

def generate_shared_secret(private_key, server_public_key):
    # Compute the shared secret using the client's private key and the server's public key
    shared_key = private_key.exchange(dh.ECDH(), server_public_key)  # Use ECDH (or regular DH) for key exchange
    return shared_key

def derive_symmetric_key(shared_secret):
    # Derive a symmetric key using PBKDF2HMAC from the shared secret
    salt = os.urandom(16)  # Generate random salt for key derivation
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000)
    symmetric_key = kdf.derive(shared_secret)
    return symmetric_key

def main():
    # Load the server's public key from the PEM file
    with open("server_public_key.pem", "rb") as f:
        server_public_key = serialization.load_pem_public_key(f.read())

    # Get the Diffie-Hellman parameters (this must match what the server is using)
    parameters = dh.generate_parameters(generator=2, key_size=2048)  # Use default DH parameters for exchange
    
    # Generate the client's private and public key pair based on the Diffie-Hellman parameters
    private_key, public_key = generate_client_key_pair(parameters)
    
    # Serialize and send the client's public key to the server (this part is usually done in communication)
    client_public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    print("Client public key (PEM):")
    print(client_public_key_pem.decode())

    # Simulate receiving the server's public key (in a real case, this would be via a network socket)
    # Example for now: we assume the public key is loaded in the server_public_key variable.
    
    # Generate the shared secret using the client's private key and the server's public key
    shared_secret = generate_shared_secret(private_key, server_public_key)
    
    print("Shared Secret (raw):", shared_secret.hex())

    # Derive a symmetric key from the shared secret
    symmetric_key = derive_symmetric_key(shared_secret)
    print("Derived Symmetric Key:", symmetric_key.hex())

if __name__ == "__main__":
    main()
