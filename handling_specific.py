try:
    a=int(input("tell me one number:"))
    b=int(input("tell me another number:"))
    print("a/b=",a/b)
    print("a+b=",a+b)
except ValueError:
    print("could not convert to a number.")
except ZeroDivisionError:
    print("can not divide by zero")
except:
    print("something were very wrong")
