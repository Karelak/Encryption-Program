import base64

class CaesarCypher:
    def __init__(self, shift, input):
        self.shift = shift
        self.input = input

    # Method to encrypt the input using Caesar Cipher
    def Encrypt(self):
        encrypted_data = ''
        for char in self.input:
            if char.isalpha():
                if char.isupper():
                    encrypted_data += chr((ord(char) + self.shift - 65) % 26 + 65)
                else:
                    encrypted_data += chr((ord(char) + self.shift - 97) % 26 + 97)
            else:
                encrypted_data += char
        return encrypted_data

    # Method to decrypt the input using Caesar Cipher
    def Decrypt(self):
        decrypted_data = ''
        for char in self.input:
            if char.isalpha():
                if char.isupper():
                    decrypted_data += chr((ord(char) - self.shift - 65) % 26 + 65)
                else:
                    decrypted_data += chr((ord(char) - self.shift - 97) % 26 + 97)
            else:
                decrypted_data += char
        return decrypted_data

class VernamCypher:
    def __init__(self, key, input):
        self.key = key
        self.input = input

    # Method to encrypt the input using Vernam Cipher
    def Encrypt(self):
        if len(self.key) == 0:
            return "Key cannot be empty"
        encrypted_data = ''
        for i in range(len(self.input)):
            encrypted_data += chr(ord(self.input[i]) ^ ord(self.key[i % len(self.key)]))
        return encrypted_data

    # Method to decrypt the input using Vernam Cipher
    def Decrypt(self):
        if len(self.key) == 0:
            return "Key cannot be empty"
        decrypted_data = ''
        for i in range(len(self.input)):
            decrypted_data += chr(ord(self.input[i]) ^ ord(self.key[i % len(self.key)]))
        return decrypted_data

class Base64Cypher:
    def __init__(self, input):
        self.input = input
    
        # Method to encrypt the input using Base64 Cipher
    def Encrypt(self):
        return base64.b64encode(self.input.encode()).decode()
    
        # Method to decrypt the input using Base64 Cipher
    def Decrypt(self):
        return base64.b64decode(self.input.encode()).decode()