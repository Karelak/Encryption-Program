import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CaesarCypher:
    # Class to handle Caesar cipher encryption and decryption.
    
    def __init__(self, shift: int, input: str):
        # Initialize with a shift value and input text.
        self.shift = shift
        self.input = input

    def Encrypt(self) -> str:
        # Encrypt the input text using Caesar cipher.
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

    def Decrypt(self) -> str:
        # Decrypt the input text using Caesar cipher.
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
    # Class to handle Vernam cipher encryption and decryption.
    
    def __init__(self, key: str, input: str):
        # Initialize with a key and input text.
        if not key:
            raise ValueError("Key cannot be empty for Vernam Cipher")
        if len(key) != len(input):
            raise ValueError("Key length must match input length for Vernam Cipher")
        
        self.key = key
        self.input = input
        logging.debug(f"VernamCypher initialized with key: {key} and input: {input}")

    def Encrypt(self) -> str:
        # Encrypt the input text using Vernam cipher.
        encrypted_data = ''.join(chr(ord(self.input[i]) ^ ord(self.key[i])) for i in range(len(self.input)))
        return encrypted_data

    def Decrypt(self) -> str:
        # Decrypt the input text using Vernam cipher.
        decrypted_data = ''.join(chr(ord(self.input[i]) ^ ord(self.key[i])) for i in range(len(self.input)))
        return decrypted_data

class VigenereCipher:
    # Class to handle Vigenere cipher encryption and decryption.
    
    def __init__(self, key: str, input_text: str):
        # Initialize with a key and input text.
        self.key = key
        self.input = input_text

    def encrypt(self) -> str:
        # Encrypt the input text using Vigenere cipher.
        encrypted_data = ''
        key_length = len(self.key)
        key_index = 0

        for char in self.input:
            if char.isalpha():
                shift = ord(self.key[key_index % key_length].lower()) - ord('a')
                if char.islower():
                    encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                else:
                    encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                encrypted_data += encrypted_char
                key_index += 1
            else:
                encrypted_data += char
        return encrypted_data

    def decrypt(self) -> str:
        # Decrypt the input text using Vigenere cipher.
        decrypted_data = ''
        key_length = len(self.key)
        key_index = 0

        for char in self.input:
            if char.isalpha():
                shift = ord(self.key[key_index % key_length].lower()) - ord('a')
                if char.islower():
                    decrypted_char = chr((ord(char) - ord('a') - shift + 26) % 26 + ord('a'))
                else:
                    decrypted_char = chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
                decrypted_data += decrypted_char
                key_index += 1
            else:
                decrypted_data += char
        return decrypted_data