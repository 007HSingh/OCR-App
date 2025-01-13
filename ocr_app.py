import cv2
import pytesseract
from tkinter import Tk, Label, Button, Text, filedialog, Scrollbar, PhotoImage, Canvas, Toplevel, OptionMenu, StringVar
from PIL import Image, ImageTk

# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# List of available languages in Tesseract (example: 'eng' for English, 'spa' for Spanish, etc.)
LANGUAGES = ['eng', 'hin', 'ind']  # You can add more languages as per your needs

def preprocess_image(image_path):
    """Refined preprocessing of the image."""
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Step 1: Grayscale Conversion
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 2: Noise Removal
    denoised = cv2.medianBlur(gray, 3)

    # Step 3: Thresholding (Otsu's method)
    _, binary = cv2.threshold(denoised, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Step 4: Optional Scaling
    scaled = cv2.resize(binary, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

    return scaled

def perform_ocr(image_path, language):
    """Perform OCR on the given image using the selected language."""
    # Preprocess the image
    preprocessed_image = preprocess_image(image_path)
    
    # Perform OCR on the preprocessed image
    text = pytesseract.image_to_string(preprocessed_image, lang = language)
    return text

def save_text(ocr_text, output_file):
    """Save the OCR text to a file."""
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "w") as f:
            f.write(ocr_text)

def batch_process_images():
    """Process multiple images in batch."""
    file_paths = filedialog.askopenfilenames(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if not file_paths:
        return

    # Get the selected OCR language from the dropdown
    selected_language = language_var.get()

    # String to hold the combined OCR results
    combined_text = ""

    # Process each image in batch
    for file_path in file_paths:
        ocr_text = perform_ocr(file_path, selected_language)
        combined_text += f"--- OCR Result for {file_path} ---\n"
        combined_text += ocr_text + "\n\n"

    # Save the combined results
    output_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if output_file:
        save_text(combined_text, output_file)

def select_file():
    """Open a file dialog to select an image and perform OCR."""
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if not file_path:
        return

    # Get the selected OCR language from the dropdown
    selected_language = language_var.get()

    # Display the selected image
    display_image(file_path)

    # Perform OCR and display the result
    ocr_text = perform_ocr(file_path, selected_language)
    display_text(ocr_text)

def display_image(image_path):
    """Display the selected image in the GUI."""
    img = Image.open(image_path)
    img.thumbnail((400, 400))  # Resize for display
    img_tk = ImageTk.PhotoImage(img)
    
    # Clear previous image
    canvas.delete("all")
    canvas.create_image(0, 0, anchor="nw", image=img_tk)
    canvas.image = img_tk  # Store reference to avoid garbage collection

def display_text(ocr_text):
    """Display the OCR result in a popup."""
    popup = Toplevel(root)
    popup.title("OCR Result")
    popup.geometry("600x400")

    text_area = Text(popup, wrap="word", font=("Arial", 12))
    text_area.insert("1.0", ocr_text)
    text_area.pack(expand=True, fill="both", padx=10, pady=10)

    scrollbar = Scrollbar(popup, command=text_area.yview)
    scrollbar.pack(side="right", fill="y")
    text_area.config(yscrollcommand=scrollbar.set)

    # Add Save and Close Buttons
    save_btn = Button(popup, text="Save Text", command=lambda: save_text(ocr_text), font=("Arial", 12))
    save_btn.pack(side="left", padx=10, pady=10)

    close_btn = Button(popup, text="Close", command=popup.destroy, font=("Arial", 12))
    close_btn.pack(side="right", padx=10, pady=10)


# Create the main application window
root = Tk()
root.title("OCR Application")
root.geometry("600x600")

# Create a variable to hold the selected language
language_var = StringVar()
language_var.set(LANGUAGES[0])  # Default to English ('eng')

# GUI Elements
Label(root, text="OCR Application", font=("Arial", 20)).pack(pady=10)

# Add the language dropdown menu
language_menu = OptionMenu(root, language_var, *LANGUAGES)
language_menu.config(font=("Arial", 14))
language_menu.pack(pady=20)

Button(root, text="Select Single Image", command=select_file, font=("Arial", 14)).pack(pady=20)

Button(root, text="Batch Process Images", command=batch_process_images, font=("Arial", 14)).pack(pady=20)

canvas = Canvas(root, width=400, height=400, bg="gray")
canvas.pack(pady=10)

# Run the application
root.mainloop()
