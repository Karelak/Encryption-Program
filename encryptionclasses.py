class CaesarCypher:
    def __init__(self, shift, input):
        self.shift = shift
        self.input = input

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

    def Encrypt(self):
        encrypted_data = ''
        for i in range(len(self.input)):
            encrypted_data += chr(ord(self.input[i]) ^ ord(self.key[i % len(self.key)]))
        return encrypted_data

    def Decrypt(self):
        decrypted_data = ''
        for i in range(len(self.input)):
            decrypted_data += chr(ord(self.input[i]) ^ ord(self.key[i % len(self.key)]))
        return decrypted_data