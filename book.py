class book:
    title =  "The million Dollar Race"
    author = "Matthew Ross Smith"


book1 = book
book2 = book

print(book1.title)
print(book2.author)

book1.title = "Diary of the wimpy kid"
print(book1.title)

book2.author = "Jeff Kinney"
print(book2.author)
print("___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
class bookk:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display(self):
        print(f"Title:{self.title},Author:{self.author}")

bookk1 = bookk("Touchdown Kid","Tim Green")
bookk2 = bookk("The lion of Mars","Jennnifer l. Holm")

bookk1.display()
bookk2.display()

print("____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")

class person:
    def __init__(self,name,yob):
        self.name= name
        self.yob = yob

    def calc_age(self,curr_year):
        age = curr_year - self.yob
        return age

    def desplay(self):
        print(f"{self.name} is {self.calc_age(2024)} YEARS OLD")

person1=person("Premlata",756)
person2 = person("Tut",1341)

person1.desplay()
person2.desplay()
