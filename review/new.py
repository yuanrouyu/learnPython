print("sunlight".encode("ascii"))
print(b"sunlight".decode("ascii"))

print("中文".encode("utf-8"))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode("utf-8"))




print("汪汪".encode("utf-8"))
print(b'\xe6\xb1\xaa\xe6\xb1\xaa'.decode("utf-8"))



list 


menu=["duck","fish","tamato"]
print(menu)

first=menu[0]
print(first)

menu.append("cabage")
print(menu)

menu.pop(1)
print(menu)

menu.insert(2,"meet")
print(menu)

menu[1]="fish"
print(menu)


tuple

menu=("duck","fish","tamato","potato")
print(len(menu))

menu=("duck","fish",["tomato","potato"])
print(len(menu))
menu[2][0]="dog"
menu[2][1]='cat'
print (menu)


