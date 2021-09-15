import boto3
from decouple import config
from botocore.exceptions import ClientError
from app.database.crud.bug import update_bug_data_for_media


SPACES_KEY = config("SPACES_KEY")
SPACES_SECRET = config("SPACES_SECRET")
SPACES_REGION = config("SPACES_REGION")
SPACE_NAME = config("SPACE_NAME")

# Initialize a session using DigitalOcean Spaces.
session = boto3.session.Session()
client = session.client(
    "s3",
    region_name=SPACES_REGION,
    endpoint_url=f"https://{SPACES_REGION}.digitaloceanspaces.com",
    aws_access_key_id=SPACES_KEY,
    aws_secret_access_key=SPACES_SECRET,
)


async def media_wrapper(id: str, files):
    media = []
    if files:
        for file in files:
            ctx = await file.read()
            singleMedia = await media_uploader(ctx, file.filename, file.content_type)
            if singleMedia["status"] == True:
                media.append(singleMedia["media_url"])
        updated_media = await update_bug_data_for_media(id, media)
        if updated_media == True:
            print("INFO: Media created.")
            return {"status": True}
    else:
        return {"status": False}


# upload a file.


async def media_uploader(file, file_name: str, content_type: str) -> dict:
    try:
        client.put_object(
            Bucket=SPACE_NAME,
            Key=file_name,
            Body=file,
            ACL="public-read",
            Metadata={
                "Content-Type": content_type,
            },
            CacheControl="36000000",
            ContentType=content_type,
        )
    except ClientError as e:
        print("INFO: Failed to upload image")
        print(f"Error: {e}")
        return {"status": False, "error": e}

    print(
        f"INFO: File object uploaded to https://{SPACE_NAME}.{SPACES_REGION}.digitaloceanspaces.com/{file_name}"
    )
    return {
        "status": True,
        "media_url": f"https://{SPACE_NAME}.{SPACES_REGION}.digitaloceanspaces.com/{file_name}",
    }
