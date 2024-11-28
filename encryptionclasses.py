import base64
import logging
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CaesarCypher:
    def __init__(self, shift: int, input: str):
        self.shift = shift
        self.input = input

    def Encrypt(self) -> str:
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
    def __init__(self, key: str, input: str):
        self.key = key
        self.input = input

    def Encrypt(self) -> str:
        if len(self.key) == 0:
            logging.error("Key cannot be empty for Vernam Cipher")
            return "Key cannot be empty"
        encrypted_data = ''
        for i in range(len(self.input)):
            encrypted_data += chr(ord(self.input[i]) ^ ord(self.key[i % len(self.key)]))
        logging.info(f"Vernam Cipher Encrypt result: {encrypted_data}")
        return encrypted_data

    def Decrypt(self) -> str:
        if len(self.key) == 0:
            logging.error("Key cannot be empty for Vernam Cipher")
            return "Key cannot be empty"
        decrypted_data = ''
        for i in range(len(self.input)):
            decrypted_data += chr(ord(self.input[i]) ^ ord(self.key[i % len(self.key)]))
        logging.info(f"Vernam Cipher Decrypt result: {decrypted_data}")
        return decrypted_data

class Base64Cypher:
    def __init__(self, input: str):
        self.input = input
    
    def Encrypt(self) -> str:
        result = base64.b64encode(self.input.encode()).decode()
        logging.info(f"Base64 Cipher Encrypt result: {result}")
        return result
    
    def Decrypt(self) -> str:
        result = base64.b64decode(self.input.encode()).decode()
        logging.info(f"Base64 Cipher Decrypt result: {result}")
        return result

class RSACypher:
    def __init__(self, key: str, input: str):
        self.key = key
        self.input = input
        logging.debug(f"RSACypher initialized with key: {key} and input: {input}")

    def Encrypt(self) -> str:
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