# http.server supports only 'GET' and 'HEAD' request methods.
# So it can serve files only.

from requests import get

def get_test(url):
    res = get(url)			# Response object
    res_txt = res.content.decode()
    print(res_txt)

get_test('http://127.0.0.1:8080')
##get_test('http://127.0.0.1:8080/hello.html')

