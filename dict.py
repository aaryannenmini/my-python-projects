keys = {1:"God",2:"Ninja",3:"Sit",5:"Fiddlesticks",6:"toothpick",7:"pickle",8:"body",9:"jellybeans",11:"pogo stick",12:"football",13:"Goat"}

print(keys[1])
print(keys.get(4))
print(keys.get(10,"NOT FOUND"))
list = [1,2,3,4,5,6,7,8,9,10]
lists = ["one","two","three","four","five","six","seven","eight","nine","ten"]
dic=dict(zip(list,lists))
print(dic)
dic[11]="eleven"
print(dic)
del dic[11]
