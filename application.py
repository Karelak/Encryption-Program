import tkinter as tk
from tkinter import ttk

def create_gui(submit_callback, freq_analysis_callback):
    root = tk.Tk()
    root.title('Encryption Program')
    root.geometry("600x400")

    # Operation Selection
    operation_var = tk.StringVar(value="Encrypt")
    operation_label = ttk.Label(root, text="Select Operation:")
    operation_menu = ttk.Combobox(root, textvariable=operation_var, values=["Encrypt", "Decrypt"])
    operation_label.pack(anchor=tk.W, padx=10, pady=5)
    operation_menu.pack(anchor=tk.W, padx=10, pady=5)

    # Cipher Selection
    cipher_var = tk.StringVar(value="Caesar")
    cipher_label = ttk.Label(root, text="Select Cipher:")
    cipher_menu = ttk.Combobox(root, textvariable=cipher_var, values=["Caesar", "Vernam"])
    cipher_label.pack(anchor=tk.W, padx=10, pady=5)
    cipher_menu.pack(anchor=tk.W, padx=10, pady=5)

    # Plaintext Entry
    plaintext_label = ttk.Label(root, text="Plaintext:")
    plaintext_entry = ttk.Entry(root)
    plaintext_label.pack(anchor=tk.W, padx=10, pady=5)
    plaintext_entry.pack(anchor=tk.W, padx=10, pady=5)

    # Key Entry (Vernam)
    key_label = ttk.Label(root, text="Key (for Vernam):")
    key_entry = ttk.Entry(root)

    # Shift Entry (Caesar)
    shift_label = ttk.Label(root, text="Shift (for Caesar):")
    shift_entry = ttk.Entry(root)

    # Result Label
    result_label = ttk.Label(root, text="Result:")
    result_label.pack(anchor=tk.W, padx=10, pady=5)

    def local_submit_callback(operation, cipher_type, plaintext, key, shift):
        submit_callback(operation, cipher_type, plaintext, key, shift, result_label)

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
        # Trigger callback with current values
        local_submit_callback(operation_var.get(), cipher_var.get(), plaintext_entry.get(), key_entry.get(), shift_entry.get())

    cipher_var.trace("w", update_fields)
    operation_var.trace("w", update_fields)
    plaintext_entry.bind("<KeyRelease>", lambda event: local_submit_callback(operation_var.get(), cipher_var.get(), plaintext_entry.get(), key_entry.get(), shift_entry.get()))
    key_entry.bind("<KeyRelease>", lambda event: local_submit_callback(operation_var.get(), cipher_var.get(), plaintext_entry.get(), key_entry.get(), shift_entry.get()))
    shift_entry.bind("<KeyRelease>", lambda event: local_submit_callback(operation_var.get(), cipher_var.get(), plaintext_entry.get(), key_entry.get(), shift_entry.get()))

    update_fields()  # Initialize the fields based on the default cipher

    submit_button = ttk.Button(root, text="Submit", command=lambda: local_submit_callback(operation_var.get(), cipher_var.get(), plaintext_entry.get(), key_entry.get(), shift_entry.get()))
    submit_button.pack(anchor=tk.W, padx=10, pady=5)

    freq_analysis_button = ttk.Button(root, text="Frequency Analysis", command=lambda: freq_analysis_callback(plaintext_entry.get()))
    freq_analysis_button.pack(anchor=tk.W, padx=10, pady=5)

    return root, result_label