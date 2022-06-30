# Self Keyword is mendatory for calling variable into classes
# Instance and class variable both have different purpose
# Constructor name should be def __init__()
# new keyword is not required when we create object of the class
class Calculator:
    num = 100

    def __init__(self, a, b):
        self.firstnumber = a
        self.secondnumber = b

    def Addition(self):
        return self.firstnumber + self.secondnumber + Calculator.num


obj = Calculator(10, 20)
print(obj.Addition())
