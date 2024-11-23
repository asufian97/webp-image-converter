# WebP Image Converter

This project is a simple **web-based tool** built with Flask to convert images (JPEG/PNG) to WebP format. It also supports converting to PNG and JPEG. Users can upload a single image or multiple images for conversion, and multiple images will be provided as a ZIP file for convenience.

## Features

- **Convert Single or Multiple Images**: Convert JPEG/PNG images to WebP, PNG, or JPEG format.
- **Flexible Output Options**: Users can adjust image dimensions (width and height) and quality.
- **Dynamic Download**: Single images are downloaded directly, while multiple images are packaged into a ZIP file.
- **Preview Uploaded Images**: Users can preview selected images before conversion.

## Tech Stack

- **Backend**: Python 3, Flask
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Dependencies**: Flask, Pillow (for image processing)

## Installation

To set up the project locally, follow these steps:

### Prerequisites

- Python 3.7+
- `pip` (Python package installer)
- Git

### Steps to Set Up Locally

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/asufian97/webp-image-converter.git
Navigate to the Project Directory:

bash
Copy code
cd webp-image-converter
Create a Virtual Environment: It is recommended to create a virtual environment to keep dependencies isolated.

bash
Copy code
python -m venv venv
Activate the virtual environment:

Windows:
bash
Copy code
venv\Scripts\activate
macOS/Linux:
bash
Copy code
source venv/bin/activate
Install the Requirements: Install the necessary packages using requirements.txt:

bash
Copy code
pip install -r requirements.txt
Running the Application
Once you have installed the dependencies, you can run the Flask application:

Run the Application:

bash
Copy code
python app.py
Access the Web App: Open your browser and go to:

arduino
Copy code
http://127.0.0.1:5000/
The web interface will allow you to upload images and convert them as needed.

Usage
Image Conversion
Upload Images: Use the "Select Images" button to upload one or more images (JPEG/PNG).
Configure Output Settings:
Select Output Format: WebP, PNG, or JPEG.
Adjust Dimensions (Optional): Set width and height to resize the images.
Adjust Quality (Optional): Set the quality level (default is 80).
Preview: Uploaded images will appear as previews before conversion.
Convert: Click on the "Convert" button to process and download the images.
For a single image, it will download directly.
For multiple images, the download will be in a ZIP file.
Project Structure
bash
Copy code
webp-image-converter/
├── app.py                # Flask application logic
├── templates/
│   └── index.html        # Frontend HTML page for uploading images
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
└── download_count.json   # (Optional) Persistent download count file
Dependencies
Flask: For building the web server.
Pillow: For handling image conversion.
Bootstrap: For styling the frontend.
Example .gitignore
It is recommended to include the following .gitignore to keep unwanted files out of your repository:

bash
Copy code
# Ignore virtual environments
venv/
.venv/

# Ignore Python cache files
__pycache__/
*.pyc

# Ignore system files
.DS_Store

# Ignore IDE files
.vscode/
*.sublime-project
*.sublime-workspace
Future Improvements
User Authentication: Allow users to create accounts to store their conversion history.
Support for More Formats: Add support for other image formats like GIF, BMP, etc.
Cloud Deployment: Deploy the app on a cloud service like Heroku or AWS.
Contribution
Feel free to submit pull requests or open issues if you want to contribute to the project or suggest new features.

How to Contribute
Fork the Repository.
Create a Feature Branch (git checkout -b feature-name).
Commit Your Changes (git commit -m 'Add some feature').
Push to Your Branch (git push origin feature-name).
Create a Pull Request.
License
This project is licensed under the MIT License. You are free to use, modify, and distribute this project as long as you include the original copyright notice.

Contact
If you have any questions or suggestions, feel free to reach out!

GitHub: asufian97
Email: sufianwp97dot@gmail.com
vbnet
Copy code


You can copy and paste this directly into your `README.md` file. Update the **contact information** (email) as needed. Let me know if you have more questions! 😊
