import tkinter as tk
from tkinter import ttk
from encryptionclasses import CaesarCypher, VernamCypher

def create_gui(submit_callback):
    root = tk.Tk()
    root.title('Encryption Program')
    root.geometry("600x400")

    cipher_var = tk.StringVar(value="Caesar")
    cipher_label = ttk.Label(root, text="Select Cipher:")
    cipher_menu = ttk.Combobox(root, textvariable=cipher_var, values=["Caesar", "Vernam"])
    cipher_label.pack(anchor=tk.W, padx=10, pady=5)
    cipher_menu.pack(anchor=tk.W, padx=10, pady=5)

    plaintext_label = ttk.Label(root, text="Plaintext:")
    plaintext_entry = ttk.Entry(root)
    plaintext_label.pack(anchor=tk.W, padx=10, pady=5)
    plaintext_entry.pack(anchor=tk.W, padx=10, pady=5)

    key_label = ttk.Label(root, text="Key (for Vernam):")
    key_entry = ttk.Entry(root)

    shift_label = ttk.Label(root, text="Shift (for Caesar):")
    shift_entry = ttk.Entry(root)

    def update_fields(*args):
        cipher_type = cipher_var.get()
        if cipher_type == "Caesar":
            shift_label.pack(anchor=tk.W, padx=10, pady=5)
            shift_entry.pack(anchor=tk.W, padx=10, pady=5)
            key_label.pack_forget()
            key_entry.pack_forget()
        elif cipher_type == "Vernam":
            key_label.pack(anchor=tk.W, padx=10, pady=5)
            key_entry.pack(anchor=tk.W, padx=10, pady=5)
            shift_label.pack_forget()
            shift_entry.pack_forget()

    cipher_var.trace("w", update_fields)
    update_fields()  # Initialize the fields based on the default cipher

    submit_button = ttk.Button(root, text="Submit", command=lambda: submit_callback(cipher_var.get(), plaintext_entry.get(), key_entry.get(), shift_entry.get()))
    submit_button.pack(anchor=tk.W, padx=10, pady=5)

    result_label = ttk.Label(root, text="Result:")
    result_label.pack(anchor=tk.W, padx=10, pady=5)

    return root, result_label

def submit(cipher_type, plaintext, key, shift):
    result = ""
    
    if cipher_type == "Caesar":
        shift = int(shift)
        caesar = CaesarCypher(shift, plaintext, "")
        result = caesar.Encrypt()
    elif cipher_type == "Vernam":
        vernam = VernamCypher(key, plaintext, "")
        result = vernam.Encrypt()
    
    result_label.config(text=f"Result: {result}")

root, result_label = create_gui(submit)
root.mainloop()
