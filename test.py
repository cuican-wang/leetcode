class TestClass(object):
    def __init__(self):
        print("in init")

    def testFunc(self):
        print("in Test Func")

testInstance = TestClass()
#in init
testInstance.testFunc()
#in Test Func