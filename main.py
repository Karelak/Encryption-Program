from encryptionclasses import CaesarCypher, VernamCypher
from application import create_gui
from frequency_analysis import frequency_analysis

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
    
    return result

def freq_analysis_callback(text):
    frequency_analysis(text)

root, result_label = create_gui(submit_callback, freq_analysis_callback)
root.mainloop()