 
class Dog:
  
    def __init__( self,name,color,age):
        self.name=name
        self.color=color
        self.age=age


    def bark(self):
        return f"Yesterday I heard {self.name} barking wowoo "

    def running(self):
        return f" yesterday I saw  a {self.name} which is {self.color}  in color running on the same day when it turns{self.age} years old"
