import logging
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class Application:
    """Class to create and manage the GUI for the Encryption Program."""
    
    def __init__(self, submit_callback, freq_analysis_callback, encryption_info_callback):
        """Initialize with callback functions and setup the GUI."""
        self.submit_callback = submit_callback
        self.freq_analysis_callback = freq_analysis_callback
        self.encryption_info_callback = encryption_info_callback
        self.root = tk.Tk()
        self.result_label = None
        self.setup_logging()
        self.create_gui()

    def setup_logging(self):
        """Setup the logging configuration."""
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def create_gui(self):
        """Create and layout the GUI components."""
        logging.info("Initializing GUI")
        self.root.title('Encryption Program')
        self.root.geometry("600x400")

        main_frame = ttk.Frame(self.root)
        main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(2, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

        # Operation Selection
        operation_var = tk.StringVar(value="Encrypt")
        operation_label = ttk.Label(main_frame, text="Select Operation:")
        operation_menu = ttk.Combobox(main_frame, textvariable=operation_var, values=["Encrypt", "Decrypt"])
        operation_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        operation_menu.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

        # Cipher Selection
        cipher_var = tk.StringVar(value="Caesar")
        cipher_label = ttk.Label(main_frame, text="Select Cipher:")
        cipher_menu = ttk.Combobox(main_frame, textvariable=cipher_var, values=["Caesar", "Vernam"])
        cipher_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        cipher_menu.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        # Plaintext Entry
        plaintext_label = ttk.Label(main_frame, text="Plaintext:")
        plaintext_entry = tk.Text(main_frame, wrap=tk.WORD, height=4)
        plaintext_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        plaintext_entry.grid(row=2, column=1, padx=10, pady=5, sticky="nsew")

        # Key and Shift Entries
        key_label = ttk.Label(main_frame, text="Key (for Vernam):")
        key_entry = ttk.Entry(main_frame)

        shift_label = ttk.Label(main_frame, text="Shift (for Caesar):")
        shift_entry = ttk.Entry(main_frame)

        # Result Display
        self.result_label = tk.Text(main_frame, wrap=tk.WORD, height=4, state='disabled')
        self.result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

        def local_submit_callback(operation: str, cipher_type: str, plaintext: str, key: str, shift: str):
            """Local callback to handle submit actions and update the result label."""
            if cipher_type == "Vernam" and not key:
                result = "Key cannot be empty for Vernam Cipher"
                logging.error(result)
            else:
                logging.info(f"Processing {operation} with {cipher_type} Cipher")
                result = self.submit_callback(operation, cipher_type, plaintext, key, shift)
            self.result_label.config(state='normal')
            self.result_label.delete(1.0, tk.END)
            self.result_label.insert(tk.END, result)
            self.result_label.config(state='disabled')
            logging.info(f"Result updated: {result}")

        def update_fields(*args):
            """Update the input fields based on the selected cipher and operation."""
            cipher_type = cipher_var.get()
            operation = operation_var.get()
            logging.info(f"Updating fields for {cipher_type} Cipher and {operation} operation")
            if cipher_type == "Caesar":
                shift_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
                shift_entry.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)
                key_label.grid_forget()
                key_entry.grid_forget()
            elif cipher_type == "Vernam":
                key_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
                key_entry.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)
                shift_label.grid_forget()
                shift_entry.grid_forget()
            local_submit_callback(operation_var.get(), cipher_var.get(), plaintext_entry.get("1.0", tk.END).strip(), key_entry.get(), shift_entry.get())

        # Trace variable changes to update GUI dynamically
        cipher_var.trace("w", update_fields)
        operation_var.trace("w", update_fields)
        plaintext_entry.bind("<KeyRelease>", lambda event: local_submit_callback(operation_var.get(), cipher_var.get(), plaintext_entry.get("1.0", tk.END).strip(), key_entry.get(), shift_entry.get()))
        key_entry.bind("<KeyRelease>", lambda event: local_submit_callback(operation_var.get(), cipher_var.get(), plaintext_entry.get("1.0", tk.END).strip(), key_entry.get(), shift_entry.get()))

        update_fields()

        # Frequency Analysis Button
        freq_analysis_button = ttk.Button(main_frame, text="Frequency Analysis", command=lambda: self.freq_analysis_callback(plaintext_entry.get("1.0", tk.END).strip(), self.result_label.get("1.0", tk.END).strip()))
        freq_analysis_button.grid(row=7, column=0, padx=10, pady=5, sticky=tk.W)

        # Encryption Info Button
        encryption_info_button = ttk.Button(main_frame, text="Encryption Info", command=self.show_encryption_info)
        encryption_info_button.grid(row=7, column=1, padx=10, pady=5, sticky=tk.W)

        logging.info("GUI initialized")

    def browse_file(self, entry: ttk.Entry):
        """Open a file dialog to select a key file and update the entry widget."""
        file_path = filedialog.askopenfilename(filetypes=[("PEM files", "*.pem"), ("All files", "*.*")])
        if file_path:
            entry.delete(0, tk.END)
            entry.insert(0, file_path)
        logging.info(f"File selected: {file_path}")

    def show_encryption_info(self):
        """Display information about symmetric and asymmetric encryption in a new window."""
        logging.info("Encryption info button clicked")
        info_text = self.encryption_info_callback()
        info_window = tk.Toplevel(self.root)
        info_window.title("Encryption Info")
        info_window.geometry("400x300")
        info_label = ttk.Label(info_window, text=info_text, justify=tk.LEFT)
        info_label.pack(padx=10, pady=10)

    def run(self):
        """Start the GUI event loop."""
        logging.info("Running application")
        self.root.mainloop()