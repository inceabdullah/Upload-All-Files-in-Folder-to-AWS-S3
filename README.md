## Uploading All Files in AWS S3 Bucket

As you know, zip files could not unzip on the **S3 bucket**, so, all files in the folder `folder/` will be uploaded to `S3 bucket`

### Python

[ls](ls.py) function is given from [Ati_News_Algo_on_Docker_Quart_Flask_Controled](https://github.com/inceabdullah/Haber-Tellali-3th-Wave-News-Service/blob/master/aws-fargate-docker-container/flask%2B/Ati_News_Algo_on_Docker_Quart_Flask_Controled/quart_flask/app.py) but slightly changed added `path`

File `Content-Type` gets from `magic` build-in module. [How to find the mime type of a file in python? - Stackoverflow](https://stackoverflow.com/questions/43580/how-to-find-the-mime-type-of-a-file-in-python?answertab=votes#tab-top)

`secret_info.py`:
```python
aws_access_key_id = "XXXXXXXXXXX"
aws_secret_access_key = "XXXXXXXXXXXXXXXXXXXXXX"
```

#### Pip

Required module is just `boto3`

please: `pip3 install boto3`


### NodeJS

For `ls` files is used [How do you get a list of the names of all files present in a directory in Node.js? - Stackoverflow](https://stackoverflow.com/questions/2727167/how-do-you-get-a-list-of-the-names-of-all-files-present-in-a-directory-in-node-j)

For uploading function, [Uploading Files to AWS S3 with Node.js](https://stackabuse.com/uploading-files-to-aws-s3-with-node-js/) is used.

`secret_info.js` is like:
```javascript
module.exports = {
    accessKeyId: "XXXXXXXXXXXXXX",
    secretAccessKey: "XXXXXXXXXXXXXXXXXXXXXXXXx"
};
```