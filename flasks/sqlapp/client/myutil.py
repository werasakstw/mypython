from requests import get, delete, post, put

def send_get(path):
   return get(path).content.decode()

def send_delete(path):
   return delete(path).content.decode()

def send_post(path, data):
   return post(path, data=data).content.decode()

def send_put(path, data):
   return put(path, data=data).content.decode()

