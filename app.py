from flask import Flask, request, send_file, render_template, jsonify
from PIL import Image
import io
import os
import zipfile
import logging
import json

app = Flask(__name__)

# Set maximum upload size to 10MB
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  

# Set up logging
logging.basicConfig(level=logging.INFO)

# Persistent counter file
COUNTER_FILE = "download_count.json"

# Load the current count from file, if it exists
def load_download_count():
    if os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, "r") as file:
            data = json.load(file)
            return data.get("count", 0)
    return 0

# Save the current count to file
def save_download_count(count):
    with open(COUNTER_FILE, "w") as file:
        json.dump({"count": count}, file)

# Initialize download count
download_count = load_download_count()

@app.route('/')
def index():
    return render_template('index.html', download_count=download_count)

@app.route('/convert', methods=['POST'])
def convert():
    global download_count
    files = request.files.getlist('image')
    output_format = request.form.get('format', 'WEBP').upper()
    width = request.form.get('width', type=int)
    height = request.form.get('height', type=int)
    quality = request.form.get('quality', type=int, default=80)

    if not files:
        return "No files uploaded", 400

    # Handling a single file
    if len(files) == 1:
        file = files[0]
        try:
            image = Image.open(file)

            # Resize if width and height are provided
            if width and height:
                image = image.resize((width, height))

            # Convert and save the image in memory
            output_io = io.BytesIO()
            image.save(output_io, format=output_format, quality=quality)
            output_io.seek(0)

            # Update and save the download count
            download_count += 1
            save_download_count(download_count)

            # Return the single converted image
            return send_file(
                output_io,
                mimetype=f'image/{output_format.lower()}',
                as_attachment=True,
                download_name=f'converted_image.{output_format.lower()}'
            )
        except Exception as e:
            logging.error(f"Error converting {file.filename}: {e}")
            return f"An error occurred while converting {file.filename}", 500

    # Handling multiple files - return a zip
    zip_io = io.BytesIO()

    with zipfile.ZipFile(zip_io, mode='w', compression=zipfile.ZIP_DEFLATED) as zipf:
        for idx, file in enumerate(files):
            try:
                image = Image.open(file)

                # Resize if width and height are provided
                if width and height:
                    image = image.resize((width, height))

                # Convert and save the image in memory
                output_io = io.BytesIO()
                image.save(output_io, format=output_format, quality=quality)
                output_io.seek(0)

                # Add the converted image to the zip file
                zipf.writestr(f'converted_image_{idx + 1}.{output_format.lower()}', output_io.read())

                logging.info(f"Successfully converted {file.filename}")
            except Exception as e:
                logging.error(f"Error converting {file.filename}: {e}")
                return f"An error occurred while converting {file.filename}", 500

    zip_io.seek(0)

    # Update and save the download count
    download_count += len(files)
    save_download_count(download_count)

    return send_file(
        zip_io,
        mimetype='application/zip',
        as_attachment=True,
        download_name='converted_images.zip'
    )

@app.route('/get_download_count', methods=['GET'])
def get_download_count():
    return jsonify({"count": download_count})

@app.route('/favicon.ico')
def favicon():
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)
