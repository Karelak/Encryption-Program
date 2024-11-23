import tkinter as tk
from tkinter import ttk

# Function to create the GUI
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

    # Result Text Box
    result_label = ttk.Entry(root, state='readonly')
    result_label.pack(anchor=tk.W, padx=10, pady=5)

    # Local callback function to update the result
    def local_submit_callback(operation, cipher_type, plaintext, key, shift):
        result = submit_callback(operation, cipher_type, plaintext, key, shift)
        result_label.config(state='normal')
        result_label.delete(0, tk.END)
        result_label.insert(0, result)
        result_label.config(state='readonly')

    # Function to update fields based on selected cipher
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

    # Trace changes in cipher and operation selection
    cipher_var.trace("w", update_fields)
    operation_var.trace("w", update_fields)
    plaintext_entry.bind("<KeyRelease>", lambda event: local_submit_callback(operation_var.get(), cipher_var.get(), plaintext_entry.get(), key_entry.get(), shift_entry.get()))
    key_entry.bind("<KeyRelease>", lambda event: local_submit_callback(operation_var.get(), cipher_var.get(), plaintext_entry.get(), key_entry.get(), shift_entry.get()))
    shift_entry.bind("<KeyRelease>", lambda event: local_submit_callback(operation_var.get(), cipher_var.get(), plaintext_entry.get(), key_entry.get(), shift_entry.get()))

    update_fields()  # Initialize the fields based on the default cipher

    # Frequency Analysis Button
    freq_analysis_button = ttk.Button(root, text="Frequency Analysis", command=lambda: freq_analysis_callback(plaintext_entry.get()))
    freq_analysis_button.pack(anchor=tk.W, padx=10, pady=5)

    return root, result_label