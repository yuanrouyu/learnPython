try:
    n=int(input("how old are you?"))
    percent=round(n*100/80,1)
    print("you have gone through",percent,"% of your life!")
except ValueError:
    print("oops,must ebter a number")
except ZeroDivisionError:
    print("division by zero")
except:
    print("something went very wrong.")

