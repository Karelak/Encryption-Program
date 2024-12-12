import logging

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


class VigenereCipher:
    """Class to handle Vigenere cipher encryption and decryption."""
    
    def __init__(self, key: str):
        """Initialize with a key."""
        self.key = key.upper()

    def _format_text(self, text: str) -> str:
        """Format the text by removing non-alphabetic characters and converting to uppercase."""
        return ''.join(filter(str.isalpha, text)).upper()

    def _shift_character(self, char: str, key_char: str, encrypt: bool = True) -> str:
        """Shift a character by the key character amount, either encrypting or decrypting."""
        shift = ord(key_char) - ord('A')
        if not encrypt:
            shift = -shift
        return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

    def encrypt(self, plaintext: str) -> str:
        """Encrypt the plaintext using Vigenere cipher."""
        formatted_text = self._format_text(plaintext)
        ciphertext = []
        key_length = len(self.key)
        
        for i, char in enumerate(formatted_text):
            key_char = self.key[i % key_length]
            ciphertext.append(self._shift_character(char, key_char, encrypt=True))
        
        return ''.join(ciphertext)

    def decrypt(self, ciphertext: str) -> str:
        """Decrypt the ciphertext using Vigenere cipher."""
        formatted_text = self._format_text(ciphertext)
        plaintext = []
        key_length = len(self.key)
        
        for i, char in enumerate(formatted_text):
            key_char = self.key[i % key_length]
            plaintext.append(self._shift_character(char, key_char, encrypt=False))
        
        return ''.join(plaintext)