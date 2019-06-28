import random

class Player:
    def __init__ (self, name):
        self.name = name 
        self.count=0

    def get_name (self):
        return self.name

    def play_count (self):
        self.count+=1

    def get_count(self):
        return self.play_count

p1=Player("Siri")
print (p1.get_name())

