import logging
from encryptionclasses import CaesarCypher, VernamCypher, Base64Cypher, RSACypher
from application import Application
from frequency_analysis import frequency_analysis

class EncryptionProgram:
    def __init__(self):
        self.setup_logging()
        self.app = Application(self.submit_callback, self.freq_analysis_callback, self.encryption_info_callback)

    def setup_logging(self):
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    def submit_callback(self, operation, cipher_type, plaintext, key, shift):
        logging.debug(f"Operation: {operation}, Cipher: {cipher_type}, Plaintext: {plaintext}, Key: {key}, Shift: {shift}")
        result = ""
        if not plaintext:
            result = "Plaintext cannot be empty"
            logging.error("Plaintext cannot be empty")
        elif cipher_type == "Caesar":
            try:
                shift = int(shift)
                caesar = CaesarCypher(shift, plaintext)
                result = caesar.Encrypt() if operation == "Encrypt" else caesar.Decrypt()
            except ValueError:
                result = "Invalid shift value"
                logging.error("Invalid shift value")
        elif cipher_type == "Vernam":
            if not key:
                result = "Key cannot be empty for Vernam Cipher"
                logging.error("Key cannot be empty for Vernam Cipher")
            else:
                vernam = VernamCypher(key, plaintext)
                result = vernam.Encrypt() if operation == "Encrypt" else vernam.Decrypt()
        elif cipher_type == "Base64":
            base64 = Base64Cypher(plaintext)
            result = base64.Encrypt() if operation == "Encrypt" else base64.Decrypt()
        elif cipher_type == "RSA":
            if not key:
                result = "Key cannot be empty for RSA Cipher"
                logging.error("Key cannot be empty for RSA Cipher")
            else:
                try:
                    with open(key, 'r') as key_file:
                        key_content = key_file.read()
                    rsa = RSACypher(key_content, plaintext)
                    result = rsa.Encrypt() if operation == "Encrypt" else rsa.Decrypt()
                except (ValueError, TypeError, FileNotFoundError) as e:
                    result = f"RSA key format error: {str(e)}"
                    logging.error(f"RSA key format error: {str(e)}")
        logging.debug(f"Result: {result}")
        return result

    def freq_analysis_callback(self, text):
        logging.debug(f"Frequency analysis for text: {text}")
        frequency_analysis(text)

    def encryption_info_callback(self):
        info_text = """
        Symmetric Encryption:
        - Uses the same key for both encryption and decryption.
        - Examples: Caesar Cipher, Vernam Cipher, Base64 Cipher.

        Asymmetric Encryption:
        - Uses a pair of keys (public and private) for encryption and decryption.
        - Example: RSA.
        """
        logging.debug("Encryption info requested")
        return info_text

    def run(self):
        self.app.run()

if __name__ == "__main__":
    program = EncryptionProgram()
    program.run()