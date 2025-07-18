from google.cloud import storage
from google.api_core import exceptions

# --- Configuration ---
# Using the Project ID you provided. Please double-check this is correct.
GCP_PROJECT_ID = 'project-101-466110' 

# Using a globally unique bucket name based on your Project ID.
GCS_BUCKET_NAME = 'bkt-sales-data-project-101-466110'

print(f"--- Starting GCS Connection Check for project: {GCP_PROJECT_ID} ---")
print(f"--- Checking for bucket: {GCS_BUCKET_NAME} ---")

try:
    # 1. Initialize the client, pointing to your specific project.
    print("\nStep 1: Initializing Google Cloud Storage client...")
    storage_client = storage.Client(project=GCP_PROJECT_ID)
    print("Step 1: Success! Client initialized.")

    # 2. Try to get the specific bucket.
    # This is a more direct test than listing all buckets.
    print(f"\nStep 2: Attempting to get bucket '{GCS_BUCKET_NAME}'...")
    bucket = storage_client.get_bucket(GCS_BUCKET_NAME)
    print("Step 2: Success! Found bucket.")
    
    print("\n--- DIAGNOSIS ---")
    print("SUCCESS! Your credentials, project ID, and bucket name are all correct.")
    print("You can now run your main Flask application.")


except exceptions.NotFound as e:
    print("\n---!!! ENCOUNTERED A 'NOT FOUND' ERROR !!! ---")
    print(f"ERROR: The system could not find the bucket named '{GCS_BUCKET_NAME}'.")
    print("This could be because:")
    print("  a) The Project ID is still incorrect.")
    print("  b) You have not yet created a bucket with this exact name.")
    print("  c) There is a typo in the bucket name in this script.")
    print("\nOriginal Error:", e)


except exceptions.Forbidden as e:
    print("\n---!!! ENCOUNTERED A PERMISSION ERROR !!! ---")
    print("ERROR: 403 Forbidden.")
    print("This means your service account key is VALID, but the account does not have the required permissions.")
    print("SOLUTION: Go to the IAM page in your Google Cloud project and grant the service account the 'Storage Admin' role.")
    print(e)

except Exception as e:
    print(f"\n---!!! AN UNEXPECTED ERROR OCCURRED !!! ---")
    print("This could be a problem with your credentials file path or project ID.")
    print(e)
