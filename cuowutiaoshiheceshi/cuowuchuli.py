try:
    print('try')
    r=10/int('2')
    print('result:',r)
except ValueError as e:
    print('ValueError:',e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
else:
    print('no error!')
finally:
    print('finally')
print('end')

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')

import logging
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)   

main()
print('end')
class fooerror(ValueError):
    pass
def foo(s):
    n=int(s)
    if n==0:
        raise ValueError('invalid value:%s'%s)
    return 10/n
def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise
bar()


try:
    10/0
except ZeroDivisionError:
    raise ValueError('input error')


