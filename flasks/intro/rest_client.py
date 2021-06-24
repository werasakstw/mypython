from myutil import send_get, send_post, send_put, send_delete

print(send_get('http://127.0.0.1:8080/student/list'))
print(send_get('http://127.0.0.1:8080/student/get/1'))
print(send_delete('http://127.0.0.1:8080/student/delete/1'))
print(send_post('http://127.0.0.1:8080/student/update/1', data={'name': 'Jame'}))
print(send_put('http://127.0.0.1:8080/student/save',  data={'id': 2, 'name': 'Jack'}))

