import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

class ECCCipher:
    def __init__(self):
        self.private_key = None
        self.public_key = None
        self.key_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
    def generate_keys(self):
        self.private_key = ec.generate_private_key(ec.SECP384R1())
        self.public_key = self.private_key.public_key()
        
        # Save private key
        private_key_path = os.path.join(self.key_dir, "private_key.pem")
        with open(private_key_path, "wb") as f:
            f.write(self.private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            ))
            
        # Save public key
        public_key_path = os.path.join(self.key_dir, "public_key.pem")
        with open(public_key_path, "wb") as f:
            f.write(self.public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))
            
    def load_keys(self):
        # Load private key
        private_key_path = os.path.join(self.key_dir, "private_key.pem")
        with open(private_key_path, "rb") as f:
            self.private_key = serialization.load_pem_private_key(
                f.read(),
                password=None
            )
            
        # Load public key
        public_key_path = os.path.join(self.key_dir, "public_key.pem")
        with open(public_key_path, "rb") as f:
            self.public_key = serialization.load_pem_public_key(
                f.read()
            )
            
        return self.private_key, self.public_key
        
    def sign(self, message, private_key):
        signature = private_key.sign(
            message.encode(),
            ec.ECDSA(hashes.SHA256())
        )
        return signature
        
    def verify(self, message, signature, public_key):
        try:
            public_key.verify(
                signature,
                message.encode(),
                ec.ECDSA(hashes.SHA256())
            )
            return True
        except:
            return False 