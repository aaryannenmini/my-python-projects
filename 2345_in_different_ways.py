class dog:
    def sound(self):
        return "BARK WOOF"
    


class cut:
    def sound(self):
        return "roar"
    

class lion:
    def sound(self):
        return "ROARRR"
    
aniamal = [dog(),cut(),lion()]
for i in aniamal:
    print(i.sound())



class circle:
    def area(self,radius):
        
        return 3.14*radius*radius
    

class tri:
    def area(self,height,base):
        return (height * base)/2

class rec:
    def area(self,lenght,width):
        return lenght*width

shape = [circle(),tri(),rec()] 

print(f"Circle area: {shape[0].area(5)}")
print(f"Triangle area: {shape[1].area(5,7)}")
print(f"Rectangle area: {shape[2].area(5,9)}")


class football:
    def rules(self):
        return "You can't throw passed the line of scrimmage and it is a safety if you start out of the endzone and you get downed in your endzone and you give them 2  points and they get the ball back from a punt"
    
class basketball:
    def rules(self):
        return " You can't hold on to the ball for more than 1 minute you haveto score in that time or else it is a penalty and the opposing team will get the ball back and you can not gaurd the basket or it will be a foul and will result in a free throw for the other team"


sport = [football(),basketball()]

for i in sport:
    print(f"{i.__class__.__name__}: {i.rules()}")


