const fs = require('fs');
const AWS = require('aws-sdk');
const secret_info = require('./secret_info');
var mime = require('mime-types');

const s3 = new AWS.S3({
    accessKeyId: secret_info.accessKeyId,
    secretAccessKey: secret_info.secretAccessKey
});

const constDir = "folder";

function getFiles (dir, files_, names_){
    files_ = files_ || [];
    names_ = names_ || [];
    var files = fs.readdirSync(dir);
    for (var i in files){
        var name = dir + '/' + files[i];
        if (fs.statSync(name).isDirectory()){
            getFiles(name, files_, names_);
        } else {
            files_.push(name);
            
            nameSplit = name.split(constDir + '/');
            
            nameSplit.shift();
            names_.push(nameSplit.join(constDir + '/'));
            contentType = mime.lookup(name);
            uploadFile(name, nameSplit.join(constDir + '/'), contentType)
            
        }
    }
    return {
        files: files_,
        names: names_
    }
}

const uploadFile = (fileName, fileKey, _contentType) => {
  
    
    const fileContent = fs.readFileSync(fileName);


    
    const params = {
        ACL:'public-read',
        ContentType: _contentType,
        Bucket: "test-bucket",
        Key: fileKey,
        Body: fileContent
    };

  
    s3.upload(params, function(err, data) {
        if (err) {
            throw err;
        }
        console.log(`File uploaded successfully. ${data.Location}`);
    });
};

console.log(getFiles(constDir))

