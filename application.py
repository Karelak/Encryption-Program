import tkinter as tk
from tkinter import ttk

# Function to create the GUI
def create_gui(submit_callback, freq_analysis_callback):
    root = tk.Tk()
    root.title('Encryption Program')  # Set the window title
    root.geometry("600x400")  # Set the window size

    # Create a frame to center the content
    main_frame = ttk.Frame(root)
    main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Center the frame

    # Operation Selection
    operation_var = tk.StringVar(value="Encrypt")  # Variable to store selected operation
    operation_label = ttk.Label(main_frame, text="Select Operation:")  # Label for operation selection
    operation_menu = ttk.Combobox(main_frame, textvariable=operation_var, values=["Encrypt", "Decrypt"])  # Dropdown menu for operation selection
    operation_label.pack(anchor=tk.CENTER, padx=10, pady=5)  # Pack the label
    operation_menu.pack(anchor=tk.CENTER, padx=10, pady=5)  # Pack the dropdown menu

    # Cipher Selection
    cipher_var = tk.StringVar(value="Caesar")  # Variable to store selected cipher
    cipher_label = ttk.Label(main_frame, text="Select Cipher:")  # Label for cipher selection
    cipher_menu = ttk.Combobox(main_frame, textvariable=cipher_var, values=["Caesar", "Vernam", "Base64"])  # Dropdown menu for cipher selection
    cipher_label.pack(anchor=tk.CENTER, padx=10, pady=5)  # Pack the label
    cipher_menu.pack(anchor=tk.CENTER, padx=10, pady=5)  # Pack the dropdown menu

    # Plaintext Entry
    plaintext_label = ttk.Label(main_frame, text="Plaintext:")  # Label for plaintext entry
    plaintext_entry = ttk.Entry(main_frame)  # Entry widget for plaintext
    plaintext_label.pack(anchor=tk.CENTER, padx=10, pady=5)  # Pack the label
    plaintext_entry.pack(anchor=tk.CENTER, padx=10, pady=5)  # Pack the entry widget

    # Key Entry (Vernam)
    key_label = ttk.Label(main_frame, text="Key (for Vernam):")  # Label for key entry
    key_entry = ttk.Entry(main_frame)  # Entry widget for key

    # Shift Entry (Caesar)
    shift_label = ttk.Label(main_frame, text="Shift (for Caesar):")  # Label for shift entry
    shift_entry = ttk.Entry(main_frame)  # Entry widget for shift

    # Result Text Box
    result_label = ttk.Entry(main_frame, state='readonly')  # Entry widget for result (readonly)
    result_label.pack(anchor=tk.CENTER, padx=10, pady=5)  # Pack the result entry widget

    # Local callback function to update the result
    def local_submit_callback(operation, cipher_type, plaintext, key, shift):
        result = submit_callback(operation, cipher_type, plaintext, key, shift)  # Call the submit callback
        result_label.config(state='normal')  # Make the result entry widget editable
        result_label.delete(0, tk.END)  # Clear the result entry widget
        result_label.insert(0, result)  # Insert the result
        result_label.config(state='readonly')  # Make the result entry widget readonly again

    # Function to update fields based on selected cipher
    def update_fields(*args):
        cipher_type = cipher_var.get()  # Get the selected cipher
        if cipher_type == "Caesar":
            shift_label.pack(anchor=tk.CENTER, padx=10, pady=5)  # Show shift entry for Caesar
            shift_entry.pack(anchor=tk.CENTER, padx=10, pady=5)  # Show shift entry for Caesar
            key_label.pack_forget()  # Hide key entry
            key_entry.pack_forget()  # Hide key entry
        elif cipher_type == "Vernam":
            key_label.pack(anchor=tk.CENTER, padx=10, pady=5)  # Show key entry for Vernam
            key_entry.pack(anchor=tk.CENTER, padx=10, pady=5)  # Show key entry for Vernam
            shift_label.pack_forget()  # Hide shift entry
            shift_entry.pack_forget()  # Hide shift entry
        elif cipher_type == "Base64":
            shift_label.pack_forget()  # Hide shift entry
            shift_entry.pack_forget()  # Hide shift entry
            key_label.pack_forget()  # Hide key entry
            key_entry.pack_forget()  # Hide key entry
        # Trigger callback with current values
        local_submit_callback(operation_var.get(), cipher_var.get(), plaintext_entry.get(), key_entry.get(), shift_entry.get())

    # Trace changes in cipher and operation selection
    cipher_var.trace("w", update_fields)  # Update fields when cipher changes
    operation_var.trace("w", update_fields)  # Update fields when operation changes
    plaintext_entry.bind("<KeyRelease>", lambda event: local_submit_callback(operation_var.get(), cipher_var.get(), plaintext_entry.get(), key_entry.get(), shift_entry.get()))  # Update result on plaintext change
    key_entry.bind("<KeyRelease>", lambda event: local_submit_callback(operation_var.get(), cipher_var.get(), plaintext_entry.get(), key_entry.get(), shift_entry.get()))  # Update result on key change
    shift_entry.bind("<KeyRelease>", lambda event: local_submit_callback(operation_var.get(), cipher_var.get(), plaintext_entry.get(), key_entry.get(), shift_entry.get()))  # Update result on shift change

    update_fields()  # Initialize the fields based on the default cipher

    # Frequency Analysis Button
    freq_analysis_button = ttk.Button(main_frame, text="Frequency Analysis", command=lambda: freq_analysis_callback(plaintext_entry.get()))  # Button for frequency analysis
    freq_analysis_button.pack(anchor=tk.CENTER, padx=10, pady=5)  # Pack the button

    return root, result_label  # Return the root window and result label