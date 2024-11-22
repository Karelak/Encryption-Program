class CaesarCypher:
    def __init__(self, shift, input, output):
        self.shift = shift
        self.input = input
        self.output = output
    def Encrypt(self):
        with open(self.input, 'r') as file:
            data = file.read()
            encrypted_data = ''
            for char in data:
                if char.isalpha():
                    if char.isupper():
                        encrypted_data += chr((ord(char) + self.shift - 65) % 26 + 65)
                    else:
                        encrypted_data += chr((ord(char) + self.shift - 97) % 26 + 97)
                else:
                    encrypted_data += char
        with open(self.output, 'w') as file:
            file.write(encrypted_data)
    def Decrypt(self):
        with open(self.input, 'r') as file:
            data = file.read()
            decrypted_data = ''
            for char in data:
                if char.isalpha():
                    if char.isupper():
                        decrypted_data += chr((ord(char) - self.shift - 65) % 26 + 65)
                    else:
                        decrypted_data += chr((ord(char) - self.shift - 97) % 26 + 97)

class VernamCypher:
    def __init__(self, key, input, output):
        self.key = key
        self.input = input
        self.output = output
    def Encrypt(self):
        with open(self.input, 'r') as file:
            data = file.read()
            encrypted_data = ''
            for i in range(len(data)):
                encrypted_data += chr(ord(data[i]) ^ ord(self.key[i % len(self.key)]))
        with open(self.output, 'w') as file:
            file.write(encrypted_data)
    def Decrypt(self):
        with open(self.input, 'r') as file:
            data = file.read()
            decrypted_data = ''
            for i in range(len(data)):
                decrypted_data += chr(ord(data[i]) ^ ord(self.key[i % len(self.key)]))
        with open(self.output, 'w') as file:
            file.write(decrypted_data)
