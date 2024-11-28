from encryptionclasses import CaesarCypher, VernamCypher, Base64Cypher
from application import create_gui
from frequency_analysis import frequency_analysis

# Callback function for submit button
def submit_callback(operation, cipher_type, plaintext, key, shift):
    result = ""
    if cipher_type == "Caesar":
        try:
            shift = int(shift)  # Convert shift to integer
            caesar = CaesarCypher(shift, plaintext)
            if operation == "Encrypt":
                result = caesar.Encrypt()  # Encrypt using Caesar Cipher
            else:
                result = caesar.Decrypt()  # Decrypt using Caesar Cipher
        except ValueError:
            result = "Invalid shift value"  # Handle invalid shift value
    elif cipher_type == "Vernam":
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
    
    return result

# Callback function for frequency analysis button
def freq_analysis_callback(text):
    frequency_analysis(text)  # Perform frequency analysis on the text

# Create the GUI and start the main loop
root, result_label = create_gui(submit_callback, freq_analysis_callback)
root.mainloop()  # Start the Tkinter main loop