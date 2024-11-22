from encryptionclasses import CaesarCypher, VernamCypher
from application import create_gui

def submit_callback(cipher_type, plaintext, key, shift):
    result = ""
    if cipher_type == "Caesar":
        shift = int(shift)
        caesar = CaesarCypher(shift, plaintext)
        result = caesar.Encrypt()
    elif cipher_type == "Vernam":
        vernam = VernamCypher(key, plaintext)
        result = vernam.Encrypt()
    
    result_label.config(text=f"Result: {result}")

root, result_label = create_gui(submit_callback)
root.mainloop()
