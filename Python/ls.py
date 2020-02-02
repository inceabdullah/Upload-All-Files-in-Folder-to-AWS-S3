import os

def ls_dir(path):

    currentPath = os.path.abspath(os.getcwd())
    #print("current: %s" % (currentPath))
    
    path = os.path.join(currentPath, path)
    #print("path: %s" % (path))

    #print(path)
    files = []
    roots = []
    fPaths = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))
            roots.append(os.path.join(r))
            fPaths.append(os.path.join(r, file).replace(path, "", 1)[1:])
    return {
        "files":files,
        "files_number":len(files),
        "roots": roots,
        "fPaths": fPaths
            }