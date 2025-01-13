# OCR App 🚀  
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)  
[![Tesseract](https://img.shields.io/badge/Tesseract-OCR-green)](https://github.com/tesseract-ocr/tesseract)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
[![Docker](https://img.shields.io/badge/Docker-Supported-blue)](https://www.docker.com/)

A Python-based Optical Character Recognition (OCR) application using Tesseract OCR and OpenCV, featuring a user-friendly GUI with batch processing capabilities.

---

## 🌟 Features  
- 📷 **Extract text from images**: Supports multiple formats (JPG, PNG, BMP, etc.).  
- 🔄 **Batch Processing**: Process multiple images at once.  
- 🖼️ **GUI**: Intuitive graphical interface built with Tkinter.  
- 🐋 **Docker Support**: Simplified deployment using Docker.  
- 🌍 **Language Support**: OCR in over 100 languages.

---

## 📖 Table of Contents  
1. [Getting Started](#getting-started)  
2. [Prerequisites](#prerequisites)  
3. [Installation](#installation)  
   - [Using Python](#using-python)  
   - [Using Docker](#using-docker)  
4. [Collaborate with Me!](#collaborate-with-me)

---

## Getting Started 

To get started with the OCR App, follow these steps:
  
## 🛠️ Prerequisites

Before running this project, make sure you have the following installed on your system:

- **Python 3.9+**: Download and install Python from [here](https://www.python.org/downloads/).
- **Tesseract OCR**: Install Tesseract OCR, which is required for text recognition.  
  - **Windows**: You can download the installer from [here](https://github.com/UB-Mannheim/tesseract/wiki).
  - **Linux**: Use your package manager to install it, e.g.,  
    ```bash
    sudo apt install tesseract-ocr
    ```
  - **Mac**: Use Homebrew to install it, e.g.,  
    ```bash
    brew install tesseract
    ```
- **Xming or Equivalent X Server**:  
  If you are running the project in an environment like **WSL** or **Docker containers** without native display support, you need an X server for GUI rendering.  
  - **Windows**: Install [Xming](https://sourceforge.net/projects/xming/) or [VcXsrv](https://sourceforge.net/projects/vcxsrv/).
  - **Linux/Mac**: X servers like **XQuartz** or native X server installations are often pre-installed or easily installable.

 Once installed:
 - Start Xming (or your chosen X server) before running the application.
 - For Docker: Use the `DISPLAY` environment variable, e.g.,  
   ```bash
   docker run -e DISPLAY=host.docker.internal:0 -it ocr-app
   ```
 - For WSL: Configure the `DISPLAY` variable with your host IP, e.g.,  
   ```bash
   export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}'):0
   ```

---

## 🚀 Installation  

### Using Python  
1. Clone the repository:  
   ```bash
   git clone https://github.com/007HSingh/OCR-App.git
   cd OCR-App
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the application:
   ```bash
   python ocr_app.py

### Using Docker
1. Build the Docker image:
   ```bash
   docker build -t ocr-app .
2. Run the container:
   ```bash
   docker run -it --rm ocr-app
   
## 📝 Collaborate with Me!  

I am always open to collaborating and refining the UI of the app, as well as adding new features. If you have ideas or suggestions for improvement, feel free to open an issue or submit a pull request. Together, we can make this project even better!

### **How You Can Contribute:**
- **UI Enhancements**: Help make the user interface more intuitive and modern.
- **Feature Development**: Contribute new features or improve existing ones.

---

## 📧 Contact Me  
You can reach out to me via email or connect with me on LinkedIn:

- Email: [singhharsh25032008@gmail.com](mailto:singhharsh25032008@gmail.com)
- LinkedIn: [Harsh Singh](https://www.linkedin.com/in/harsh-singh-iiitkalyani)
