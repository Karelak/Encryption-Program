import logging
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from Crypto.PublicKey import RSA

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to create the GUI
def create_gui(submit_callback, freq_analysis_callback, encryption_info_callback):
    logging.debug("Initializing GUI")
    root = tk.Tk()
    root.title('Encryption Program')  # Set the window title
    root.geometry("600x400")  # Set the window size

    # Create a frame to center the content
    main_frame = ttk.Frame(root)
    main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")  # Use grid layout

    # Configure grid to expand
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    main_frame.grid_rowconfigure(2, weight=1)
    main_frame.grid_columnconfigure(1, weight=1)

    # Operation Selection
    operation_var = tk.StringVar(value="Encrypt")  # Variable to store selected operation
    operation_label = ttk.Label(main_frame, text="Select Operation:")  # Label for operation selection
    operation_menu = ttk.Combobox(main_frame, textvariable=operation_var, values=["Encrypt", "Decrypt"])  # Dropdown menu for operation selection
    operation_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)  # Grid layout for label
    operation_menu.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)  # Grid layout for dropdown menu

    # Cipher Selection
    cipher_var = tk.StringVar(value="Caesar")  # Variable to store selected cipher
    cipher_label = ttk.Label(main_frame, text="Select Cipher:")  # Label for cipher selection
    cipher_menu = ttk.Combobox(main_frame, textvariable=cipher_var, values=["Caesar", "Vernam", "Base64", "RSA"])  # Dropdown menu for cipher selection
    cipher_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)  # Grid layout for label
    cipher_menu.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)  # Grid layout for dropdown menu

    # Plaintext Entry
    plaintext_label = ttk.Label(main_frame, text="Plaintext:")  # Label for plaintext entry
    plaintext_entry = tk.Text(main_frame, wrap=tk.WORD, height=4)  # Text widget for plaintext
    plaintext_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)  # Grid layout for label
    plaintext_entry.grid(row=2, column=1, padx=10, pady=5, sticky="nsew")  # Grid layout for text widget

    # Key Entry (Vernam)
    key_label = ttk.Label(main_frame, text="Key (for Vernam):")  # Label for key entry
    key_entry = ttk.Entry(main_frame)  # Entry widget for key

    # Shift Entry (Caesar)
    shift_label = ttk.Label(main_frame, text="Shift (for Caesar):")  # Label for shift entry
    shift_entry = ttk.Entry(main_frame)  # Entry widget for shift

    # RSA Key File Selector
    rsa_key_label = ttk.Label(main_frame, text="RSA Key File:")  # Label for RSA key file
    rsa_key_entry = ttk.Entry(main_frame)  # Entry widget for RSA key file
    rsa_key_button = ttk.Button(main_frame, text="Browse", command=lambda: browse_file(rsa_key_entry))  # Button to browse for RSA key file

    # Function to generate RSA key and save to file
    def generate_rsa_key():
        logging.debug("Generating RSA key")
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()
        with open("private_key.pem", "wb") as priv_file:
            priv_file.write(private_key)
        with open("public_key.pem", "wb") as pub_file:
            pub_file.write(public_key)
        messagebox.showinfo("RSA Key Generation", "RSA keys generated and saved as 'private_key.pem' and 'public_key.pem'.")
        logging.debug("RSA keys generated and saved")

    rsa_generate_button = ttk.Button(main_frame, text="Generate Key", command=generate_rsa_key)  # Button to generate RSA key

    # Result Text Box
    result_label = tk.Text(main_frame, wrap=tk.WORD, height=4, state='disabled')  # Text widget for result (disabled)
    result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")  # Grid layout for result text widget

    # Local callback function to update the result
    def local_submit_callback(operation, cipher_type, plaintext, key, shift):
        logging.debug(f"Local submit callback: Operation: {operation}, Cipher: {cipher_type}, Plaintext: {plaintext}, Key: {key}, Shift: {shift}")
        result = submit_callback(operation, cipher_type, plaintext, rsa_key_entry.get(), shift)  # Call the submit callback
        result_label.config(state='normal')  # Make the result text widget editable
        result_label.delete(1.0, tk.END)  # Clear the result text widget
        result_label.insert(tk.END, result)  # Insert the result
        result_label.config(state='disabled')  # Make the result text widget readonly again
        logging.debug(f"Result updated: {result}")

    # Function to update fields based on selected cipher and operation
    def update_fields(*args):
        cipher_type = cipher_var.get()  # Get the selected cipher
        operation = operation_var.get()  # Get the selected operation
        logging.debug(f"Updating fields: Cipher: {cipher_type}, Operation: {operation}")
        if cipher_type == "Caesar":
            shift_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)  # Show shift entry for Caesar
            shift_entry.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)  # Show shift entry for Caesar
            key_label.grid_forget()  # Hide key entry
            key_entry.grid_forget()  # Hide key entry
            rsa_key_label.grid_forget()  # Hide RSA key file entry
            rsa_key_entry.grid_forget()  # Hide RSA key file entry
            rsa_key_button.grid_forget()  # Hide RSA key file button
            rsa_generate_button.grid_forget()  # Hide RSA key generate button
        elif cipher_type == "Vernam":
            key_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)  # Show key entry for Vernam
            key_entry.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)  # Show key entry for Vernam
            shift_label.grid_forget()  # Hide shift entry
            shift_entry.grid_forget()  # Hide shift entry
            rsa_key_label.grid_forget()  # Hide RSA key file entry
            rsa_key_entry.grid_forget()  # Hide RSA key file entry
            rsa_key_button.grid_forget()  # Hide RSA key file button
            rsa_generate_button.grid_forget()  # Hide RSA key generate button
        elif cipher_type == "Base64":
            shift_label.grid_forget()  # Hide shift entry
            shift_entry.grid_forget()  # Hide shift entry
            key_label.grid_forget()  # Hide key entry
            key_entry.grid_forget()  # Hide key entry
            rsa_key_label.grid_forget()  # Hide RSA key file entry
            rsa_key_entry.grid_forget()  # Hide RSA key file entry
            rsa_key_button.grid_forget()  # Hide RSA key file button
            rsa_generate_button.grid_forget()  # Hide RSA key generate button
        elif cipher_type == "RSA":
            rsa_key_entry.delete(0, tk.END)  # Clear RSA key file entry
            if operation == "Encrypt":
                rsa_key_label.config(text="RSA Public Key File:")  # Update label text for public key
            else:
                rsa_key_label.config(text="RSA Private Key File:")  # Update label text for private key
            rsa_key_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)  # Show RSA key file entry
            rsa_key_entry.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)  # Show RSA key file entry
            rsa_key_button.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)  # Show RSA key file button
            rsa_generate_button.grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)  # Show RSA key generate button
            shift_label.grid_forget()  # Hide shift entry
            shift_entry.grid_forget()  # Hide shift entry
            key_label.grid_forget()  # Hide key entry
            key_entry.grid_forget()  # Hide key entry
        # Trigger callback with current values
        local_submit_callback(operation_var.get(), cipher_var.get(), plaintext_entry.get("1.0", tk.END).strip(), rsa_key_entry.get(), shift_entry.get())

    # Function to browse for RSA key file
    def browse_file(entry):
        file_path = filedialog.askopenfilename(filetypes=[("PEM files", "*.pem"), ("All files", "*.*")])
        if file_path:
            entry.delete(0, tk.END)
            entry.insert(0, file_path)
        logging.debug(f"File selected: {file_path}")

    # Trace changes in cipher and operation selection
    cipher_var.trace("w", update_fields)  # Update fields when cipher changes
    operation_var.trace("w", update_fields)  # Update fields when operation changes
    plaintext_entry.bind("<KeyRelease>", lambda event: local_submit_callback(operation_var.get(), cipher_var.get(), plaintext_entry.get("1.0", tk.END).strip(), rsa_key_entry.get(), shift_entry.get()))  # Update result on plaintext change
    rsa_key_entry.bind("<KeyRelease>", lambda event: local_submit_callback(operation_var.get(), cipher_var.get(), plaintext_entry.get("1.0", tk.END).strip(), rsa_key_entry.get(), shift_entry.get()))  # Update result on RSA key change

    update_fields()  # Initialize the fields based on the default cipher

    # Frequency Analysis Button
    freq_analysis_button = ttk.Button(main_frame, text="Frequency Analysis", command=lambda: freq_analysis_callback(plaintext_entry.get("1.0", tk.END).strip()))  # Button for frequency analysis
    freq_analysis_button.grid(row=7, column=0, padx=10, pady=5, sticky=tk.W)  # Grid layout for button

    # Function to show encryption info
    def show_encryption_info():
        logging.debug("Encryption info button clicked")
        info_text = encryption_info_callback()
        info_window = tk.Toplevel(root)
        info_window.title("Encryption Info")
        info_window.geometry("400x300")
        info_label = ttk.Label(info_window, text=info_text, justify=tk.LEFT)
        info_label.pack(padx=10, pady=10)

    # Encryption Info Button
    encryption_info_button = ttk.Button(main_frame, text="Encryption Info", command=show_encryption_info)
    encryption_info_button.grid(row=7, column=1, padx=10, pady=5, sticky=tk.W)  # Grid layout for button

    logging.debug("GUI initialized")
    return root, result_label  # Return the root window and result label