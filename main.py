from encryptionclasses import CaesarCypher, VernamCypher
from application import create_gui
from frequency_analysis import frequency_analysis

def submit_callback(cipher_type, plaintext, key, shift, result_label):
    result = ""
    if cipher_type == "Caesar":
        try:
            shift = int(shift)
            caesar = CaesarCypher(shift, plaintext)
            result = caesar.Encrypt()
        except ValueError:
            result = "Invalid shift value"
    elif cipher_type == "Vernam":
        vernam = VernamCypher(key, plaintext)
        result = vernam.Encrypt()
    
    result_label.config(text=f"Result: {result}")

def freq_analysis_callback(text):
    frequency_analysis(text)

root, result_label = create_gui(submit_callback, freq_analysis_callback)
root.mainloop()