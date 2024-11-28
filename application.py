import logging
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from Crypto.PublicKey import RSA

class Application:
    def __init__(self, submit_callback, freq_analysis_callback, encryption_info_callback):
        self.submit_callback = submit_callback
        self.freq_analysis_callback = freq_analysis_callback
        self.encryption_info_callback = encryption_info_callback
        self.root = tk.Tk()
        self.result_label = None
        self.setup_logging()
        self.create_gui()

    def setup_logging(self):
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    def create_gui(self):
        logging.debug("Initializing GUI")
        self.root.title('Encryption Program')
        self.root.geometry("600x400")

        main_frame = ttk.Frame(self.root)
        main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(2, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

        operation_var = tk.StringVar(value="Encrypt")
        operation_label = ttk.Label(main_frame, text="Select Operation:")
        operation_menu = ttk.Combobox(main_frame, textvariable=operation_var, values=["Encrypt", "Decrypt"])
        operation_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        operation_menu.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

        cipher_var = tk.StringVar(value="Caesar")
        cipher_label = ttk.Label(main_frame, text="Select Cipher:")
        cipher_menu = ttk.Combobox(main_frame, textvariable=cipher_var, values=["Caesar", "Vernam", "Base64", "RSA"])
        cipher_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        cipher_menu.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        plaintext_label = ttk.Label(main_frame, text="Plaintext:")
        plaintext_entry = tk.Text(main_frame, wrap=tk.WORD, height=4)
        plaintext_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        plaintext_entry.grid(row=2, column=1, padx=10, pady=5, sticky="nsew")

        key_label = ttk.Label(main_frame, text="Key (for Vernam):")
        key_entry = ttk.Entry(main_frame)

        shift_label = ttk.Label(main_frame, text="Shift (for Caesar):")
        shift_entry = ttk.Entry(main_frame)

        rsa_key_label = ttk.Label(main_frame, text="RSA Key File:")
        rsa_key_entry = ttk.Entry(main_frame)
        rsa_key_button = ttk.Button(main_frame, text="Browse", command=lambda: self.browse_file(rsa_key_entry))

        rsa_generate_button = ttk.Button(main_frame, text="Generate Key", command=self.generate_rsa_key)

        self.result_label = tk.Text(main_frame, wrap=tk.WORD, height=4, state='disabled')
        self.result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

        def local_submit_callback(operation, cipher_type, plaintext, key, shift):
            if cipher_type == "Vernam" and not key:
                result = "Key cannot be empty for Vernam Cipher"
                logging.error(result)
            else:
                logging.debug(f"Local submit callback: Operation: {operation}, Cipher: {cipher_type}, Plaintext: {plaintext}, Key: {key}, Shift: {shift}")
                result = self.submit_callback(operation, cipher_type, plaintext, key, shift)
            self.result_label.config(state='normal')
            self.result_label.delete(1.0, tk.END)
            self.result_label.insert(tk.END, result)
            self.result_label.config(state='disabled')
            logging.debug(f"Result updated: {result}")

        def update_fields(*args):
            cipher_type = cipher_var.get()
            operation = operation_var.get()
            logging.debug(f"Updating fields: Cipher: {cipher_type}, Operation: {operation}")
            if cipher_type == "Caesar":
                shift_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
                shift_entry.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)
                key_label.grid_forget()
                key_entry.grid_forget()
                rsa_key_label.grid_forget()
                rsa_key_entry.grid_forget()
                rsa_key_button.grid_forget()
                rsa_generate_button.grid_forget()
            elif cipher_type == "Vernam":
                key_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
                key_entry.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)
                shift_label.grid_forget()
                shift_entry.grid_forget()
                rsa_key_label.grid_forget()
                rsa_key_entry.grid_forget()
                rsa_key_button.grid_forget()
                rsa_generate_button.grid_forget()
            elif cipher_type == "Base64":
                shift_label.grid_forget()
                shift_entry.grid_forget()
                key_label.grid_forget()
                key_entry.grid_forget()
                rsa_key_label.grid_forget()
                rsa_key_entry.grid_forget()
                rsa_key_button.grid_forget()
                rsa_generate_button.grid_forget()
            elif cipher_type == "RSA":
                rsa_key_entry.delete(0, tk.END)
                rsa_key_label.config(text="RSA Public Key File:" if operation == "Encrypt" else "RSA Private Key File:")
                rsa_key_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
                rsa_key_entry.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)
                rsa_key_button.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)
                rsa_generate_button.grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)
                shift_label.grid_forget()
                shift_entry.grid_forget()
                key_label.grid_forget()
                key_entry.grid_forget()
            local_submit_callback(operation_var.get(), cipher_var.get(), plaintext_entry.get("1.0", tk.END).strip(), key_entry.get(), shift_entry.get())

        cipher_var.trace("w", update_fields)
        operation_var.trace("w", update_fields)
        plaintext_entry.bind("<KeyRelease>", lambda event: local_submit_callback(operation_var.get(), cipher_var.get(), plaintext_entry.get("1.0", tk.END).strip(), key_entry.get(), shift_entry.get()))
        key_entry.bind("<KeyRelease>", lambda event: local_submit_callback(operation_var.get(), cipher_var.get(), plaintext_entry.get("1.0", tk.END).strip(), key_entry.get(), shift_entry.get()))
        rsa_key_entry.bind("<KeyRelease>", lambda event: local_submit_callback(operation_var.get(), cipher_var.get(), plaintext_entry.get("1.0", tk.END).strip(), rsa_key_entry.get(), shift_entry.get()))

        update_fields()

        freq_analysis_button = ttk.Button(main_frame, text="Frequency Analysis", command=lambda: self.freq_analysis_callback(plaintext_entry.get("1.0", tk.END).strip()))
        freq_analysis_button.grid(row=7, column=0, padx=10, pady=5, sticky=tk.W)

        encryption_info_button = ttk.Button(main_frame, text="Encryption Info", command=self.show_encryption_info)
        encryption_info_button.grid(row=7, column=1, padx=10, pady=5, sticky=tk.W)

        logging.debug("GUI initialized")

    def browse_file(self, entry):
        file_path = filedialog.askopenfilename(filetypes=[("PEM files", "*.pem"), ("All files", "*.*")])
        if file_path:
            entry.delete(0, tk.END)
            entry.insert(0, file_path)
        logging.debug(f"File selected: {file_path}")

    def generate_rsa_key(self):
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

    def show_encryption_info(self):
        logging.debug("Encryption info button clicked")
        info_text = self.encryption_info_callback()
        info_window = tk.Toplevel(self.root)
        info_window.title("Encryption Info")
        info_window.geometry("400x300")
        info_label = ttk.Label(info_window, text=info_text, justify=tk.LEFT)
        info_label.pack(padx=10, pady=10)

    def run(self):
        self.root.mainloop()