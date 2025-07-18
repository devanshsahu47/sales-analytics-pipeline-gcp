from flask import Flask, request, render_template
from google.cloud import storage
from google.api_core import exceptions
import os

app = Flask(__name__)

# --- Configuration ---
# Using the Project ID you provided. Please double-check this is correct.
GCP_PROJECT_ID = 'project-101-466110' 

# Using a globally unique bucket name based on your Project ID.
GCS_BUCKET_NAME = 'bkt-sales-data-project-101-466110'

# Initialize the Google Cloud Storage client with your project ID
try:
    storage_client = storage.Client(project=GCP_PROJECT_ID)
except Exception as e:
    print("Could not create storage client. Please ensure you have authenticated correctly.")
    print(e)
    storage_client = None

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if not storage_client:
            return "Error: Storage client is not configured. Check your credentials and project ID.", 500

        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            try:
                # This will now correctly look for the new, unique bucket name.
                bucket = storage_client.bucket(GCS_BUCKET_NAME)
                blob = bucket.blob(file.filename)
                
                # Rewind the file stream before uploading
                file.seek(0)
                
                blob.upload_from_file(file)
                
                return f'File {file.filename} uploaded to {GCS_BUCKET_NAME}.'
            
            except exceptions.NotFound:
                return f"Error: Bucket '{GCS_BUCKET_NAME}' not found. Please create this bucket in your Google Cloud project.", 404
            except exceptions.Forbidden:
                return "Error: Permission denied. Ensure your service account has the 'Storage Admin' role.", 403
            except Exception as e:
                return f"An unexpected error occurred: {e}", 500
                
    return render_template('index.html')

if __name__ == '__main__':
    if 'GOOGLE_APPLICATION_CREDENTIALS' not in os.environ:
        print("-----------------------------------------------------------------")
        print("WARNING: The GOOGLE_APPLICATION_CREDENTIALS environment variable")
        print("is not set. The application may not be able to authenticate.")
        print("-----------------------------------------------------------------")

    app.run(debug=True)
