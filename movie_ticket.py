class movie:
    def __init__(self, movie_people, movie_name, movie_price):
        self.movie_people=movie_people
        self.movie_name=movie_name
        self.movie_price = movie_price

    def cost(self):
        return self.movie_people*self.movie_price
    def display(self):
        print(f"Your are watching the movie {self.movie_name} with {self.movie_people} people and the total cost is {self.cost()}")

x = input("What movie are you watching: ")

y = float(input("How much a ticket cost: "))

z = int(input("HOw many people are you going with: "))

p1 = movie(z,x,y)

p1.display()
        