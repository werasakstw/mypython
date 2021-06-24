from myutil import send_get, send_post

print(send_get('http://127.0.0.1:8080/pathparam/1/John'))
print(send_get('http://127.0.0.1:8080/querystr?name=jack&id=2'))
print(send_get('http://127.0.0.1:8080/querystr?name=joe&id=3'))
print(send_post('http://127.0.0.1:8080/form', data={'id': 4, 'name': 'Jame'}))



