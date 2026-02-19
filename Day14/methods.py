# method ??
# function which is inside a class 

# types :
# Instance method

class Instance_method:

    def intro(self):
        print("executed automatically ")

    def Timepass(self):
        print("timepass successfully done")

obj=Instance_method()
obj.intro()
obj.Timepass()


class Instance_method:

    def __init__(self,name):
        self.name=name
        print("executed automatically ")

    def Timepass(self):
        print(self.name)

obj=Instance_method("Naseem")
obj.Timepass()



# class method

class Class_method:

    name="Meenakshi"

    @classmethod
    def Timepass(cls):
        print(cls.name)


Class_method.Timepass()


# Static method 

class Static_method:

    @staticmethod
    def Timepass():
        name="Meenakshi"
        print(name)

Static_method.Timepass()




