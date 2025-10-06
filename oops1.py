class employee:

    def __init__(self):
        # print('Started attributes/data')
        print(id(self))
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print('Ended attributes/data')
    
    def travel(self):
        print('This travel method was called manually')
        print(f"Employee is now travelling to delhi")


sam = employee()
sam.name = "Sam"
print(id(sam))
print(sam.name)
# print(sam.salary)

sam.travel()