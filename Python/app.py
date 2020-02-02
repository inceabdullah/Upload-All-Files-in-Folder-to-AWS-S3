import ls
from contentType import Content as contentType
import secret_info
import boto3

client = boto3.client(
    's3',
    aws_access_key_id=secret_info.aws_access_key_id,
    aws_secret_access_key=secret_info.aws_secret_access_key
    ) 

lsFolder = ls.ls_dir("folder")
files = lsFolder["files"]
fPaths = lsFolder["fPaths"]

for _file in files:
    openFile = open(_file, "rb")
    _contentType = contentType(_file)
    client.put_object(
    ACL='public-read',
    ContentType= _contentType,
    Body=openFile.read(),
    Bucket='test-bucket',
    Key=fPaths[files.index(_file)]
    )
    openFile.close()
    print("Type: %s \r\nPath: %s" % (_contentType, _file))

