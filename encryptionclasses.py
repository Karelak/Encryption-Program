import base64

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