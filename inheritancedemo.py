from classdemo2 import Calculator


class Child(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 5, 10)

    def getcompletedata(self):
        return self.num2 + self.Addition() + self.num


obj = Child()
obj.getcompletedata()
print(obj.getcompletedata())