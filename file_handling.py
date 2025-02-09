with open("test.txt","w")as file:
    file.write("hi")
    file.write("food")
    file.write("I need")

with open("test.txt","r")as file:
    conetnt = file.read()
    print(conetnt)

