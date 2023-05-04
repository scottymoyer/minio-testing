from minio import Minio
from minio.error import S3Error


def main():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio(
        "play.min.io",
        access_key="Q3AM3UQ867SPQQA43P2F",
        secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
    )

    # Make 'playful-puppies' bucket if not exist.
    found = client.bucket_exists("playful-puppies")
    if not found:
        client.make_bucket("playful-puppies")
    else:
        print("Bucket 'playful-puppies' already exists")

    # Upload '/Users/scottymoyer/minio-project/puppies.jpeg' as object name
    # 'puppy-object' to bucket 'playful-puppies'.
    client.fput_object(
        "playful-puppies", "puppy-object", "/Users/scottymoyer/minio-project/puppies.jpeg",
    )
    print(
        "'/Users/scottymoyer/minio-project/puppies.jpeg' is successfully uploaded as "
        "object 'puppy-object' to bucket 'playful-puppies'."
    )


if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)