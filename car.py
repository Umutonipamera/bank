 
class Car:
   
    def  __init__(self, name,model,color,registration):
        self.name=name
        self.model=model
        self.color=color
        self.registration=registration
    def stop(self):
        return f"Hello this {self.name} car always stops in the main road"
       

    def move(self):
        return f"Hello this {self.name}  car ,which is {self.model} in model,that has {self.color} color, and has {self.registration} registration number, it moves very faster"  
