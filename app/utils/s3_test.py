import boto3
import pprint
import io
import timeit

from make_env import get_env

env_variables = get_env()

IAM_PUBLIC = env_variables["IAM_PUBLIC"]
IAM_SECRET = env_variables["IAM_SECRET"]


session = boto3.session.Session()
bucket_name = "carddrafterstorage"

ENDPOINT = "https://storage.yandexcloud.net"

session = boto3.Session(
    aws_access_key_id=(env_variables["SA_KEY_ID"]),
    aws_secret_access_key=(env_variables["SA_SECRET_KEY"]),
    region_name="ru-central1",
)

s3 = session.client(
    "s3", endpoint_url=ENDPOINT)


def getObjectImg():
    object = s3.get_object(Bucket=bucket_name, Key="icons/c_0001.png")

print(timeit.timeit(getObjectImg, number=10))