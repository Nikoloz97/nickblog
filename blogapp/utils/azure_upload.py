from azure.storage.blob import BlobServiceClient
from django.conf import settings
import uuid
import re

def upload_to_azure(file, blog_title):
    print(f"Uploading: {file.name}, Size: {file.size / (1024 * 1024):.2f} MB")
    container_name = 'posts'

    # Normalize prefix
    prefix = re.sub(r'[^a-z0-9-]', '', blog_title.lower().replace(' ', '-'))

    blob_service_client = BlobServiceClient(
        account_url=f"https://{settings.AZURE_ACCOUNT_NAME}.blob.core.windows.net/",
        credential=settings.AZURE_ACCOUNT_KEY
    )

    # Create the container if it doesn’t exist
    container_client = blob_service_client.get_container_client(settings.AZURE_CONTAINER_NAME)
    try:
        container_client.get_container_properties()
    except Exception as e:
        print(f"Container does not exist or error occurred: {e}")

    # Generate blob name with "folder-like" prefix
    file_extension = file.name.split('.')[-1]
    blob_name = f"{prefix}/{uuid.uuid4()}.{file_extension}"

    # Upload
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    blob_client.upload_blob(file, overwrite=True)

    return f"https://{settings.AZURE_ACCOUNT_NAME}.blob.core.windows.net/{container_name}/{blob_name}"

