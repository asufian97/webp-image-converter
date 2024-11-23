 <h1>WebP Image Converter</h1>
    <p>
        <strong>WebP Image Converter</strong> is a simple <strong>web-based tool</strong> built using Flask to convert images between formats such as JPEG, PNG, and WebP. 
        It supports single or multiple image conversion, with multiple images packaged as a ZIP file for easy download.
    </p>

    <h2>✨ Features</h2>
    <ul>
        <li><strong>Convert Single or Multiple Images</strong>: Easily convert JPEG/PNG images to WebP, PNG, or JPEG.</li>
        <li><strong>Flexible Output Settings</strong>: Adjust image dimensions (width and height) and quality.</li>
        <li><strong>Convenient Download</strong>: Single images are downloaded directly, while multiple images are provided in a ZIP file.</li>
        <li><strong>Image Preview</strong>: Users can preview uploaded images before converting.</li>
    </ul>

    <h2>🛠️ Tech Stack</h2>
    <ul>
        <li><strong>Backend</strong>: Python 3, Flask</li>
        <li><strong>Frontend</strong>: HTML5, CSS3, JavaScript, Bootstrap 5</li>
        <li><strong>Dependencies</strong>: Flask, Pillow (image processing)</li>
    </ul>

    <h2>🚀 Installation</h2>
    <p>To set up the project locally, follow these steps:</p>

    <h3>Prerequisites</h3>
    <ul>
        <li>Python 3.7+</li>
        <li><code>pip</code> (Python package installer)</li>
        <li>Git</li>
    </ul>

    <h3>Steps to Set Up Locally</h3>
    <ol>
        <li><strong>Clone the Repository</strong>:
            <pre class="command-line">
git clone https://github.com/asufian97/webp-image-converter.git
            </pre>
        </li>
        <li><strong>Navigate to the Project Directory</strong>:
            <pre class="command-line">
cd webp-image-converter
            </pre>
        </li>
        <li><strong>Create a Virtual Environment</strong>: It is recommended to create a virtual environment to keep dependencies isolated.
            <pre class="command-line">
python -m venv venv
            </pre>
        </li>
        <li><strong>Activate the Virtual Environment</strong>:
            <p><strong>Windows:</strong></p>
            <pre class="command-line">
venv\Scripts\activate
            </pre>
            <p><strong>macOS/Linux:</strong></p>
            <pre class="command-line">
source venv/bin/activate
            </pre>
        </li>
        <li><strong>Install the Requirements</strong>: Install the necessary packages using <code>requirements.txt</code>:
            <pre class="command-line">
pip install -r requirements.txt
            </pre>
        </li>
    </ol>

    <h3>Running the Application</h3>
    <ol>
        <li><strong>Run the Application</strong>:
            <pre class="command-line">
python app.py
            </pre>
        </li>
        <li><strong>Access the Web App</strong>: Open your browser and go to:
            <pre class="command-line">
http://127.0.0.1:5000/
            </pre>
            <p>The web interface will allow you to upload images and convert them as needed.</p>
        </li>
    </ol>

    <h2>📖 Usage</h2>
    <h3>Image Conversion</h3>
    <ol>
        <li><strong>Upload Images</strong>: Use the "Select Images" button to upload one or more images (JPEG/PNG).</li>
        <li><strong>Configure Output Settings</strong>:
            <ul>
                <li><strong>Select Output Format</strong>: WebP, PNG, or JPEG.</li>
                <li><strong>Adjust Dimensions (Optional)</strong>: Set width and height to resize the images.</li>
                <li><strong>Adjust Quality (Optional)</strong>: Set the quality level (default is 80).</li>
            </ul>
        </li>
        <li><strong>Preview</strong>: Uploaded images will appear as previews before conversion.</li>
        <li><strong>Convert</strong>: Click on the "Convert" button to process and download the images.
            <ul>
                <li>For a single image, it will download directly.</li>
                <li>For multiple images, the download will be in a ZIP file.</li>
            </ul>
        </li>
    </ol>

    <h2>📁 Project Structure</h2>
    <pre>
webp-image-converter/
├── app.py                # Flask application logic
├── templates/
│   └── index.html        # Frontend HTML page for uploading images
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
└── download_count.json   # (Optional) Persistent download count file
    </pre>

    <h2>🧩 Dependencies</h2>
    <ul>
        <li><strong>Flask</strong>: For building the web server.</li>
        <li><strong>Pillow</strong>: For handling image conversion.</li>
        <li><strong>Bootstrap</strong>: For styling the frontend.</li>
    </ul>

    <h2>📝 Example .gitignore</h2>
    <p>It is recommended to include the following <code>.gitignore</code> to keep unwanted files out of your repository:</p>
    <pre>
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
    </pre>

    <h2>🔮 Future Improvements</h2>
    <ul>
        <li><strong>User Authentication</strong>: Allow users to create accounts to store their conversion history.</li>
        <li><strong>Support for More Formats</strong>: Add support for other image formats like GIF, BMP, etc.</li>
        <li><strong>Cloud Deployment</strong>: Deploy the app on a cloud service like Heroku or AWS.</li>
    </ul>

    <h2>🤝 Contribution</h2>
    <p>Feel free to submit pull requests or open issues if you want to contribute to the project or suggest new features.</p>

    <h3>How to Contribute</h3>
    <ol>
        <li><strong>Fork the Repository</strong>.</li>
        <li><strong>Create a Feature Branch</strong>:
            <pre class="command-line">
git checkout -b feature-name
            </pre>
        </li>
        <li><strong>Commit Your Changes</strong>:
            <pre class="command-line">
git commit -m 'Add some feature'
            </pre>
        </li>
        <li><strong>Push to Your Branch</strong>:
            <pre class="command-line">
git push origin feature-name
            </pre>
        </li>
        <li><strong>Create a Pull Request</strong>.</li>
    </ol>

    <h2>📄 License</h2>
    <p>
        This project is licensed under the MIT License. You are free to use, modify, and distribute this project as long as you include the original copyright notice.
    </p>

    <h2>📬 Contact</h2>
    <p>
        If you have any questions or suggestions, feel free to reach out!
    </p>
    <ul>
        <li><strong>GitHub</strong>: <a href="https://github.com/asufian97">asufian97</a></li>
        <li><strong>Email</strong>: sufianwp97dot@gmail.com</li>
    </ul>