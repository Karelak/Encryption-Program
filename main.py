from encryptionclasses import CaesarCypher, VernamCypher, Base64Cypher
from application import create_gui
from frequency_analysis import frequency_analysis

# Callback function for submit button
def submit_callback(operation, cipher_type, plaintext, key, shift):
    result = ""
    if cipher_type == "Caesar":
        try:
            shift = int(shift)
            caesar = CaesarCypher(shift, plaintext)
            if operation == "Encrypt":
                result = caesar.Encrypt()
            else:
                result = caesar.Decrypt()
        except ValueError:
            result = "Invalid shift value"
    elif cipher_type == "Vernam":
        vernam = VernamCypher(key, plaintext)
        if operation == "Encrypt":
            result = vernam.Encrypt()
        else:
            result = vernam.Decrypt()
    elif cipher_type == "Base64":
        base64 = Base64Cypher(plaintext)
        if operation == "Encrypt":
            result = base64.Encrypt()
        else:
            result = base64.Decrypt()
    
    return result

# Callback function for frequency analysis button
def freq_analysis_callback(text):
    frequency_analysis(text)

# Create the GUI and start the main loop
root, result_label = create_gui(submit_callback, freq_analysis_callback)
root.mainloop()