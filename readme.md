# WebP Image Converter

    **WebP Image Converter** is a simple **web-based tool** built using Flask that helps you convert images between formats such as JPEG, PNG, and WebP. It supports both single image conversion and bulk conversion, with the option to download multiple images as a ZIP file.

    ## ✨ Features

    - **Convert Single or Multiple Images**: Convert JPEG/PNG images to WebP, PNG, or JPEG format with ease.
    - **Flexible Output Settings**: Customize the image dimensions (width and height) and quality level.
    - **Convenient Download Options**: Direct download for a single image or ZIP packaging for multiple images.
    - **Image Preview**: Preview uploaded images before starting the conversion process.

    ## 🛠️ Tech Stack

    - **Backend**: Python 3, Flask
    - **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
    - **Dependencies**: Flask, Pillow (image processing library)

    ## 🚀 Installation

    Follow these instructions to set up the project locally.

    ### Prerequisites

    - Python 3.7+
    - `pip` (Python package installer)
    - Git

    ### Steps to Set Up Locally

    1. **Clone the Repository**:
       ```bash
       git clone https://github.com/asufian97/webp-image-converter.git
       ```
    2. **Navigate to the Project Directory**:
       ```bash
       cd webp-image-converter
       ```
    3. **Create a Virtual Environment**:
       It is recommended to create a virtual environment to isolate dependencies.
       ```bash
       python -m venv venv
       ```
    4. **Activate the Virtual Environment**:

       - **Windows**:
         ```bash
         venv\Scripts\activate
         ```
       - **macOS/Linux**:
         ```bash
         source venv/bin/activate
         ```
    5. **Install the Requirements**:
       Install the necessary packages using `requirements.txt`:
       ```bash
       pip install -r requirements.txt
       ```

    ### Running the Application

    1. **Run the Flask Application**:
       ```bash
       python app.py
       ```
    2. **Access the Web Interface**:
       Open your browser and go to:
       ```
       http://127.0.0.1:5000/
       ```
       You can now upload images and start converting them!

    ## 📖 Usage

    ### Image Conversion

    1. **Upload Images**:
       Click on the "Select Images" button to upload one or more JPEG/PNG images.
    2. **Configure Output Settings**:
       - **Output Format**: Choose WebP, PNG, or JPEG.
       - **Adjust Dimensions (Optional)**: Set desired width and height.
       - **Adjust Quality (Optional)**: Define quality level (default is 80).
    3. **Preview Images**:
       Uploaded images will be displayed as a preview.
    4. **Convert**:
       Click on the "Convert" button:
       - For a single image, it will download directly.
       - For multiple images, the download will be in a ZIP file.

    ## 📁 Project Structure

    ```
    webp-image-converter/
    ├── app.py                # Flask application logic
    ├── templates/
    │   └── index.html        # Frontend HTML page for uploading images
    ├── requirements.txt      # Project dependencies
    ├── README.md             # Project documentation
    └── download_count.json   # (Optional) Persistent download count file
    ```

    ## 🧩 Dependencies

    - **Flask**: To build the web server.
    - **Pillow**: To handle image processing.
    - **Bootstrap**: For frontend styling.

    ## 📝 Example .gitignore

    It is recommended to include the following `.gitignore` file to keep unwanted files out of your repository:

    ```
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
    ```

    ## 🔮 Future Improvements

    - **User Authentication**: Allow users to create accounts to save their conversion history.
    - **Support for More Formats**: Add additional image formats like GIF, BMP, etc.
    - **Cloud Deployment**: Deploy the app to a cloud platform such as Heroku or AWS for easier access.

    ## 🤝 Contribution

    If you'd like to contribute, feel free to submit pull requests or open issues for new features or bug fixes.

    ### How to Contribute

    1. **Fork the Repository**.
    2. **Create a Feature Branch**:
       ```bash
       git checkout -b feature-name
       ```
    3. **Commit Your Changes**:
       ```bash
       git commit -m 'Add some feature'
       ```
    4. **Push to Your Branch**:
       ```bash
       git push origin feature-name
       ```
    5. **Create a Pull Request**.

    ## 📄 License

    This project is licensed under the MIT License. You are free to use, modify, and distribute this project, provided you include the original copyright notice.

    ## 📬 Contact

    If you have any questions or suggestions, feel free to reach out!

    - **GitHub**: [asufian97](https://github.com/asufian97)
    - **Email**: sufianwp97dot@gmail.com