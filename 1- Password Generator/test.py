class TestClass:
    count = 0

    def __init__(self):
        TestClass.count += 1
    
    @classmethod
    def print_count(cls):
        print(TestClass.count)


a = TestClass()
b = TestClass()
c = TestClass()

print(a.count)

TestClass.print_count()

c.print_count()