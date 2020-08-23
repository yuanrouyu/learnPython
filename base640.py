import base64
a=base64.b64encode(b'binary\x00string')
print(a)
c=base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
print(c)
b=base64.b64decode(b'i\xb7\x1d\xfb\xef\xff')
print(b)
s=base64.urlsafe_b64decode(b'i\xb7\x1d\xfb\xef\xff')
print(s)

def safe_base64_decode(s):
    if len(s)%4==0:
        k=0
    else:
        k=4-len(s)%4
    result=s+b'='*k
    return base64.b64decode(result)
