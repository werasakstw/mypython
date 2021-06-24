from myutil import send_get, send_post, send_put, send_delete

print('Init:', send_get('http://127.0.0.1:8081/student/init'))
print('Get:', send_get('http://127.0.0.1:8081/student/get/1'))
print('List:', send_get('http://127.0.0.1:8081/student/list'))

print(send_put('http://127.0.0.1:8081/student/save',  \
	data={'sid': 2, 'name': 'Jim', 'dep': 'ee', 'gpa': 1.4 }))
print('List:', send_get('http://127.0.0.1:8081/student/list'))

print(send_post('http://127.0.0.1:8081/student/update/5', data={'gpa': 2.4}))
print('List:', send_get('http://127.0.0.1:8081/student/list'))

print(send_delete('http://127.0.0.1:8081/student/delete/5'))
print('List:', send_get('http://127.0.0.1:8081/student/list'))
