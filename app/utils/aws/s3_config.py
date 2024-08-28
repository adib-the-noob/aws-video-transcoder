import boto3
import os
from dotenv import load_dotenv
load_dotenv()

from boto3.s3.transfer import TransferConfig

aws_access_key_id = os.getenv("ACCESS_KEY")
aws_secret_access_key = os.getenv("SECRET_KEY")
aws_session_token = os.getenv("SESSION_TOKEN")


s3_client = boto3.client('s3')

def upload_raw_video(
    file_name: str,
    bucket_name: str,
    object_name: str = None,
):
    if object_name is None:
        object_name = file_name
        
    config = TransferConfig(
        multipart_threshold=1024 * 25, # 25 MB # The size threshold in bytes for use of multipart uploading
        multipart_chunksize=10 * 1024 * 1024, # 10 MB
        max_concurrency=10, # 10 threads
        use_threads=True
    )
    
    try:
        _ = s3_client.upload_file(
            Filename=file_name,
            Bucket=f"raw_vide/{bucket_name}/",
            Key=object_name,
            # object_name=object_name,
            Config=config
        )
        return {
            'status': 'success',
            'file_path': f"https://{bucket_name}.s3.amazonaws.com/{object_name}"
        } 

    except Exception as e:
        raise e
    
# x = upload_raw_video("meme.mp4", "adib-source-bucket") # // testing purpos
# print(x) # // testing purpose

# will call this function in save function when a video is uploaded.
