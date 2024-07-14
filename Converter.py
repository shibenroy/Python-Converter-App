import customtkinter as ctk
from tkinter import filedialog, messagebox, Tk, StringVar
from PIL import Image

def select_image():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.webp;*.jpg;*.jpeg;*.bmp;*.tiff")])
    if file_path:
        selected_image_label.config(text=f"Selected Image: {file_path.split('/')[-1]}")

def convert_image():
    if not file_path:
        messagebox.showwarning("Warning", "Please select an image first.")
        return

    output_format = format_var.get()
    if not output_format:
        messagebox.showwarning("Warning", "Please select an output format.")
        return

    try:
        img = Image.open(file_path)
        save_path = filedialog.asksaveasfilename(defaultextension=f".{output_format}", filetypes=[(f"{output_format.upper()} files", f"*.{output_format}")])
        if save_path:
            img.save(save_path, output_format.upper())
            messagebox.showinfo("Success", f"Image saved as {save_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Initialize the main window using standard Tkinter for root window configuration
root = Tk()
root.title("Image Format Converter")
root.geometry("500x300")
root.configure(bg="white")

# Set the window icon (make sure you have 'logo.ico' in the same directory or provide the correct path)
root.iconbitmap('Logo.ico')

# Use customtkinter for the rest of the UI
app = ctk.CTkFrame(root, corner_radius=15)
app.pack(fill="both", expand=True, padx=20, pady=20)

# Add a title label
title_label = ctk.CTkLabel(app, text="Image Format Converter", font=("Arial", 20))
title_label.pack(pady=10)

# Button to select image
select_button = ctk.CTkButton(app, text="Select Image", command=select_image, width=200)
select_button.pack(pady=10)

# Label to show selected image path
selected_image_label = ctk.CTkLabel(app, text="No image selected", font=("Arial", 12))
selected_image_label.pack(pady=10)

# Add a label for output format
format_label = ctk.CTkLabel(app, text="Select Output Format:", font=("Arial", 14))
format_label.pack(pady=10)

# Add a dropdown menu for format selection
format_var = StringVar()
format_dropdown = ctk.CTkOptionMenu(app, variable=format_var, values=["png", "jpeg", "bmp", "tiff"], width=200)
format_dropdown.pack(pady=10)

# Add a button to trigger the conversion
convert_button = ctk.CTkButton(app, text="Convert Image", command=convert_image, width=200)
convert_button.pack(pady=20)

# Global variable to store the file path
file_path = None

# Run the application
root.mainloop()
