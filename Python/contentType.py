import magic
mime = magic.Magic(mime=True)

def Content(filePath):
    return mime.from_file(filePath)