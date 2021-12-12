

class DataLoad:
    def __init__(self, name: str):
        self.name = name
    
    def hello(self):
        print("hello" + self.name)
        return self.name