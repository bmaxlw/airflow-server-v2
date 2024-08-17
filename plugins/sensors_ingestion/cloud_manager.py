from boto3 import Session
from botocore.client import ClientError

class CloudManager:

    def __init__(self, aws_access_key_id: str, aws_secret_access_key: str) -> None:
        self.aws_session = Session(aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    def create_S3_bucket(self, bucket_name: str, bucket_location: str) -> None:
        s3 = self.aws_session.resource('s3')
        try:
            s3.meta.client.head_bucket(Bucket=bucket_name)
        except ClientError:
            s3.create_bucket(Bucket=bucket_name, 
                            CreateBucketConfiguration={'LocationConstraint': bucket_location})
            
    # def load_JSON_into_S3_bucket(self, processed_responses: list[str]):
    #     s3 = self.aws_session.resource("s3")
    #     for response in processed_responses:
    #         s3.Object(get_dt(), f"{response.get('ticker')}{get_ms()}.json").put(
    #             Body=dumps(response)
    #         )
