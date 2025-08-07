class car():

    def __init__(self,brand,model,year):
        self.b= brand
        self.m= model
        self.y= year
    def start_engine(self):
        print(f"engine started for {self.b}, {self.m},{self.y}")

vehicle= car("benz","f29", 2021)
vehicle.start_engine()
