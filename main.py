import logging
from encryptionclasses import CaesarCypher, VernamCypher, Base64Cypher, RSACypher
from application import create_gui
from frequency_analysis import frequency_analysis

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Callback function for submit button
def submit_callback(operation, cipher_type, plaintext, key, shift):
    logging.debug(f"Operation: {operation}, Cipher: {cipher_type}, Plaintext: {plaintext}, Key: {key}, Shift: {shift}")
    result = ""
    if not plaintext:
        result = "Plaintext cannot be empty"
        logging.error("Plaintext cannot be empty")
    elif cipher_type == "Caesar":
        try:
            shift = int(shift)  # Convert shift to integer
            caesar = CaesarCypher(shift, plaintext)
            if operation == "Encrypt":
                result = caesar.Encrypt()  # Encrypt using Caesar Cipher
            else:
                result = caesar.Decrypt()  # Decrypt using Caesar Cipher
        except ValueError:
            result = "Invalid shift value"  # Handle invalid shift value
            logging.error("Invalid shift value")
    elif cipher_type == "Vernam":
        if not key:
            result = "Key cannot be empty for Vernam Cipher"
            logging.error("Key cannot be empty for Vernam Cipher")
        else:
            vernam = VernamCypher(key, plaintext)
            if operation == "Encrypt":
                result = vernam.Encrypt()  # Encrypt using Vernam Cipher
            else:
                result = vernam.Decrypt()  # Decrypt using Vernam Cipher
    elif cipher_type == "Base64":
        base64 = Base64Cypher(plaintext)
        if operation == "Encrypt":
            result = base64.Encrypt()  # Encrypt using Base64 Cipher
        else:
            result = base64.Decrypt()  # Decrypt using Base64 Cipher
    elif cipher_type == "RSA":
        if not key:
            result = "Key cannot be empty for RSA Cipher"
            logging.error("Key cannot be empty for RSA Cipher")
        else:
            try:
                with open(key, 'r') as key_file:
                    key_content = key_file.read()
                rsa = RSACypher(key_content, plaintext)
                if operation == "Encrypt":
                    result = rsa.Encrypt()  # Encrypt using RSA Cipher (requires public key)
                else:
                    result = rsa.Decrypt()  # Decrypt using RSA Cipher (requires private key)
            except (ValueError, TypeError, FileNotFoundError) as e:
                result = f"RSA key format error: {str(e)}"  # Handle RSA key format error
                logging.error(f"RSA key format error: {str(e)}")
    
    logging.debug(f"Result: {result}")
    return result

# Callback function for frequency analysis button
def freq_analysis_callback(text):
    logging.debug(f"Frequency analysis for text: {text}")
    frequency_analysis(text)  # Perform frequency analysis on the text

# Callback function for encryption info button
def encryption_info_callback():
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

# Create the GUI and start the main loop
root, result_label = create_gui(submit_callback, freq_analysis_callback, encryption_info_callback)
root.mainloop()  # Start the Tkinter main loop