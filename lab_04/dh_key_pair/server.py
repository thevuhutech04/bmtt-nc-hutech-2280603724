from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

def generate_dh_parameters():
    # Generate Diffie-Hellman parameters with a 2048-bit key size
    parameters = dh.generate_parameters(generator=2, key_size=2048)
    return parameters

def generate_server_key_pair(parameters):
    # Generate the server's private and public key pair from the parameters
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

def main():
    # Generate the Diffie-Hellman parameters
    parameters = generate_dh_parameters()

    # Generate the server's private and public key pair
    private_key, public_key = generate_server_key_pair(parameters)

    # Serialize the server's public key and save it to a PEM file
    with open("server_public_key.pem", "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

    print("Server public key saved to 'server_public_key.pem'.")

if __name__ == "__main__":
    main()
