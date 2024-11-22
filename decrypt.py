class CaesarCypher:

    def __init__(self, input, output, shift):
        self.input = input
        self.output = output
        self.shift = shift

    def decrypt(self):
        with open(self.input, 'r') as file:
            data = file.read()
            decrypted_data = ''
            for char in data:
                if char.isalpha():
                    if char.isupper():
                        decrypted_data += chr((ord(char) - self.shift - 65) % 26 + 65)
                    else:
                        decrypted_data += chr((ord(char) - self.shift - 97) % 26 + 97)
                else:
                    decrypted_data += char
        with open(self.output, 'w') as file:
            file.write(decrypted_data)


class VernamCypher:

    def __init__(self, input, output, key):
        self.input = input
        self.key = key
        self.output = output

    def decrypt(self):
        with open(self.input, 'r') as file:
            data = file.read()
            decrypted_data = ''
            for i in range(len(data)):
                decrypted_data += chr(ord(data[i]) ^ ord(self.key[i % len(self.key)]))
        with open(self.output, 'w') as file:
            file.write(decrypted_data)
