def read_file(name):
    try:
        print('Read:', name)
        with open(name, 'rb') as f:
            return f.read()
    except:
        return 'error'

typemap = {
   '.txt': 'text/plain',
   '.html': 'text/html',
   '.csv': 'text/csv',
   '.xml': 'application/xml',
   '.json': 'application/json',
   '.bin': 'application/octet-stream',
   '.zip': 'application/zip',
   '.pdf': 'application/pdf',
   '.png': 'image/png',
   '.jpg': 'image/jpeg',
   '.gif': 'image/gif',
}
def to_content_type(ext):
    return  typemap[ext]

_image_pool = {}
def get_file(name):
    d = _image_pool.get(name)
    if d == None:
        d = read_file('files/data/' + name)
        if d != 'error':
            _image_pool[name] = d
    return d

