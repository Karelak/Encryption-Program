import logging
from encryptionclasses import CaesarCypher, VernamCypher, Base64Cypher, RSACypher
from application import Application
from frequency_analysis import frequency_analysis

class EncryptionProgram:
    """Main class for the Encryption Program handling initialization and callbacks."""

    def __init__(self):
        # Initialize logging and the application interface
        self.setup_logging()
        self.app = Application(self.submit_callback, self.freq_analysis_callback, self.encryption_info_callback)

    def setup_logging(self):
        """Setup the logging configuration."""
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def submit_callback(self, operation: str, cipher_type: str, plaintext: str, key: str, shift: str) -> str:
        """Handle the submission of encryption/decryption requests."""
        logging.info(f"Operation: {operation}, Cipher: {cipher_type}")
        if not plaintext:
            logging.error("Plaintext cannot be empty")
            return "Plaintext cannot be empty"
        
        try:
            if cipher_type == "Caesar":
                return self.handle_caesar(operation, plaintext, shift)
            elif cipher_type == "Vernam":
                return self.handle_vernam(operation, plaintext, key)
            elif cipher_type == "Base64":
                return self.handle_base64(operation, plaintext)
            elif cipher_type == "RSA":
                return self.handle_rsa(operation, plaintext, key)
            else:
                logging.error("Unsupported cipher type")
                return "Unsupported cipher type"
        except Exception as e:
            logging.error(f"Error during {operation}: {str(e)}")
            return f"Error during {operation}: {str(e)}"

    def handle_caesar(self, operation: str, plaintext: str, shift: str) -> str:
        """Handle Caesar cipher encryption/decryption."""
        try:
            shift = int(shift)
            caesar = CaesarCypher(shift, plaintext)
            result = caesar.Encrypt() if operation == "Encrypt" else caesar.Decrypt()
            logging.info(f"Caesar Cipher {operation} result: {result}")
            return result
        except ValueError:
            logging.error("Invalid shift value")
            return "Invalid shift value"

    def handle_vernam(self, operation: str, plaintext: str, key: str) -> str:
        """Handle Vernam cipher encryption/decryption."""
        if not key:
            logging.error("Key cannot be empty for Vernam Cipher")
            return "Key cannot be empty for Vernam Cipher"
        vernam = VernamCypher(key, plaintext)
        result = vernam.Encrypt() if operation == "Encrypt" else vernam.Decrypt()
        logging.info(f"Vernam Cipher {operation} result: {result}")
        return result

    def handle_base64(self, operation: str, plaintext: str) -> str:
        """Handle Base64 encoding/decoding."""
        base64 = Base64Cypher(plaintext)
        result = base64.Encrypt() if operation == "Encrypt" else base64.Decrypt()
        logging.info(f"Base64 Cipher {operation} result: {result}")
        return result

    def handle_rsa(self, operation: str, plaintext: str, key: str) -> str:
        """Handle RSA encryption/decryption."""
        if not key:
            logging.error("Key cannot be empty for RSA Cipher")
            return "Key cannot be empty for RSA Cipher"
        try:
            with open(key, 'r') as key_file:
                key_content = key_file.read()
            rsa = RSACypher(key_content, plaintext)
            result = rsa.Encrypt() if operation == "Encrypt" else rsa.Decrypt()
            logging.info(f"RSA Cipher {operation} result: {result}")
            return result
        except (ValueError, TypeError, FileNotFoundError) as e:
            logging.error(f"RSA key format error: {str(e)}")
            return f"RSA key format error: {str(e)}"

    def freq_analysis_callback(self, text: str):
        """Callback to perform frequency analysis on the provided text."""
        logging.info(f"Performing frequency analysis for text of length {len(text)}")
        frequency_analysis(text)

    def encryption_info_callback(self) -> str:
        """Provide information about symmetric and asymmetric encryption."""
        logging.info("Encryption info requested")
        info_text = """
        Symmetric Encryption:
        - Uses the same key for both encryption and decryption.
        - Examples: Caesar Cipher, Vernam Cipher, Base64 Cipher.

        Asymmetric Encryption:
        - Uses a pair of keys (public and private) for encryption and decryption.
        - Example: RSA.
        """
        return info_text

    def run(self):
        """Start the Encryption Program."""
        logging.info("Starting Encryption Program")
        self.app.run()

if __name__ == "__main__":
    program = EncryptionProgram()
    program.run()