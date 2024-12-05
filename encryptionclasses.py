import base64
import logging
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CaesarCypher:
    """Class to handle Caesar cipher encryption and decryption."""
    
    def __init__(self, shift: int, input: str):
        """Initialize with a shift value and input text."""
        self.shift = shift
        self.input = input

    def Encrypt(self) -> str:
        """Encrypt the input text using Caesar cipher."""
        encrypted_data = ''
        for char in self.input:
            if char.isalpha():
                if char.isupper():
                    encrypted_data += chr((ord(char) + self.shift - 65) % 26 + 65)
                else:
                    encrypted_data += chr((ord(char) + self.shift - 97) % 26 + 97)
            else:
                encrypted_data += char
        logging.info(f"Caesar Cipher Encrypt result: {encrypted_data}")
        return encrypted_data

    def Decrypt(self) -> str:
        """Decrypt the input text using Caesar cipher."""
        decrypted_data = ''
        for char in self.input:
            if char.isalpha():
                if char.isupper():
                    decrypted_data += chr((ord(char) - self.shift - 65) % 26 + 65)
                else:
                    decrypted_data += chr((ord(char) - self.shift - 97) % 26 + 97)
            else:
                decrypted_data += char
        logging.info(f"Caesar Cipher Decrypt result: {decrypted_data}")
        return decrypted_data

class VernamCypher:
    """Class to handle Vernam cipher encryption and decryption."""
    
    def __init__(self, key: str, input: str):
        """Initialize with a key and input text."""
        if not key:
            raise ValueError("Key cannot be empty for Vernam Cipher")
        if len(key) != len(input):
            raise ValueError("Key length must match input length for Vernam Cipher")
        
        self.key = key
        self.input = input
        logging.debug(f"VernamCypher initialized with key: {key} and input: {input}")

    def Encrypt(self) -> str:
        """Encrypt the input text using Vernam cipher."""
        encrypted_data = ''.join(chr(ord(self.input[i]) ^ ord(self.key[i])) for i in range(len(self.input)))
        logging.info(f"Vernam Cipher Encrypt result: {encrypted_data}")
        return encrypted_data

    def Decrypt(self) -> str:
        """Decrypt the input text using Vernam cipher."""
        decrypted_data = ''.join(chr(ord(self.input[i]) ^ ord(self.key[i])) for i in range(len(self.input)))
        logging.info(f"Vernam Cipher Decrypt result: {decrypted_data}")
        return decrypted_data

class Base64Cypher:
    """Class to handle Base64 encoding and decoding."""
    
    def __init__(self, input: str):
        """Initialize with input text."""
        self.input = input
    
    def Encrypt(self) -> str:
        """Encode the input text using Base64."""
        result = base64.b64encode(self.input.encode()).decode()
        logging.info(f"Base64 Cipher Encrypt result: {result}")
        return result
    
    def Decrypt(self) -> str:
        """Decode the input text from Base64."""
        result = base64.b64decode(self.input.encode()).decode()
        logging.info(f"Base64 Cipher Decrypt result: {result}")
        return result

class RSACypher:
    """Class to handle RSA encryption and decryption."""
    
    def __init__(self, key: str, input: str):
        """Initialize with a key and input text."""
        self.key = key
        self.input = input
        logging.debug(f"RSACypher initialized with key: {key} and input: {input}")

    def Encrypt(self) -> str:
        """Encrypt the input text using RSA."""
        try:
            public_key = RSA.import_key(self.key)
            cipher = PKCS1_OAEP.new(public_key)
            encrypted_data = cipher.encrypt(self.input.encode())
            result = encrypted_data.hex()
            logging.info(f"RSA Cipher Encrypt result: {result}")
            return result
        except (ValueError, TypeError) as e:
            logging.error(f"Encryption error: {str(e)}")
            return f"Encryption error: {str(e)}"

    def Decrypt(self) -> str:
        """Decrypt the input text using RSA."""
        try:
            private_key = RSA.import_key(self.key)
            cipher = PKCS1_OAEP.new(private_key)
            decrypted_data = cipher.decrypt(bytes.fromhex(self.input))
            result = decrypted_data.decode()
            logging.info(f"RSA Cipher Decrypt result: {result}")
            return result
        except (ValueError, TypeError) as e:
            logging.error(f"Decryption error: {str(e)}")
            return f"Decryption error: {str(e)}"