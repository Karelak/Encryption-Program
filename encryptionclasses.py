import base64
import logging
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class CaesarCypher:
    def __init__(self, shift, input):
        self.shift = shift  # Shift value for Caesar Cipher
        self.input = input  # Input text to be encrypted/decrypted

    # Method to encrypt the input using Caesar Cipher
    def Encrypt(self):
        encrypted_data = ''
        for char in self.input:
            if char.isalpha():  # Check if character is alphabetic
                if char.isupper():
                    encrypted_data += chr((ord(char) + self.shift - 65) % 26 + 65)  # Encrypt uppercase letters
                else:
                    encrypted_data += chr((ord(char) + self.shift - 97) % 26 + 97)  # Encrypt lowercase letters
            else:
                encrypted_data += char  # Non-alphabetic characters remain unchanged
        return encrypted_data

    # Method to decrypt the input using Caesar Cipher
    def Decrypt(self):
        decrypted_data = ''
        for char in self.input:
            if char.isalpha():  # Check if character is alphabetic
                if char.isupper():
                    decrypted_data += chr((ord(char) - self.shift - 65) % 26 + 65)  # Decrypt uppercase letters
                else:
                    decrypted_data += chr((ord(char) - self.shift - 97) % 26 + 97)  # Decrypt lowercase letters
            else:
                decrypted_data += char  # Non-alphabetic characters remain unchanged
        return decrypted_data

class VernamCypher:
    def __init__(self, key, input):
        self.key = key  # Key for Vernam Cipher
        self.input = input  # Input text to be encrypted/decrypted

    # Method to encrypt the input using Vernam Cipher
    def Encrypt(self):
        if len(self.key) == 0:
            return "Key cannot be empty"  # Handle empty key
        encrypted_data = ''
        for i in range(len(self.input)):
            encrypted_data += chr(ord(self.input[i]) ^ ord(self.key[i % len(self.key)]))  # XOR encryption
        return encrypted_data

    # Method to decrypt the input using Vernam Cipher
    def Decrypt(self):
        if len(self.key) == 0:
            return "Key cannot be empty"  # Handle empty key
        decrypted_data = ''
        for i in range(len(self.input)):
            decrypted_data += chr(ord(self.input[i]) ^ ord(self.key[i % len(self.key)]))  # XOR decryption
        return decrypted_data

class Base64Cypher:
    def __init__(self, input):
        self.input = input  # Input text to be encrypted/decrypted
    
    # Method to encrypt the input using Base64 Cipher
    def Encrypt(self):
        return base64.b64encode(self.input.encode()).decode()  # Base64 encode the input
    
    # Method to decrypt the input using Base64 Cipher
    def Decrypt(self):
        return base64.b64decode(self.input.encode()).decode()  # Base64 decode the input

class RSACypher:
    def __init__(self, key, input):
        self.key = key  # Key for RSA Cipher
        self.input = input  # Input text to be encrypted/decrypted
        logging.debug(f"RSACypher initialized with key: {key} and input: {input}")

    def Encrypt(self):
        try:
            public_key = RSA.import_key(self.key)
            cipher = PKCS1_OAEP.new(public_key)
            encrypted_data = cipher.encrypt(self.input.encode())
            logging.debug(f"Encrypted data: {encrypted_data.hex()}")
            return encrypted_data.hex()
        except (ValueError, TypeError) as e:
            logging.error(f"Encryption error: {str(e)}")
            return f"Encryption error: {str(e)}"

    def Decrypt(self):
        try:
            private_key = RSA.import_key(self.key)
            cipher = PKCS1_OAEP.new(private_key)
            decrypted_data = cipher.decrypt(bytes.fromhex(self.input))
            logging.debug(f"Decrypted data: {decrypted_data.decode()}")
            return decrypted_data.decode()
        except (ValueError, TypeError) as e:
            logging.error(f"Decryption error: {str(e)}")
            return f"Decryption error: {str(e)}"