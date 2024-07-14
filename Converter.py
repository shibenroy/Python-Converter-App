import customtkinter as ctk
from tkinter import filedialog, messagebox, Tk, StringVar
from PIL import Image, ImageTk

def select_image():
    global file_path, selected_image_label, img_label
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.webp;*.jpg;*.jpeg;*.bmp;*.tiff")])
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((300, 300))  # Resize for display
        img = ImageTk.PhotoImage(img)
        img_label.configure(image=img)
        img_label.image = img
        selected_image_label.config(text=f"Selected Image: {file_path.split('/')[-1]}")

def convert_image(output_format):
    if not file_path:
        messagebox.showwarning("Warning", "Please select an image first.")
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
root.geometry("800x400")
root.configure(bg="#80C7C5")

# Set the window icon (make sure you have 'logo.ico' in the same directory or provide the correct path)
root.iconbitmap('logo.ico')

# Load the Overpass font
overpass_font = ("Overpass", 16)
overpass_font_large = ("Overpass", 24)

# Use customtkinter for the rest of the UI
app = ctk.CTkFrame(root, corner_radius=15)
app.pack(fill="both", expand=True, padx=20, pady=20)

# Left panel for image selection
left_panel = ctk.CTkFrame(app, width=400, corner_radius=15)
left_panel.pack(side="left", fill="both", expand=True, padx=10, pady=10)

# Right panel for conversion options
right_panel = ctk.CTkFrame(app, width=200, corner_radius=15)
right_panel.pack(side="right", fill="both", expand=False, padx=10, pady=10)

# Add a title label on the left panel
title_label = ctk.CTkLabel(left_panel, text="Image Format Converter", font=overpass_font_large)
title_label.pack(pady=10)

# Button to select image
select_button = ctk.CTkButton(left_panel, text="Select Image", command=select_image, font=overpass_font, width=200)
select_button.pack(pady=10)

# Label to show selected image path
selected_image_label = ctk.CTkLabel(left_panel, text="No image selected", font=overpass_font)
selected_image_label.pack(pady=10)

# Placeholder for selected image display
img_label = ctk.CTkLabel(left_panel, text="", width=300, height=300, bg_color="#80C7C5")
img_label.pack(pady=10)

# Conversion options in the right panel
convert_label = ctk.CTkLabel(right_panel, text="Convert image", font=overpass_font_large)
convert_label.pack(pady=10)

# Conversion buttons
convert_buttons = [
    ("Convert to PNG", "png"),
    ("Convert to JPEG", "jpeg"),
    ("Convert to BMP", "bmp"),
    ("Convert to TIFF", "tiff"),
    ("Convert to PDF", "pdf")
]

for text, fmt in convert_buttons:
    btn = ctk.CTkButton(right_panel, text=text, command=lambda f=fmt: convert_image(f), font=overpass_font, width=200)
    btn.pack(pady=5)

# Global variable to store the file path
file_path = None

# Run the application
root.mainloop()
